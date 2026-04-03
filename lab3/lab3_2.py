# -*- coding: utf-8 -*-
import cv2
import numpy as np

# 1. ADIM: RESMİ OKU VE TUVAL HAZIRLA
img = cv2.imread('resim1.jpg')

if img is not None:
    y, x = img.shape[:2] # Resmin yükseklik ve genişliğini al

    # 2. ADIM: MASKE ÜRETME (Siyah Tuval)
    # Resimle aynı boyutta, içi 0 (Siyah) dolu tek kanallı bir matris.
    mask = np.zeros((y, x), dtype=np.uint8)

    # 3. ADIM: MASKE ÜZERİNE BEYAZ DAİRE ÇİZ
    # (x//2, y//2) -> Merkeze çiz, 150 -> Yarıçap, 255 -> Beyaz, -1 -> İçini doldur
    cv2.circle(mask, (x//2, y//2), 150, 255, -1)

    # 4. ADIM: BITWISE AND (Ve İşlemi)
    # Resmin sadece maske üzerindeki beyaz (255) alana denk gelen kısmını tutar.
    # Formül: Görüntü AND Maske = Sadece maskenin olduğu yer görünür.
    sonuc = cv2.bitwise_and(img, img, mask=mask)

    # 5. ADIM: NEGATİF ALMA (Tersleme)
    # Tüm renklerin zıttını alır (255 - piksel_degeri).
    negatif = cv2.bitwise_not(img)

    cv2.imshow('Maskeli Sonuc', sonuc)
    cv2.imshow('Negatif Goruntu', negatif)