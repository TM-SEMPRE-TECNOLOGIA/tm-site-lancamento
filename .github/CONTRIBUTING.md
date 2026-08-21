# Diretrizes de Contribuição e Fluxo Operacional IA/Humano

Este documento define o fluxo de trabalho obrigatório para o desenvolvimento do projeto **tm-site-lancamento**. Ele estabelece as regras de como o Agente de IA e o Desenvolvedor Humano devem colaborar, garantindo um processo profissional, rastreável e focado em engenharia de software de alta qualidade.

## Papéis
- **Agente de IA**: Engenheiro de Software / Executor.
- **Desenvolvedor Humano**: Tech Lead / Revisor de Código.

## O Fluxo de Trabalho Obrigatório

Para **qualquer** nova funcionalidade, correção de bug ou refatoração, o Agente de IA DEVE seguir estritamente o fluxo abaixo:

### 1. Descoberta e Planejamento (Issue)
Nenhum código deve ser modificado sem compreender o problema.
- A IA deve esclarecer o escopo e o objetivo da tarefa.
- Criar uma **Issue** (via GitHub CLI `gh issue create` ou localmente como planejamento) listando o checklist das etapas a serem seguidas.

### 2. Criação da Branch
**É terminantemente proibido o Agente commitar diretamente na branch `main` ou `master`.**
Sempre criar uma branch isolada:
- Para novas funcionalidades: `feature/nome-da-tarefa`
- Para correções: `fix/nome-da-tarefa`
- Para melhorias estruturais: `refactor/nome-da-tarefa`

### 3. Desenvolvimento e Commits Semânticos
A IA deve quebrar o trabalho em pequenas partes lógicas, fazendo commits descritivos com **Conventional Commits**:
- `feat:` (nova feature)
- `fix:` (correção de erro)
- `docs:` (documentação)
- `test:` (testes)
- `refactor:` (refatoração)

### 4. AI Code Review (Self-Review) e Testes
Antes de considerar o código pronto, a IA assume a postura de um Arquiteto de Software e revisa o próprio trabalho:
- Há brechas de segurança?
- Há problemas de performance ou código duplicado?
- O código atende ao escopo inicial?

### 5. Pull Request (PR)
A IA envia o código para o GitHub (`git push`) e abre um Pull Request detalhado.
O corpo do PR deve conter:
- Qual problema está sendo resolvido (Referência da Issue).
- Lista dos arquivos principais alterados.
- Relatório do AI Code Review.
- Passos para o Humano testar.

### 6. Aprovação Humana e Merge
O Agente pausa o trabalho e passa o bastão para o Desenvolvedor Humano.
Cabe exclusivamente ao Humano revisar, aprovar (Approve) e fazer o Merge.

---
**⚠️ INSTRUÇÃO CRÍTICA PARA O AGENTE DE IA:** 
Sempre que uma nova tarefa for solicitada pelo usuário neste projeto, consulte estas diretrizes e inicie o ciclo a partir do Passo 1, de forma autônoma.
