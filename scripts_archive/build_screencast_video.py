import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import os

WIDTH = 1280
HEIGHT = 720
NAV_BAR_H = 68
VIEW_H = HEIGHT - NAV_BAR_H
FPS = 30

home_path = r"c:\Users\mikaa\Documents\antigravity\tm-site-lancamento\estrategia-politica-funil\assets\screenshot_home.png"
agenda_path = r"c:\Users\mikaa\Documents\antigravity\tm-site-lancamento\estrategia-politica-funil\assets\screenshot_agenda.png"
doacoes_path = r"c:\Users\mikaa\Documents\antigravity\tm-site-lancamento\estrategia-politica-funil\assets\screenshot_doacoes.png"
output_path = r"c:\Users\mikaa\Documents\antigravity\tm-site-lancamento\estrategia-politica-funil\assets\video-portfolio-adir.mp4"

# Carrega as imagens
img_home = Image.open(home_path).convert("RGB")
img_agenda = Image.open(agenda_path).convert("RGB")
img_doacoes = Image.open(doacoes_path).convert("RGB")

# Redimensiona mantendo a largura do viewport (1280)
def prep_page(img):
    w, h = img.size
    new_h = int(h * (WIDTH / w))
    return img.resize((WIDTH, new_h), Image.Resampling.LANCZOS)

page_home = prep_page(img_home)
page_agenda = prep_page(img_agenda)
page_doacoes = prep_page(img_doacoes)

# Fontes padrão
try:
    font_url = ImageFont.truetype("segoeui.ttf", 14)
    font_tab = ImageFont.truetype("segoeuib.ttf", 12)
    font_badge = ImageFont.truetype("segoeuib.ttf", 11)
except Exception:
    font_url = ImageFont.load_default()
    font_tab = ImageFont.load_default()
    font_badge = ImageFont.load_default()

def draw_browser_frame(url_text="https://adirgentil2211.com.br", active_tab="Adir Gentil 2211 — Deputado Federal (PL)"):
    nav = Image.new("RGB", (WIDTH, NAV_BAR_H), "#1e2430")
    draw = ImageDraw.Draw(nav)
    
    # Aba superior
    tab_w = 290
    draw.rounded_rectangle([(10, 8), (10 + tab_w, 36)], radius=6, fill="#2b3342")
    draw.ellipse([(22, 18), (30, 26)], fill="#004f9f") # ícone azul da aba
    draw.text((38, 15), active_tab[:38] + ("..." if len(active_tab)>38 else ""), fill="#f1f5f9", font=font_tab)
    
    # Botão nova aba '+'
    draw.text((10 + tab_w + 12, 14), "+", fill="#94a3b8", font=font_tab)
    
    # Botões janela (traffic lights mac/clean)
    draw.ellipse([(WIDTH - 65, 16), (WIDTH - 55, 26)], fill="#ff5f56")
    draw.ellipse([(WIDTH - 45, 16), (WIDTH - 35, 26)], fill="#ffbd2e")
    draw.ellipse([(WIDTH - 25, 16), (WIDTH - 15, 26)], fill="#27c93f")
    
    # Barra de ferramentas / URL
    draw.rectangle([(0, 36), (WIDTH, NAV_BAR_H)], fill="#262d3d")
    
    # Setas voltar/avançar/recarregar
    draw.polygon([(20, 52), (28, 46), (28, 58)], fill="#94a3b8") # Back
    draw.polygon([(46, 46), (38, 52), (38, 46)], fill="#64748b") # Forward
    draw.arc([(58, 47), (70, 57)], start=30, end=300, fill="#94a3b8", width=2) # Reload
    
    # Caixa da URL
    url_box = [(85, 41), (WIDTH - 180, 63)]
    draw.rounded_rectangle(url_box, radius=6, fill="#191f2c", outline="#3b4458")
    
    # Cadeado verde de segurança
    draw.rectangle([(98, 49), (106, 56)], fill="#10b981")
    draw.arc([(100, 46), (104, 50)], start=180, end=360, fill="#10b981", width=2)
    
    draw.text((114, 45), url_text, fill="#e2e8f0", font=font_url)
    
    # Selo no canto direito da barra de endereço
    draw.rounded_rectangle([(WIDTH - 165, 43), (WIDTH - 15, 61)], radius=4, fill="#004f9f")
    draw.text((WIDTH - 158, 46), "PORTAL OFICIAL 2211", fill="#ffd500", font=font_badge)
    
    return nav

def draw_cursor(img_draw, x, y, clicking=False):
    # Desenha um cursor elegante de mouse
    pts = [(x, y), (x, y + 18), (x + 4, y + 14), (x + 9, y + 21), (x + 12, y + 19), (x + 7, y + 13), (x + 13, y + 13)]
    fill_col = "#ff6b00" if clicking else "#ffffff"
    img_draw.polygon(pts, fill=fill_col, outline="#000000")
    if clicking:
        img_draw.ellipse([(x - 8, y - 8), (x + 16, y + 16)], outline="#ff6b00", width=2)

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_path, fourcc, FPS, (WIDTH, HEIGHT))

print("Generating screencast video frames...")

# Sequência de cenas da navegação
# Uma cena: (page_img, y_start, y_end, duration_sec, url, tab_name, mouse_pos_start, mouse_pos_end, click_at_end)
scenes = [
    # 1. Home - pausa no Hero
    (page_home, 0, 0, 2.5, "https://adirgentil2211.com.br", "Adir Gentil 2211 — Deputado Federal (PL)", (600, 350), (600, 350), False),
    # 2. Home - scroll suave descendo para 'Quem sou'
    (page_home, 0, 580, 2.2, "https://adirgentil2211.com.br", "Adir Gentil 2211 — Deputado Federal (PL)", (600, 350), (620, 420), False),
    # 3. Home - pausa em 'Quem sou'
    (page_home, 580, 580, 2.0, "https://adirgentil2211.com.br", "Adir Gentil 2211 — Deputado Federal (PL)", (620, 420), (620, 420), False),
    # 4. Home - scroll suave até 'Propostas Prioritárias'
    (page_home, 580, 1250, 2.5, "https://adirgentil2211.com.br", "Adir Gentil 2211 — Deputado Federal (PL)", (620, 420), (550, 380), False),
    # 5. Home - pausa em 'Propostas'
    (page_home, 1250, 1250, 2.0, "https://adirgentil2211.com.br", "Adir Gentil 2211 — Deputado Federal (PL)", (550, 380), (550, 380), False),
    # 6. Home - scroll suave até Jingles e Rodapé
    (page_home, 1250, 1950, 2.2, "https://adirgentil2211.com.br", "Adir Gentil 2211 — Deputado Federal (PL)", (550, 380), (700, 450), False),
    # 7. Home - pausa no rodapé
    (page_home, 1950, 1950, 1.5, "https://adirgentil2211.com.br", "Adir Gentil 2211 — Deputado Federal (PL)", (700, 450), (700, 450), False),
    # 8. Home - scroll de volta para o topo e mouse vai até o menu 'Doações'
    (page_home, 1950, 0, 2.0, "https://adirgentil2211.com.br", "Adir Gentil 2211 — Deputado Federal (PL)", (700, 450), (835, 110), True),
    
    # 9. Abre página de Doações / Crowdfunding TSE
    (page_doacoes, 0, 0, 1.8, "https://adirgentil2211.com.br/doacoes", "Doações Oficiais TSE — Adir Gentil 2211", (835, 110), (750, 300), False),
    # 10. Scroll na página de Doações mostrando valores e PIX
    (page_doacoes, 0, 450, 2.2, "https://adirgentil2211.com.br/doacoes", "Doações Oficiais TSE — Adir Gentil 2211", (750, 300), (640, 400), False),
    # 11. Pausa e mouse clica em 'Agenda'
    (page_doacoes, 450, 0, 1.5, "https://adirgentil2211.com.br/doacoes", "Doações Oficiais TSE — Adir Gentil 2211", (640, 400), (770, 110), True),
    
    # 12. Abre página de Agenda pelos 139 municípios
    (page_agenda, 0, 0, 1.8, "https://adirgentil2211.com.br/agenda", "Agenda & Caravana Tocantins — 2211", (770, 110), (600, 320), False),
    # 13. Scroll na Agenda
    (page_agenda, 0, 500, 2.0, "https://adirgentil2211.com.br/agenda", "Agenda & Caravana Tocantins — 2211", (600, 320), (580, 420), False),
    # 14. Mouse volta para 'Início'
    (page_agenda, 500, 0, 1.5, "https://adirgentil2211.com.br/agenda", "Agenda & Caravana Tocantins — 2211", (580, 420), (520, 110), True),
    
    # 15. Volta para a Home com selo de fechamento
    (page_home, 0, 0, 2.0, "https://adirgentil2211.com.br", "Adir Gentil 2211 — Deputado Federal (PL)", (520, 110), (640, 360), False)
]

def ease_in_out(t):
    return t * t * (3 - 2 * t)

total_frames = 0
for idx, scene in enumerate(scenes):
    page, y1, y2, dur, url, tab, (mx1, my1), (mx2, my2), click_end = scene
    num_frames = int(dur * FPS)
    nav_frame = draw_browser_frame(url, tab)
    max_scroll = max(0, page.size[1] - VIEW_H)
    
    for f in range(num_frames):
        t = f / max(1, num_frames - 1)
        ease_t = ease_in_out(t)
        
        # Posição de scroll da página
        current_y = int(y1 + (y2 - y1) * ease_t)
        current_y = min(max_scroll, max(0, current_y))
        
        # Posição do cursor
        cur_mx = int(mx1 + (mx2 - mx1) * ease_t)
        cur_my = int(my1 + (my2 - my1) * ease_t)
        is_clicking = click_end and (f >= num_frames - 8)
        
        # Monta a imagem final
        frame_img = Image.new("RGB", (WIDTH, HEIGHT))
        frame_img.paste(nav_frame, (0, 0))
        
        # Recorta viewport da página
        crop_view = page.crop((0, current_y, WIDTH, current_y + VIEW_H))
        frame_img.paste(crop_view, (0, NAV_BAR_H))
        
        # Desenha cursor do mouse
        draw_f = ImageDraw.Draw(frame_img)
        draw_cursor(draw_f, cur_mx, cur_my, clicking=is_clicking)
        
        # Converte para OpenCV BGR
        cv_frame = cv2.cvtColor(np.array(frame_img), cv2.COLOR_RGB2BGR)
        out.write(cv_frame)
        total_frames += 1

out.release()
print(f"Video created successfully! Total frames: {total_frames} ({total_frames/FPS:.1f}s) at {output_path}")
