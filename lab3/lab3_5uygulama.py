# -*- coding: utf-8 -*-
"""
🌟 KONU: Aritmetik Çıkarma (Gürültü Simülasyonu)
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

# 1. ADIM: İKİ FARKLI RASTGELE MATRİS (NOISE) ÜRETELİM
# 300x300 boyutunda, 0-255 arası rastgele sayılar
noise1 = np.random.randint(0, 256, (300, 300), dtype=np.uint8)
noise2 = np.random.randint(0, 256, (300, 300), dtype=np.uint8)

# 2. ADIM: İKİ GÜRÜLTÜYÜ BİRBİRİNDEN ÇIKARALIM (MUTLAK FARK)
# Formül: fark = |noise1 - noise2|
fark = cv2.absdiff(noise1, noise2)

# ---------------------------------------------------------
# 3. GÖRSELLEŞTİRME
# ---------------------------------------------------------

# OpenCV Penceresi ile Gösterme
cv2.imshow('Gurultu 1', noise1)
cv2.imshow('Gurultu 2', noise2)
cv2.imshow('Cikarim Modeli (Fark)', fark)

# Alternatif: Matplotlib ile yan yana gösterme (Analiz için daha iyi)
plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.imshow(noise1, cmap='gray')
plt.title('Görüntü 1 (Gürültü)')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(noise2, cmap='gray')
plt.title('Görüntü 2 (Gürültü)')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(fark, cmap='gray')
plt.title('Aritmetik Fark')
plt.axis('off')

plt.tight_layout()
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()