# Metodologia: "O Efeito Homem de Ferro" (Scroll 3D Imersivo Institucional)

> Baseado nas referências de sites imersivos e no modelo "Iron Man Scrolling Effect". Este é o padrão exigido para transformar um site básico em uma experiência institucional de alto luxo (projetos precificados entre R$ 6.500 e R$ 9.000, conforme referências de mercado).

## 1. O Conceito Central
O site deixa de ser um "mosaico de imagens planas". Ele passa a ser uma janela para um ambiente tridimensional, onde o scroll do usuário funciona como o **controle remoto de uma máquina do tempo ou de uma câmera cinematográfica**.
Ao descer a página, um objeto (ou ambiente) 3D se move, se desmonta (efeito *Exploded View* como a armadura do Homem de Ferro) ou viaja pelo espaço.

## 2. Como é Feito Tecnicamente (A Matemática)
Existem duas formas absolutas de criar esse efeito imersivo sem explodir a memória do celular do cliente:

### A. O Método "Spline3D + ScrollTrigger" (Mais Rápido/Fácil)
Muito utilizado pelos canais de IA para "fazer sites 3D sem código".
- Você cria a cena no **Spline.design** (uma ferramenta 3D colaborativa na nuvem).
- Exporta o `<spline-viewer>` embed.
- Usa o **GSAP ScrollTrigger** no Javascript para injetar eventos de controle na câmera do Spline. Conforme o usuário rola a página, o GSAP aciona "Estados" (States) no Spline, fazendo o modelo 3D virar e desmontar suavemente na tela.

### B. O Método "Image Sequence Canvas" (O Padrão Apple / Hardcore)
- O objeto 3D é renderizado no Blender em um vídeo de 10 segundos com fundo transparente (formato PNG/WebP sequence de 300 quadros).
- O GSAP vincula a rolagem da página ao quadro atual da imagem dentro de um `<canvas>` de HTML5. A precisão é milimétrica e funciona 100% liso no iPhone.

## 3. Como Aplicaremos no Projeto Institucional
Para abandonar a "vibe de pedreiro rústico" e elevar para "Construtora Premium Institucional", a jornada muda:

1. **Hero (Cena 1):** Em vez de uma parede de tijolos estática, teremos o modelo 3D escuro de um empreendimento luxuoso. O texto flutua: "Engenharia de Vanguarda".
2. **Scroll 1 (A "Explosão"):** O usuário roda o scroll. A casa em 3D gira e se desmonta (As paredes levantam, os móveis ficam transparentes). O texto aparece: "Transparência Absoluta em Cada Camada do Projeto."
3. **Scroll 2 (A Base):** O modelo 3D foca na fundação (luzes acendem). Texto: "Sólidos como nossas fundações."
4. **Clímax:** A casa se remonta, ganha texturas hiper-realistas e o botão de contato "Agende uma Reunião com Nossos Engenheiros" surge.

## Próximos Passos (Ação Imediata)
Para aplicarmos essa metodologia, precisaremos injetar a biblioteca Spline (ou Canvas) no nosso `index.html` e substituir as imagens JPG paradas pelo container 3D.
