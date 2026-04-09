# -*- coding: utf-8 -*-
"""
🌟 KONU: Görüntü Yumuşatma ve Filtreleme Teknikleri
"""
import cv2
import numpy as np

img = cv2.imread('ornekk.jpeg')

if img is not None:
    # 1. ORTALAMA (BOX) FİLTRE: Her pikseli 5x5'lik komşularının ortalamasıyla değiştirir.
    kutu = cv2.blur(img, (5, 5))

    # 2. GAUSS FİLTRE: Merkeze yakın piksellere daha fazla ağırlık verir. 
    # Doğal bir yumuşatma sağlar.
    gauss = cv2.GaussianBlur(img, (5, 5), 0)

    # 3. MEDYAN FİLTRE: Komşular arasındaki ortanca değeri seçer. 
    # 'Tuz-biber' (siyah-beyaz noktalar) gürültüsünü silmede bir numaradır!
    medyan = cv2.medianBlur(img, 5) # ksize mutlaka TEK sayı olmalı.

    # 4. BİLATERAL FİLTRE: Hem gürültüyü siler hem de kenarları korur. 
    # Piksellerin sadece renkleri yakınsa birbirini etkiler. (Modern portre modu gibi)
    bilateral = cv2.bilateralFilter(img, 9, 75, 75)

    # 5. ÖZEL KERNEL (Filter2D): Kendi filtre matrisimizi uyguluyoruz.
    kernel = np.ones((5, 5), np.float32) / 25
    ozel = cv2.filter2D(img, -1, kernel)

    # --- [ KENAR ALGILAMA VE KESKİNLERŞTİRME ] ---

    # 1. LAPLACIAN: Görüntünün ikinci türeini alarak tüm kenarları belirler.
    laplacian = cv2.Laplacian(img, cv2.CV_64F)
    laplacian = np.uint8(np.absolute(laplacian))

    # 2. SOBEL: Yatay (X) ve Dikey (Y) geçişleri bularak yönlü kenarları tespit eder.
    sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
    sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
    sobel_mag = cv2.magnitude(sobelx, sobely) # İkisini birleştirip şiddeti bulur.

    # 3. UNSHARP MASKING: Resmi bulandırıp orijinalinden çıkararak detayları parlatır.
    bulanik = cv2.GaussianBlur(img, (9, 9), 10.0)
    keskin = cv2.addWeighted(img, 1.5, bulanik, -0.5, 0)

    # 4. KESKİNLERŞTİRME KERNELİ: Özel matris ile pikselleri vurgulama.
    kernel_sharp = np.array([[ 0, -1,  0],
                             [-1,  5, -1],
                             [ 0, -1,  0]])
    keskin2 = cv2.filter2D(img, -1, kernel_sharp)

    cv2.imshow('Keskinlestirilmiş Görüntü', keskin2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
