# Relatório de merge: agent-skills -> agent

Data: 2026-11-05

## Regra
Este repositório (`agent`) é a base. Para skills com o mesmo nome em `tayobinha/agent-skills`:
- idênticas (352): nada a fazer;
- diferentes (1.092): mantida a versão do `agent` (mais atual: campos `risk`/`date_added`, estrutura com `references/`), exceto quando a versão do `agent-skills` tem conteúdo total >15% maior E frontmatter válido (nesse caso foi adotada);
- skills só existentes no `agent` (1.135): mantidas;
- skills só existentes no `agent-skills`: nenhuma real (docx/pdf/pptx/xlsx lá são symlinks quebrados do Windows).

## Adotadas do agent-skills (19)

| Skill | bytes agent | bytes agent-skills |
|---|---|---|
| andrej-karpathy | 4145 | 53098 |
| api-security-best-practices | 11267 | 23777 |
| code-refactoring-context-restore | 2693 | 6567 |
| context-management-context-restore | 2613 | 6571 |
| distributed-tracing | 5488 | 10840 |
| error-debugging-error-analysis | 11112 | 37392 |
| error-debugging-multi-agent-review | 2787 | 7093 |
| error-diagnostics-error-analysis | 11032 | 37394 |
| git-pr-workflows-git-workflow | 5203 | 10466 |
| github-actions-templates | 5273 | 7919 |
| github-automation | 5356 | 11687 |
| google-sheets-automation | 2698 | 4325 |
| google-slides-automation | 2633 | 4470 |
| langfuse | 5795 | 12221 |
| pci-compliance | 4397 | 14162 |
| performance-testing-review-multi-agent-review | 2897 | 7115 |
| secrets-management | 4405 | 8374 |
| ui-component | 3249 | 3830 |
| zipai-optimizer | 5188 | 6372 |

## Maiores no agent-skills mas descartadas por frontmatter sem description (0)


## Skills de design (curated/design-ui)
As 10 skills pedidas foram adicionadas em `curated/design-ui/` com sync automático. Já existiam também em `skills/` (versão da biblioteca Awesome, possivelmente desatualizada): frontend-design, emil-design-eng, review-animations, ui-ux-pro-max, web-design-guidelines, webapp-testing. Novas no repositório: impeccable, create-design-md, mobile-native, break-ui. As cópias antigas em `skills/` não foram removidas.
