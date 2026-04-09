
"""
233405040- Ceren ÇEKEN
Filtre Karşılaştırma ve Kenar Algılama Raporu
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

# 1. ADIM: Görüntü Edinme ve Yapay Gürültü Ekleme
img = cv2.imread('indir.jpeg', 0)
noisy = img.copy()
prob = 0.05  # %5 Tuz-Biber gürültüsü
noisy[np.random.random(img.shape) < prob] = 255
noisy[np.random.random(img.shape) < prob] = 0

# 2. ADIM: 4 Farklı Filtrenin Uygulanması
kutu   = cv2.blur(noisy, (5, 5))
gauss  = cv2.GaussianBlur(noisy, (5, 5), 0)
medyan = cv2.medianBlur(noisy, 5)
bilat  = cv2.bilateralFilter(noisy, 9, 75, 75)

# 3. ADIM: Kenar Algılama (Sobel vs Laplacian)
laplacian = cv2.Laplacian(img, cv2.CV_64F)
laplacian = np.uint8(np.absolute(laplacian))

sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
sobel_combined = cv2.magnitude(sobelx, sobely)
sobel_combined = np.uint8(sobel_combined)

# 4. ADIM: Görselleştirme
titles = ['Gürültülü', 'Medyan Filtre', 'Bilateral', 'Laplacian', 'Sobel']
images = [noisy, medyan, bilat, laplacian, sobel_combined]

plt.figure(figsize=(20, 10))
for i in range(5):
    plt.subplot(1, 5, i+1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.axis('off')
plt.show()