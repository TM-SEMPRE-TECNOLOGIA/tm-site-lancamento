from PIL import Image, ImageFilter
import numpy as np

# Carrega a imagem original gerada
img = Image.open('c:/Users/mikaa/Documents/antigravity/tm-site-lancamento/thiago_armor_disassembly.jpg').convert('RGB')
w, h = img.size

# Converte para array numpy
arr = np.array(img, dtype=np.float32)
r, g, b = arr[:,:,0], arr[:,:,1], arr[:,:,2]

# Calcula a luminância (perceptual brightness)
lum = 0.299 * r + 0.587 * g + 0.114 * b

# O fundo preto começa em limiares bem baixos
# Transição ultra suave entre limiares 10 e 35
black_floor = 10.0
solid_thresh = 38.0

# Máscara de opacidade inicial com rampa linear suave
alpha = np.clip((lum - black_floor) / (solid_thresh - black_floor), 0.0, 1.0) * 255.0

# Onde houver cor pronunciada (propulsores amarelos ou partículas cyan), garante translucidez luminosa
max_channel = np.maximum(np.maximum(r, g), b)
min_channel = np.minimum(np.minimum(r, g), b)
saturation = np.where(max_channel > 0, (max_channel - min_channel) / (max_channel + 1e-5), 0)
glow_boost = (max_channel / 255.0) * saturation * 255.0
alpha = np.maximum(alpha, glow_boost)

# Previne halos pretos desagradáveis em modo normal multiplicando as cores suavemente (unpremultiply/clean edge)
alpha_uint8 = alpha.astype(np.uint8)

# Cria imagem RGBA
rgba = np.zeros((h, w, 4), dtype=np.uint8)
rgba[:,:,:3] = np.clip(arr, 0, 255).astype(np.uint8)
rgba[:,:,3] = alpha_uint8

result = Image.fromarray(rgba, 'RGBA')

# Salva a versão transparente full
result.save('c:/Users/mikaa/Documents/antigravity/tm-site-lancamento/thiago_armor_disassembly_transparent.png', 'PNG')

# Agora vamos calcular o bounding box vertical para garantir alinhamento idêntico ao chakra anterior
alpha_channel = np.array(result.split()[-1])
non_zero = np.where(alpha_channel > 15)
min_y, max_y = non_zero[0].min(), non_zero[0].max()
min_x, max_x = non_zero[1].min(), non_zero[1].max()

print(f'Bounding Box: X=[{min_x}, {max_x}] (W={max_x - min_x}), Y=[{min_y}, {max_y}] (H={max_y - min_y})')

# Corta ligeiramente o topo vazio (mantendo um respiro harmonioso) e centraliza
crop_top = max(0, min_y - 20)
crop_bottom = min(h, max_y + 30)

cropped = result.crop((0, crop_top, w, crop_bottom))
cropped.save('c:/Users/mikaa/Documents/antigravity/tm-site-lancamento/thiago_armor_cropped_transparent.png', 'PNG')
print('Imagens salvas com sucesso!')
