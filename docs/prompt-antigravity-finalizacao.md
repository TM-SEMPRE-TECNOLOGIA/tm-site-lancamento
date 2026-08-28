# Handoff para Antigravity 2.0 — TM Sempre Tecnologia

## Contexto do projeto

Este repositório é um site institucional pessoal apresentado dentro de um iframe. A experiência não deve parecer uma landing page comercial tradicional. O conceito é uma narrativa visual de página única, com o vídeo como elemento dominante e o scroll como mecanismo de progressão da história.

A branch de trabalho é `feature/iframe-scroll-story`. A implementação atual está no commit `17f4543`, com o commit visual principal `38d9d61`. A branch `master` não deve ser alterada diretamente.

## Direção visual aprovada

A hero atual foi aprovada como direção. Ela usa o vídeo em tela inteira, um overlay cinematográfico, marca TM discreta, tipografia Inter, laranja queimado como cor de acento e textos editoriais mínimos. O personagem deve continuar sendo o foco visual. Não reintroduzir cards, grids de cases, modal, formulário, botão de CTA ou blocos comerciais.

A experiência deve parecer um filme interativo sobre evolução profissional e capacidade de transformar complexidade em sistemas. O texto entra e sai de forma elegante ao longo do scroll, sem competir com o rosto ou com a montagem da armadura.

## Problema técnico prioritário

O vídeo ainda pode aparentar travamento durante o scroll. Investigue isso antes de criar novas páginas. O vídeo está em `assets-video-cover.mp4`, com 1.920 × 1.080 px, 24 fps e 10 segundos. O HTML usa `preload="auto"`, `muted`, `playsinline` e sincroniza `video.currentTime` com o progresso da página usando `requestAnimationFrame`.

A versão foi reempacotada com `-movflags +faststart`. Ainda assim, o comportamento deve ser validado em uma hospedagem que suporte requisições Range e em dispositivos móveis. Não assumir que um servidor local simples tem o mesmo comportamento do GitHub Pages.

### Estratégia de investigação

Primeiro, medir o comportamento com `readyState`, `buffered`, `seekable`, `currentTime`, `seeking` e `seeked`. Verificar se o servidor responde com `Accept-Ranges: bytes` e `Content-Range`. Confirmar se o problema é rede, decodificação, excesso de seeks ou conflito entre o scroll e a busca do vídeo.

Depois, implementar uma fila de seeks: guardar somente o último tempo solicitado, ignorar seeks intermediários enquanto o vídeo estiver buscando e aplicar o valor mais recente após `seeked`. Usar um limiar mínimo de mudança, por exemplo entre 30 e 50 ms, para evitar centenas de seeks por segundo. Avaliar `requestVideoFrameCallback` quando disponível para manter a atualização sincronizada com frames realmente decodificados.

Testar também uma interpolação curta do progresso e um fallback de reprodução suave quando o scrubbing por seek não for confiável no dispositivo. Não converter novamente o vídeo para baixa resolução.

Se o scrubbing continuar irregular, avaliar três alternativas em ordem: vídeo com keyframes mais frequentes; divisão do vídeo em quatro capítulos com transições controladas; ou uma sequência de imagens extraída diretamente do vídeo Full HD, com quantidade reduzida e compressão de alta qualidade. A decisão deve ser baseada em teste real, não em preferência abstrata.

## Nova narrativa da Home

A copy atual é provisória e deve ser substituída. A narrativa correta é uma história de vitória profissional, não uma apresentação de uma empresa de construção ou de automação predial.

A história começa com a entrada do protagonista em uma empresa. Ao cair nos relatórios, ele tem o primeiro contato com desenvolvimento. Em vez de tratar os relatórios como tarefa operacional, ele enxerga um sistema: identifica o que é repetitivo, automatiza o processo e potencializa os relatórios em 85%. Esse é o momento de origem da capacidade técnica.

A narrativa deve evoluir da seguinte maneira:

| Momento | Ideia narrativa |
| --- | --- |
| Antes | Um ambiente cheio de relatórios, tarefas repetitivas e informação dispersa. |
| Descoberta | O primeiro contato com desenvolvimento acontece através dos relatórios. |
| Virada | O protagonista percebe que não precisa apenas executar o processo; pode redesenhá-lo. |
| Resultado | Os relatórios são potencializados em 85%, conforme o relato do próprio usuário. |
| Expansão | A mesma capacidade passa a ser aplicada a dados, automações, sistemas e experiências digitais. |
| Presente | A TM representa a forma de pensar: observar, estruturar, automatizar e entregar. |

Tratar “85%” como um marco visual importante, mas sem inventar uma metodologia, número adicional ou promessa empresarial que o usuário não forneceu. A copy deve ser pessoal e institucional ao mesmo tempo, em primeira pessoa quando contar a origem e em tom de marca quando apresentar a TM.

## Arquitetura proposta do site

### Home

A Home é o filme de origem. Deve conter apenas a hero e a narrativa de vitória distribuída pelo scroll. O vídeo permanece como fundo. A copy aparece em capítulos curtos, com bastante espaço negativo e transições de opacidade/posição. O encerramento deve apresentar a TM como assinatura profissional, não como uma tela de venda.

### Portfólio

A página de Portfólio deve seguir a mesma linguagem visual, mas sem virar uma grade de cards. Cada projeto deve ser apresentado como um estudo editorial de caso, com uma imagem ou vídeo dominante, contexto breve, problema, intervenção e resultado. A navegação entre projetos pode ser feita por sequência vertical ou links textuais discretos. O conteúdo deve mostrar amplitude: relatórios, automações, sistemas, interfaces, dados e experiências digitais. Construção e automação predial podem aparecer como parte da trajetória, mas não como limite da identidade profissional.

### Contato

A página de Contato deve ser silenciosa e direta. Evitar formulário complexo e chamadas agressivas. Usar uma composição limpa com uma frase de abertura, e-mail, LinkedIn, GitHub e WhatsApp somente se os links reais forem fornecidos. Não inventar URLs. O contato deve parecer uma continuação natural da história, com a ideia de “vamos transformar o próximo processo”.

## Navegação

A navegação deve ser discreta e textual, compatível com iframe. Usar no máximo marca TM e links simples para `Home`, `Portfólio` e `Contato`. Evitar menus expansivos, botões grandes e componentes que escondam o vídeo. Garantir que links funcionem tanto quando o site é aberto diretamente quanto quando é incorporado em iframe.

## Critérios de aceite

A entrega será considerada correta quando o vídeo não parecer travar durante o scroll em desktop e mobile; o tempo do vídeo acompanhar o progresso sem voltar para trás ou acumular seeks; a Home contar a história do primeiro contato com desenvolvimento por meio dos relatórios e do resultado de 85%; a identidade do site não ficar restrita à construção ou automação predial; Portfólio e Contato seguirem a mesma linguagem editorial; não existirem cards, modais, formulários comerciais ou CTAs agressivos; e a página funcionar como site estático dentro de iframe.

## Comandos e entrega

Preservar a branch `master`. Trabalhar na branch `feature/iframe-scroll-story` ou abrir uma nova branch derivada dela. Executar `git diff --check`, validar a página em servidor com suporte a Range e registrar os commits com Conventional Commits.

Depois de concluir, publicar a branch e abrir um Pull Request para `master`. O workflow `.github/workflows/deploy-pages.yml` já existe. Se a publicação do GitHub Pages for usada, habilitar **Settings → Pages → Source: GitHub Actions**.
