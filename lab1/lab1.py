# -*- coding: utf-8 -*-
"""
KONU: Görüntü İşlemeye Giriş (OpenCV Temelleri)
"""
import cv2              # Görüntü işleme kütüphanesi (Temel araç setimiz)
import numpy as np       # Matris işlemleri (Resimler aslında birer matristir: Sayı dizileri)
from matplotlib import pyplot as plt  # Görselleştirme (Resmi grafik olarak basar)

# ---------------------------------------------------------
# 1. GÖRÜNTÜ OKUMA (Image Input)
# ---------------------------------------------------------
# OpenCV varsayılan olarak BGR (Blue, Green, Red) formatında okur.
# Formül: Her piksel [B, G, R] şeklinde 3 kanallı bir listedir.
# ÖNEMLİ: Dosya adının ve uzantısının (.jpg / .jpeg) klasördekiyle aynı olduğundan emin ol!
img = cv2.imread('kaliteli.jpg') 

# Gri tonlamaya dönüştürerek okuma (Luminance - Parlaklık odaklı)
# Formül (Basitleştirilmiş): Gri = 0.299*R + 0.587*G + 0.114*B
# Gri resimler tek kanallıdır (0=Siyah, 255=Beyaz).
gray = cv2.imread('kaliteli.jpg', cv2.IMREAD_GRAYSCALE)

# Hata Kontrolü: Eğer dosya bulunamazsa img 'None' olur ve program çöker.
if img is None:
    print("HATA: Resim dosyası bulunamadı! Lütfen dosya adını kontrol edin.")
else:
    # ---------------------------------------------------------
    # 2. GÖRÜNTÜ METRİKLERİ (Image Properties)
    # ---------------------------------------------------------
    # .shape -> (Yükseklik, Genişlik, Kanal Sayısı) döndürür.
    # .size  -> Yükseklik * Genişlik * Kanal (Toplam hücre/sayı miktarı)
    # .dtype -> Veri tipi. Genelde uint8'dir (8-bit unsigned integer: 0-255 arası).
    print(f"Resim Boyutu (Y, G, K): {img.shape}")
    print(f"Veri Tipi: {img.dtype}")
    print(f"Toplam Sayısal Hücre (Pixel x Kanal): {img.size}")

    # ---------------------------------------------------------
    # 3. RENK UZAYI DÖNÜŞÜMÜ (Color Space Conversion)
    # ---------------------------------------------------------
    # OpenCV: BGR (Mavi-Yeşil-Kırmızı) kullanır.
    # Matplotlib: RGB (Kırmızı-Yeşil-Mavi) bekler.
    # Bu yüzden görüntülemeden önce dönüşüm şarttır, yoksa renkler hatalı görünür.
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # ---------------------------------------------------------
    # 4. GÖRÜNTÜLEME - YÖNTEM 1 (Matplotlib)
    # ---------------------------------------------------------
    plt.imshow(img_rgb)
    plt.title('Matplotlib ile RGB Gösterimi')
    plt.axis('off') # Kenardaki koordinat çizgilerini kapatır
    plt.show()

    # ---------------------------------------------------------
    # 5. GÖRÜNTÜLEME - YÖNTEM 2 (OpenCV Penceresi)
    # ---------------------------------------------------------
    # Etkileşimli (interaktif) pencereler açmak için kullanılır.
    cv2.imshow('OpenCV Standart Pencere', img)
    cv2.waitKey(0) # Klavyeden bir tuşa basana kadar pencereyi açık tutar
    cv2.destroyAllWindows() # Belleği temizlemek için tüm pencereleri kapatır

    # Boyutlandırılabilir Pencere Örneği
    cv2.namedWindow('Boyutlanabilir Resim', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Boyutlanabilir Resim', 800, 600)
    cv2.imshow('Boyutlanabilir Resim', img)
    cv2.waitKey(2000) # 2000 milisaniye (2 saniye) bekle ve sonra devam et
    cv2.destroyAllWindows()

    # ---------------------------------------------------------
    # 6. KAYDETME VE SIKIŞTIRMA (Image Output)
    # ---------------------------------------------------------
    # Farklı formatların farklı sıkıştırma algoritmaları vardır.
    cv2.imwrite('cikti_standart.jpg', img) # Standart kayıt

    # JPEG Kalite Ayarı: [0 (en kötü) - 100 (en iyi)] arası değer alır.
    # Sayı arttıkça dosya boyutu artar ama görüntü netleşir.
    cv2.imwrite('cikti_yuksek_kalite.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 95])

    # PNG Sıkıştırma: [0 (sıkıştırma yok) - 9 (maksimum sıkıştırma)] arası.
    # PNG kayıpsız bir formattır; bu ayar sadece dosya boyutunu ve işlem süresini etkiler.
    cv2.imwrite('cikti_sikistirilmis.png', img, [cv2.IMWRITE_PNG_COMPRESSION, 9])

    print("İşlem başarıyla tamamlandı, dosyalar kaydedildi.")