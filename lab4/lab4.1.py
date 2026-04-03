# -*- coding: utf-8 -*-
"""
🌟 KONU: Görüntü İyileştirme (Negatif, Log, Threshold, CLAHE)
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

# 1. HAZIRLIK: Resimleri gri tonlamalı oku (İyileştirme genelde gri kanalda yapılır)
img_karanlik = cv2.imread('sisli_gece.jpg', 0)
img_belge = cv2.imread('indir.jpeg', 0)

if img_karanlik is None or img_belge is None:
    print("❌ Dosyalar bulunamadı! Lütfen isimleri kontrol et.")
else:
    # --- [ ADIM A: NEGATİF VE LOGARİTMİK DÖNÜŞÜM ] ---
    # Negatif: Renkleri ters yüz eder.
    negatif = 255 - img_karanlik

    # Logaritmik: Düşük ışıklı pikselleri parlatır.
    # Formül: s = c * log(1 + r). +1 ekliyoruz çünkü log(0) tanımsızdır!
    c = 255 / np.log(1 + np.max(img_karanlik))
    log_img = c * (np.log(img_karanlik.astype(np.float64) + 1))
    log_img = np.uint8(log_img) # Sayıları tekrar 0-255 tam sayı formatına sok

    # --- [ ADIM B: AKILLI EŞİKLEME (OTSU THRESHOLD) ] ---
    # Belge okumada 'Otsu' yöntemi en ideal eşik değerini kendi bulur.
    _, otsu_sonuc = cv2.threshold(img_belge, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # --- [ ADIM C: KONTRAST GERME (STRETCHING) ] ---
    # Puslu fotolarda pikselleri 0-255 arasına yayarız.
    min_v, max_v = np.min(img_karanlik), np.max(img_karanlik)
    stretched = np.uint8((img_karanlik - min_v) * (255.0 / (max_v - min_v)))

    # --- [ ADIM D: CLAHE (MODERN KONTRAST SİHRİ) ] ---
    # Standart eşitleme yerine 'Lokal' iyileştirme yapar, gürültüyü korur.
    # clipLimit: Kontrastın çok patlamasını engeller.
    clahe_obj = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    clahe_final = clahe_obj.apply(img_karanlik)

    # ---------------------------------------------------------
    # GÖRSELLEŞTİRME
    # ---------------------------------------------------------
    cv2.imshow('1. Negatif Goruntu', negatif)
    cv2.imshow('2. Logaritmik (Karanlik Cozucu)', log_img)
    cv2.imshow('3. Otsu (Akilli Belge Okuma)', otsu_sonuc)
    cv2.imshow('4. CLAHE (Mucize Dokunus)', clahe_final)

    print("✅ Tüm iyileştirme teknikleri başarıyla uygulandı!")
    cv2.waitKey(0)
    cv2.destroyAllWindows()