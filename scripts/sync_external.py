#!/usr/bin/env python3
"""Sincroniza skills externas listadas em curated/sources.json para curated/<categoria>/.

Uso: python scripts/sync_external.py [--check]
Grava o commit de origem em curated/sources.lock.json e regenera curated/design-ui/INDEX.md.
Só requer git e Python 3.8+.
"""
import json, os, shutil, subprocess, sys, tempfile, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CUR = os.path.join(ROOT, "curated")
SRC = os.path.join(CUR, "sources.json")
LOCK = os.path.join(CUR, "sources.lock.json")


def run(*a, cwd=None):
    return subprocess.run(a, cwd=cwd, check=True, capture_output=True, text=True).stdout.strip()


def main():
    cfg = json.load(open(SRC, encoding="utf-8"))
    cat = cfg["category"]
    dest_root = os.path.join(CUR, cat)
    os.makedirs(dest_root, exist_ok=True)
    lock = json.load(open(LOCK, encoding="utf-8")) if os.path.exists(LOCK) else {}
    clones = {}
    changed = []
    with tempfile.TemporaryDirectory() as tmp:
        for s in cfg["skills"]:
            key = (s["repo"], s["ref"])
            if key not in clones:
                d = os.path.join(tmp, str(len(clones)))
                run("git", "clone", "--depth", "1", "--branch", s["ref"], f"https://github.com/{s['repo']}", d)
                clones[key] = (d, run("git", "rev-parse", "HEAD", cwd=d))
            d, sha = clones[key]
            src = os.path.join(d, s["path"])
            if not os.path.isfile(os.path.join(src, "SKILL.md")):
                print(f"ERRO: {s['name']}: SKILL.md não encontrado em {s['repo']}/{s['path']}", file=sys.stderr)
                sys.exit(1)
            out = os.path.join(dest_root, s["name"])
            if os.path.isdir(out):
                shutil.rmtree(out)
            shutil.copytree(src, out, symlinks=False, ignore=shutil.ignore_patterns(".git"))
            prev = lock.get(s["name"], {}).get("commit")
            if prev != sha:
                changed.append(s["name"])
            lock[s["name"]] = {"repo": s["repo"], "path": s["path"], "commit": sha,
                               "synced_at": datetime.date.today().isoformat()}
    json.dump(lock, open(LOCK, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
    rows = ["# Índice: design-ui", "",
            "Skills externas, sincronizadas automaticamente de repositórios de origem (`scripts/sync_external.py`).",
            "Não edite estas pastas à mão: as mudanças são sobrescritas no próximo sync.", "",
            "| Skill | Quando usar | Origem |", "|---|---|---|"]
    for s in cfg["skills"]:
        l = lock[s["name"]]
        rows.append(f"| [{s['name']}]({s['name']}/SKILL.md) | {s['purpose']} | {s['repo']} @ `{l['commit'][:7]}` |")
    open(os.path.join(dest_root, "INDEX.md"), "w", encoding="utf-8").write("\n".join(rows) + "\n")
    print("Atualizadas:", ", ".join(changed) if changed else "nenhuma")


if __name__ == "__main__":
    main()
