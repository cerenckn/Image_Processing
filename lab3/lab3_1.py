# -*- coding: utf-8 -*-
"""
🌟 KONU: Görüntü Aritmetiği ve Hareket Algılama Mantığı
"""

import cv2
import numpy as np

# --- BÖLÜM 1: RESİM KARIŞTIRMA (BLENDING) ---
# Önemli: İki resmin boyutları (Yükseklik x Genişlik) AYNI olmalıdır!
img1 = cv2.imread('resim1.jpg')
img2 = cv2.imread('resim2.jpg')

if img1 is not None and img2 is not None:
    # 1. Doygunluklu Toplama (Saturated Addition)
    # Formül: Sonuç = resim1 + resim2 (Max 255)
    toplam = cv2.add(img1, img2)

    # 2. Ağırlıklı Toplama (Blending - Şeffaflık Etkisi)
    # Formül: Sonuç = (img1 * alpha) + (img2 * beta) + gamma
    # Burada img1 %70, img2 %30 baskın.
    karisim = cv2.addWeighted(img1, 0.7, img2, 0.3, 0)
    
    cv2.imshow("Karisim (Blending)", karisim)

# --- BÖLÜM 2: FARK BULMA VE HAREKET ALGILAMA ---
# Zaman 1 ve Zaman 2'deki iki kareyi (frame) gri modda okuyoruz.
onceki_kare = cv2.imread('zaman1.png', 0)
sonraki_kare = cv2.imread('zaman2.png', 0)

if onceki_kare is not None and sonraki_kare is not None:
    # 3. Mutlak Fark (Absolute Difference)
    # Neden cv2.subtract değil? Çünkü çıkarma işlemi negatifleri 0 yapar.
    # Absdiff ise |fark| alır; yani hangi karenin daha parlak olduğu önemli değildir.
    mutlak_fark = cv2.absdiff(sonraki_kare, onceki_kare)

    # 4. Eşikleme (Thresholding) - Hareket Maskesi Oluşturma
    # Mantık: Eğer iki kare arasındaki fark 30'dan büyükse orası "hareketli" demektir.
    # 30'un üzerindeki farkları 255 (BEYAZ), altındakileri 0 (SİYAH) yap.
    _, hareket_maskesi = cv2.threshold(mutlak_fark, 30, 255, cv2.THRESH_BINARY)

    # Sonuçları göster
    cv2.imshow("Degisim (Fark)", mutlak_fark)
    cv2.imshow("Hareket Algilandi (Maske)", hareket_maskesi)

cv2.waitKey(0)
cv2.destroyAllWindows()