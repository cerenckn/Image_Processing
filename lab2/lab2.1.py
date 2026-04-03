# -*- coding: utf-8 -*-
"""
🌟 KONU: Ölçekleme (Interpolasyon) ve Nicemleme (Quantization)
"""

import cv2
import numpy as np

# 1. OKUMA VE BİLGİ ALMA
# 'ornek.jpeg' yerine kendi dosya adını yazmayı unutma!
img_color = cv2.imread('ornek.jpeg', cv2.IMREAD_COLOR)
img_gray = cv2.imread('ornek.jpeg', cv2.IMREAD_GRAYSCALE)

if img_gray is None:
    print("❌ Hata: Resim bulunamadı!")
else:
    print(f'🎨 Renkli Boyut (Y, G, Kanal): {img_color.shape}') 
    print(f'📂 Gri Boyut (Y, G): {img_gray.shape}')
    print(f'🔢 Veri Tipi: {img_gray.dtype}') # Genelde uint8 (0-255)

    # ---------------------------------------------------------
    # 2. ÖLÇEKLEME (RESIZE) VE INTERPOLASYON
    # ---------------------------------------------------------
    # fx ve fy: Genişlik ve yükseklik çarpanlarıdır. 
    # 0.5 demek resmi yarı yarıya küçültmek demektir.
    for olcek in [1, 0.5, 0.25, 0.125]:
        # INTER_NEAREST: En yakın komşu pikselleri kopyalar. 
        # Keskin ama pikselli bir görüntü oluşturur.
        kucuk = cv2.resize(img_gray, None, fx=olcek, fy=olcek, interpolation=cv2.INTER_NEAREST)
        
        # Küçülen resmi tekrar eski boyutuna (1.0) çekersen 'Piksel Sanatı' (Pixel Art) etkisini görürsün.
        buyuk = cv2.resize(kucuk, None, fx=1/olcek, fy=1/olcek, interpolation=cv2.INTER_NEAREST)
        
        cv2.imshow(f'Olcek Etkisi: {olcek}', buyuk)

    # ---------------------------------------------------------
    # 3. NİCEMLEME / QUANTA (Renk Seviyesi Azaltma)
    # ---------------------------------------------------------
    # Bilgisayar dünyasında renkler bitlerle ifade edilir.
    # 8-bit = 256 renk | 1-bit = 2 renk (Siyah-Beyaz)
    for bit in [6, 4, 2, 1]:
        seviye = 2**bit  # 2'nin kuvveti olarak seviyeyi hesaplarız
        faktor = 256 // seviye
        
        # Matematiksel Sihir: Pikselleri belirli aralıklara hapsederiz.
        # Örneğin faktor 64 ise; 0-63 arası pikseller 0 olur, 64-127 arası 64 olur.
        nicemli = (img_gray // faktor) * faktor
        
        cv2.imshow(f'Renk Seviyesi: {seviye} (Bit: {bit})', nicemli)

    # ---------------------------------------------------------
    # 4. ROI (İlgi Alanı) İŞLEMLERİ
    # ---------------------------------------------------------
    img = cv2.imread('ornek.jpeg')
    # Resimden bir parça koparalım (Y: 50-200, X: 100-300)
    roi = img[50:200, 100:300]
    
    cv2.imshow('Kesilen Parca (ROI)', roi)

    # Kestiğimiz parçayı resmin üzerine geri yapıştıralım (Burada aynı yere yapışıyor)
    img[50:200, 100:300] = roi

    cv2.waitKey(0)
    cv2.destroyAllWindows()