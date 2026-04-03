# -*- coding: utf-8 -*-
"""
🌟 KONU: Puslu Görüntü Restorasyonu ve CLAHE Analizi
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

# 1. ADIM: RESMİ GRİ TONLAMALI OLARAK TANITIN
# Not: Klasöründe 'puslu.jpg' adında bir dosya olduğunu varsayıyorum.
img = cv2.imread('sisli_gece.jpg', 0) 

if img is None:
    print("❌ HATA: Puslu resim dosyası bulunamadı!")
else:
# 2. ADIM: CLAHE ALGORİTMASINI UYGULAYIN
# İstendiği gibi clipLimit=40.0 (Oldukça yüksek bir değer)
# tileGridSize=(8, 8) resmi 64 küçük parçaya bölüp ayrı ayrı iyileştirir.
    clahe = cv2.createCLAHE(clipLimit=10.0, tileGridSize=(8, 8))
    final_img = clahe.apply(img)

# 3. ADIM: GÖRSELLEŞTİRME VE HİSTOGRAM ANALİZİ
plt.figure(figsize=(15, 10))

# --- Orijinal Puslu Görüntü ---
plt.subplot(2, 2, 1)
plt.imshow(img, cmap='gray')
plt.title('1. Orijinal Puslu Görüntü')
plt.axis('off')

# --- Orijinal Histogram ---
plt.subplot(2, 2, 2)
plt.hist(img.ravel(), 256, [0, 256], color='gray')
plt.title('2. Orijinal Histogram (Sıkışıklık)')

# --- CLAHE Sonucu ---
plt.subplot(2, 2, 3)
plt.imshow(final_img, cmap='gray')
plt.title('3. CLAHE Sonucu (clipLimit=10.0)')
plt.axis('off')

# --- CLAHE Histogramı ---
plt.subplot(2, 2, 4)
plt.hist(final_img.ravel(), 256, [0, 256], color='blue')
plt.title('4. Yeni Histogram (Kontrast Kazanan Pikseller)')

plt.tight_layout()
plt.show()

# =============================================================================
# 🔬 DENEYSEL ANALİZ: CLAHE clipLimit Parametresi ve Histogram Etkisi
# =============================================================================
# clipLimit değerleri (10, 40, 100) denendiğinde gözlemlenen sonuçlar:
#
# 1. GÖRSEL ETKİ (Noise Patlaması):
#    - Limit arttıkça (özellikle 40 ve 100'de), görüntüdeki kontrast aşırı sertleşti.
#    - Puslu bölgelerdeki "karıncalanmalar" (noise), algoritma tarafından "detay" 
#      sanılarak devasa oranda yükseltildi (Doğrusal olmayan artış).
#
# 2. HİSTOGRAMDAKİ "UÇLARDA YÜKSELME" MANTIĞI:
#    - clipLimit düşük olduğunda (örn: 2-10 arası), baskın renk tepeleri "tıraşlanır".
#    - Bu tıraşlanan (kesilen) piksel miktarı, 0 (Siyah) ve 255 (Beyaz) uçları dahil 
#      tüm histograma EŞİT olarak dağıtılır. 
#    - Gözlemlediğim uçlardaki yükselme, aslında bu dağıtılan piksellerin 0 ve 255 
#      noktalarında birikerek görüntünün kontrastını tüm aralığa yaymaya çalışmasıdır.
#
# 3. NEDEN DOĞRUSAL OLMAYAN ARTIŞ?
#    - Pikseller dar bir aralıkta (örneğin 120-130 arası) sıkıştığında, bu aralığı 
#      birbirinden uzaklaştırmak için uygulanan matematiksel katsayı, limit 
#      arttıkça üstel bir etki yaratır. Bu da gürültünün kontrolsüz büyümesine sebep olur.
#
# SONUÇ: En doğal ve temiz görüntü genellikle 2.0 - 5.0 arasındaki limitlerde alınır.
# 40 ve 100 değerleri, algoritmanın "sınırlama" özelliğini devre dışı bırakarak 
# standart histogram eşitlemeye (HE) yaklaşmasına neden olur.
# =============================================================================