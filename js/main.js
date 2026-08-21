// ── LENIS SMOOTH SCROLL ──
const lenis = new Lenis({
  duration: 1.2,
  easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)), // https://www.desmos.com/calculator/brs54l4xou
  direction: 'vertical',
  gestureDirection: 'vertical',
  smooth: true,
  mouseMultiplier: 1,
  smoothTouch: false,
  touchMultiplier: 2,
  infinite: false,
});

// Update ScrollTrigger whenever Lenis updates
lenis.on('scroll', ScrollTrigger.update);

// Sincroniza o RAF do Lenis e do GSAP
gsap.ticker.add((time)=>{
  lenis.raf(time * 1000);
});
gsap.ticker.lagSmoothing(0);

// ── CANVAS BACKGROUND ANIMATION (181 FRAMES) WITH GSAP ──
const canvas = document.getElementById('bg-canvas');
const ctx = canvas.getContext('2d');
let W, H;

function resizeCanvas() {
  W = canvas.width = window.innerWidth;
  H = canvas.height = window.innerHeight;
}
resizeCanvas();
window.addEventListener('resize', resizeCanvas);

const FRAME_COUNT = 181;
const FRAMES_PATH = 'frames/';
const images = [];
let loadedCount = 0;

// Objeto dummy para o GSAP animar (scrub) o índice do frame
const frameData = { frame: 1 };

function render(frameIdx) {
  const img = images[frameIdx];
  if (!img || !img.complete) return;
  const hRatio = W / img.width;
  const vRatio = H / img.height;
  const ratio = Math.max(hRatio, vRatio);
  const cx = (W - img.width * ratio) / 2;
  const cy = (H - img.height * ratio) / 2;
  ctx.clearRect(0, 0, W, H);
  ctx.drawImage(img, 0, 0, img.width, img.height, cx, cy, img.width * ratio, img.height * ratio);
}

// Pré-carrega frames
for (let i = 1; i <= FRAME_COUNT; i++) {
  const img = new Image();
  const num = String(i).padStart(3, '0');
  img.src = FRAMES_PATH + 'ezgif-frame-' + num + '.jpg';
  img.onload = () => { 
    loadedCount++; 
    if (loadedCount === 1) { 
      render(1); 
      initScrollTrigger(); // Inicia o ScrollTrigger quando a 1ª img carregar
    } 
  };
  images.push(img);
}

function initScrollTrigger() {
  gsap.to(frameData, {
    frame: FRAME_COUNT - 1,
    snap: "frame",
    ease: "none",
    scrollTrigger: {
      trigger: "body",
      start: "top top",
      end: "bottom bottom",
      scrub: 0.5, // Scrub de 0.5s para maior suavidade
      onUpdate: () => render(frameData.frame)
    }
  });
}

// ── PROGRESS BAR ──
const progressBar = document.getElementById('progress-bar');
gsap.to(progressBar, {
  width: "100%",
  ease: "none",
  scrollTrigger: {
    trigger: "body",
    start: "top top",
    end: "bottom bottom",
    scrub: true
  }
});

// ── ANIMAÇÕES DE ENTRADA (FADE IN UP) ──
gsap.utils.toArray('.section, .subsection, .footer').forEach(section => {
  gsap.fromTo(section, 
    { opacity: 0, y: 50 },
    { 
      opacity: 1, 
      y: 0, 
      duration: 1, 
      ease: "power3.out",
      scrollTrigger: {
        trigger: section,
        start: "top 80%", // Dispara quando o topo da seção atinge 80% da tela
        toggleActions: "play none none reverse"
      }
    }
  );
});

// ── STICKY HORIZONTAL (SCROLLTRIGGER) ──
function setupHorizontal(containerId, trackId, dotsId) {
  const track = document.getElementById(trackId);
  if(!track) return;
  const slides = track.querySelectorAll('.horizontal-slide');
  const dots = document.querySelectorAll(`#${dotsId} .h-dot`);
  
  // A largura total que precisa ser transladada
  const moveAmount = -100 * (slides.length - 1);
  
  const tween = gsap.to(track, {
    xPercent: moveAmount,
    ease: "none",
    scrollTrigger: {
      trigger: `#${containerId}`,
      start: "top top",
      end: () => `+=${window.innerHeight * (slides.length - 1)}`,
      pin: true,
      scrub: 1,
      onUpdate: (self) => {
        // Atualiza as bolinhas com base no progresso (0 a 1)
        const progress = self.progress;
        const activeIdx = Math.round(progress * (slides.length - 1));
        dots.forEach((d, i) => d.classList.toggle('active', i === activeIdx));
      }
    }
  });
}

// Substituímos os placeholders horizontais originais para usarem o GSAP
setTimeout(() => {
    setupHorizontal('h-container-3', 'h-track', 'h-dots');
    setupHorizontal('h-container-6', 'h-track-6', 'h-dots-6');
}, 100);


// ── SCROLL TO ──
window.scrollToSection = function(id) {
  const el = document.getElementById(id);
  if (el) { 
    lenis.scrollTo(el, { offset: 0, duration: 1.2 });
  }
}

// ── MODAL ──
const btnDecolar = document.getElementById('btn-decolar');
const modal = document.getElementById('modal-captura');

if(btnDecolar) {
  btnDecolar.addEventListener('click', () => {
    lenis.scrollTo(0, { duration: 1 });
    setTimeout(() => { 
      modal.classList.add('open'); 
      lenis.stop(); // Para o scroll enquanto o modal tá aberto
    }, 1000);
  });
}

document.getElementById('modal-close-btn').addEventListener('click', () => {
  modal.classList.remove('open'); 
  lenis.start(); 
});
modal.addEventListener('click', (e) => { 
  if (e.target === modal) { 
    modal.classList.remove('open'); 
    lenis.start(); 
  } 
});
document.addEventListener('keydown', (e) => { 
  if (e.key === 'Escape' && modal.classList.contains('open')) { 
    modal.classList.remove('open'); 
    lenis.start(); 
  } 
});
