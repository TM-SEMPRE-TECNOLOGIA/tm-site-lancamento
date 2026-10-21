from PIL import Image
import numpy as np

# Load generated image
img = Image.open('thiago_cyber_chakra.jpg').convert('RGBA')
data = np.array(img)

# Pure black background keying with soft edge
r, g, b, a = data[:,:,0], data[:,:,1], data[:,:,2], data[:,:,3]

# Pixels very close to black
black_mask = (r < 18) & (g < 18) & (b < 18)

# Create soft alpha
alpha = np.ones(r.shape, dtype=np.uint8) * 255
alpha[black_mask] = 0

# Smooth edges slightly
data[:,:,3] = alpha
result = Image.fromarray(data)
result.save('thiago_cyber_chakra_transparent.png', 'PNG')
print('Transparent PNG saved successfully!')
