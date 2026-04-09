# -*- coding: utf-8 -*-
"""
🌟 KONU: Manuel Gürültü (Salt & Pepper) Oluşturma ve Filtre Karşılaştırması
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

# 1. ADIM: RESMİ OKU VE MANUEL GÜRÜLTÜ EKLE
img = cv2.imread('ornekk.jpeg', 0)
noisy = img.copy()
prob = 0.02 # Gürültü yoğunluğu (%2)

# Tuz (Beyaz noktalar) ekleme
noisy[np.random.random(img.shape) < prob] = 255
# Biber (Siyah noktalar) ekleme
noisy[np.random.random(img.shape) < prob] = 0

# 2. ADIM: FİLTRELEME TEKNİKLERİ
# Kutu Filtre: Pikselleri komşularıyla harmanlar (Gürültüyü bulandırır ama yok etmez).
kutu = cv2.blur(noisy, (5, 5))

# Gauss Filtre: Merkeze ağırlık vererek yumuşatır (Doğal bulanıklık sağlar).
gauss = cv2.GaussianBlur(noisy, (5, 5), 0)

# Medyan Filtre: Komşular arasındaki ortanca değeri seçer. 
# ÖNEMLİ: Tuz-biber gürültüsü için en etkili yöntemdir, gürültüyü tamamen siler!
medyan = cv2.medianBlur(noisy, 5)

# Bilateral Filtre: Kenarları koruyarak yüzeydeki gürültüyü temizlemeye çalışır.
bilat = cv2.bilateralFilter(noisy, 9, 75, 75)

# 3. ADIM: GÖRSELLEŞTİRME (MATPLOTLIB)
titles = ['Gürültülü (Salt&Pepper)', 'Kutu (Mean)', 'Gauss Blur', 'Medyan (Best!)', 'Bilateral']
images = [noisy, kutu, gauss, medyan, bilat]

fig, axes = plt.subplots(1, 5, figsize=(20, 4))

for ax, im, t in zip(axes, images, titles):
    ax.imshow(im, cmap='gray')
    ax.set_title(t, fontsize=10)
    ax.axis('off')

plt.tight_layout()
plt.show()

print("✅ Filtre karşılaştırması başarıyla tamamlandı!")