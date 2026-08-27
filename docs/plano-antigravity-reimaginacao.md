# Plano de execução — Reimaginação do iframe TM

## Estado atual

A implementação está isolada na branch `feature/reimaginar-iframe-hero`, baseada na `master`. O commit local de referência é `5f809c4` (`feat: reimagina hero cinematografico do iframe`). A master não foi modificada.

## O que foi implementado

O hero foi reorganizado para usar uma composição editorial lateral. O texto agora ocupa o terço esquerdo, enquanto o personagem permanece visualmente preservado no centro-direita. O título foi substituído por “Seu processo. Em órbita.”, acompanhado da proposta de valor, metadados de serviço e indicador de exploração.

O overlay uniforme foi substituído por uma composição de gradientes horizontal, vertical e radial. Isso aumenta o contraste onde o texto aparece sem apagar a fotografia cinematográfica. A navegação superior também recebeu tratamento de vidro mais discreto.

A animação agora usa o vídeo original Full HD, com 1.920 × 1.080 px, em vez dos 181 JPEGs reduzidos. O `currentTime` do vídeo é sincronizado com o progresso global do scroll usando `requestAnimationFrame`, e o poster garante uma primeira pintura estável antes de a metadata estar disponível. O HTML usa `muted`, `playsinline` e `preload="auto"` para manter o comportamento compatível com navegadores móveis.

## Arquivos

| Arquivo | Função |
| --- | --- |
| `index.html` | Hero, overlay, vídeo sincronizado ao scroll e responsividade revisados. |
| `assets-video-cover.mp4` | Vídeo original Full HD usado como fundo. |
| `hero-poster.jpg` | Poster de alta qualidade para a primeira pintura. |
| `.github/workflows/deploy-pages.yml` | Workflow de publicação no GitHub Pages. |
| `.github/issue-reimaginacao-iframe.md` | Checklist do escopo. |

## Critérios de aceite

A revisão deve confirmar que o texto não cobre o rosto do personagem em desktop, que o título permanece legível em mobile, que o scroll move o vídeo do primeiro ao último segundo, que o poster aparece antes do carregamento da metadata e que a página continua funcionando como documento estático sem dependências de build.

Também é importante verificar a política de autoplay/carregamento em dispositivos móveis e confirmar que o volume total dos assets é aceitável para o ambiente de publicação.

## Como visualizar

Para uma prévia local, execute `python3 -m http.server 4173` na raiz do projeto e abra `http://localhost:4173`. No ambiente desta execução, a prévia temporária foi disponibilizada em `https://4173-iffa5gmbeu06ucu9o4loz-f42a892c.us4.manus.computer`. O teste confirmou metadata de 10 segundos e sincronização de `currentTime` com o scroll.

## Como publicar

O workflow está preparado para publicar a branch `master` no GitHub Pages. Depois de enviar a branch de feature ao GitHub, abra um Pull Request para `master`. Após o merge, a Action `Deploy static site to GitHub Pages` fará o upload do conteúdo estático.

No repositório, habilite **Settings → Pages → Source: GitHub Actions**. O endereço final será exibido no ambiente `github-pages` da Action. Como esta sessão não possui autenticação de escrita no GitHub, o push da branch não foi executado; é necessário autenticar o GitHub CLI ou fazer o push manualmente.

## Comandos de continuação

```bash
git switch feature/reimaginar-iframe-hero
git push -u origin feature/reimaginar-iframe-hero
```

Depois, crie o Pull Request e faça o merge somente após a revisão visual. Para delegar ao Antigravity 2.0, forneça este arquivo junto com o commit `5f809c4` e peça que preserve a branch `master`, valide o hero em desktop/mobile e não substitua os 181 frames sem aprovação.
