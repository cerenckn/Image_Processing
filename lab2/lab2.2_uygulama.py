# -*- coding: utf-8 -*-
"""
🌟 KONU: Sıfırdan Görüntü Oluşturma ve Bölgesel Boyama
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

# 1. ADIM: SİYAH BİR TUVAL OLUŞTURMA
# 300x300 boyutunda, içi 0 (Siyah) dolu bir matris.
# dtype=np.uint8: Sayıların 0-255 arasında olacağını belirtir (Görüntü standardı).
img = np.zeros((300, 300), dtype=np.uint8)

# 2. ADIM: ORTAYA BEYAZ KARE ÇİZME (Slicing)
# Y ekseninde 100'den 200'e, X ekseninde 100'den 200'e olan bölgeyi seç.
# Bu bölgedeki 0 değerlerini 255 (Beyaz) yaparak "boya".
img[100:200, 100:200] = 255

# ---------------------------------------------------------
# 3. GÖRSELLEŞTİRME (İki Farklı Yöntem)
# ---------------------------------------------------------

# Yöntem A: OpenCV Penceresi (Canlı pencere)
cv2.imshow('Siyah Tuval Üzerine Beyaz Kare', img)
cv2.waitKey(0) # Bir tuşa basana kadar bekle
cv2.destroyAllWindows()

# Yöntem B: Matplotlib (Ders notu için daha şık)
plt.imshow(img, cmap='gray') # Gri tonlamalı göster
plt.title('Sıfırdan Oluşturulan Matris')
plt.axis('off') # Kenar sayılarını gizle
plt.show()

print("✅ Başarıyla siyah tuval üzerine beyaz kare çizildi!")