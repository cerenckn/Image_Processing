# -*- coding: utf-8 -*-
"""
🌟 KONU: Pikseller, ROI (Bölgesel İşlem) ve Renk Kanalları
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

# 1. RESMİ SAHNEYE ALALIM (Okuma ve Kontrol)
img = cv2.imread('kaliteli.jpg')

if img is None:
    print("❌ HATA: Resim yüklenemedi! Dosya adını kontrol et.")
else:
    # ---------------------------------------------------------
    # 2. PİKSEL ERİŞİMİ (Nokta Atışı)
    # ---------------------------------------------------------
    # Bir koordinattaki renk değerini öğrenmek: img[y, x]
    y, x = 100, 200
    bgr_degeri = img[y, x] 
    print(f"📍 ({x},{y}) koordinatındaki BGR değerleri: {bgr_degeri}")

    # Sadece Kırmızı (Red) kanalına erişim (B=0, G=1, R=2)
    kirmizi = img[y, x, 2]
    
    # Pikseli Değiştirme (O noktayı bembeyaz yapalım)
    img[y, x] = [255, 255, 255]

    # ---------------------------------------------------------
    # 3. ROI (Region of Interest) - İLGİ BÖLGESİ (Kes-Yapıştır)
    # ---------------------------------------------------------
    # Resmin bir bölgesini seçmek için: img[y1:y2, x1:x2]
    # Önemli: Kestiğin parçanın boyutu ile yapıştıracağın yerin boyutu AYNI olmalı!
    
    # 50 piksel yükseklik (100'den 150'ye), 100 piksel genişlik (200'den 300'e)
    roi_parca = img[100:150, 200:300] 

    # Şimdi bu 50x100'lük parçayı sol üst köşeye (0,0 noktasına) yapıştıralım
    img[0:50, 0:100] = roi_parca 

    # ---------------------------------------------------------
    # 4. KANAL YÖNETİMİ (Kanal Ayırma ve Birleştirme)
    # ---------------------------------------------------------
    # Resmi renklerine ayırmak: Her renk kanalı gri bir resim gibi görünür.
    mavi, yesil, kirmizi_kanali = cv2.split(img)
    
    # Tekrar birleştirmek (Sıralama B-G-R olmalı)
    birlesik_resim = cv2.merge([mavi, yesil, kirmizi_kanali])

    # ---------------------------------------------------------
    # 5. GÖRSEL ANALİZ PANELİ (Matplotlib ile Show)
    # ---------------------------------------------------------
    # Matplotlib RGB beklediği için dönüşüm yapıyoruz
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    gri_resim = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    plt.figure(figsize=(15, 5))

    # 1. Panel: İşlenmiş Görüntü
    plt.subplot(1, 3, 1)
    plt.imshow(img_rgb)
    plt.title('1. ROI ve Piksel Değişimi')
    plt.axis('off')

    # 2. Panel: Gri Tonlama
    plt.subplot(1, 3, 2)
    plt.imshow(gri_resim, cmap='gray')
    plt.title('2. Gri Tonlama (Tek Kanal)')
    plt.axis('off')

    # 3. Panel: Histogram (Renk Rönteni)
    # Resmin içinde hangi tondan kaç tane var? (Sayısal dağılım)
    plt.subplot(1, 3, 3)
    plt.hist(gri_resim.ravel(), 256, [0, 256], color='purple')
    plt.title('3. Renk Dağılımı (Histogram)')

    plt.tight_layout()
    plt.show()