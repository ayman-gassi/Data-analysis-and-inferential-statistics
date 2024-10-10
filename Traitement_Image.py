import numpy as np
import matplotlib.pyplot as plt

largeur, hauteur = 100, 100
image = np.zeros((hauteur, largeur), dtype=np.uint8)

# Ligne H (Horizontal line)
image[50, :] = 255
# Ligne V (Vertical line)
image[:, 50] = 255
# Ligne M (Diagonal line)
for i in range(100):
    image[i, i] = 255

# Carré (Square)
for i in range(40, 60):
    image[40, i] = 255
    image[60, i] = 255
    image[i, 40] = 255
    image[i, 60] = 255

# Cercle (Circle outline)
centre = 50
rayon = 20
image_circle = np.zeros((hauteur, largeur), dtype=np.uint8)
for i in range(hauteur):
    for j in range(largeur):
        if ((i - centre)**2 + (j - centre)**2) == rayon**2:
            image_circle[i, j] = 255

# Cercle V2 (Filled Circle)
image_filled_circle = np.zeros((hauteur, largeur), dtype=np.uint8)
for i in range(hauteur):
    for j in range(largeur):
        if ((i - centre)**2 + (j - centre)**2) < rayon**2:
            image_filled_circle[i, j] = 255

# Palestine Flag (Black & White)
image_bw = np.ones((hauteur, largeur), dtype=np.uint8) * 255
image_bw[0, :] = 0
image_bw[33, :] = 0
image_bw[66, :] = 0
for i in range(50):
    image_bw[i, i] = 0
for i in range(50):
    image_bw[99 - i, i] = 0

# Palestine Flag (Colors)
image_color = np.ones((hauteur, largeur, 3), dtype=np.uint8) * 255
image_color[0:33, :] = [0, 0, 0]
image_color[33:66, :] = [255, 255, 255]
image_color[66:100, :] = [0, 128, 0]
for i in range(50):
    for j in range(i + 1):
        image_color[i, j] = [255, 0, 0]  

for i in range(50):
    image_color[50:99 - i, i] = [255, 0, 0]     


plt.figure(figsize=(15, 10))

plt.subplot(2, 3, 1)
plt.imshow(image, cmap='gray', vmin=0, vmax=255)
plt.title('Lines and Square')

plt.subplot(2, 3, 2)
plt.imshow(image_circle, cmap='gray', vmin=0, vmax=255)
plt.title('Circle Outline')

plt.subplot(2, 3, 3)
plt.imshow(image_filled_circle, cmap='gray', vmin=0, vmax=255)
plt.title('Filled Circle')

plt.subplot(2, 3, 4)
plt.imshow(image_bw, cmap='gray', vmin=0, vmax=255)
plt.title('Black & White Palestine Flag')

plt.subplot(2, 3, 5)
plt.imshow(image_color)
plt.title('Colored Palestine Flag')

plt.tight_layout()
plt.show()
