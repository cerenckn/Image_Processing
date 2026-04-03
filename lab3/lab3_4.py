# -*- coding: utf-8 -*-
"""
🌟 KONU: Geometrik Dönüşümler (Ölçekleme, Öteleme, Döndürme, Perspektif)
"""
import cv2
import numpy as np

# 1. HAZIRLIK: Resmi oku ve boyutlarını al
img = cv2.imread('resim2.jpg')

if img is None:
    print("❌ Resim bulunamadı! Lütfen dosya adını kontrol et.")
else:
    rows, cols = img.shape[:2]

    # --- [ ADIM A: YENİDEN BOYUTLANDIRMA (RESIZE) ] ---
    # Interpolation: Yeni piksellerin nasıl 'uydurulacağını' belirler.
    buyuk = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)
    kucuk = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

    # --- [ ADIM B: ÖTELEME (TRANSLATION) ] ---
    # Sağa 100, Aşağı 50 piksel kaydırıyoruz.
    # Matris Formülü: [[1, 0, tx], [0, 1, ty]]
    M_otelleme = np.float32([[1, 0, 100], [0, 1, 50]])
    otelenmis = cv2.warpAffine(img, M_otelleme, (cols, rows))

    # --- [ ADIM C: DÖNDÜRME (ROTATION) ] ---
    # Merkeze göre, 45 derece, 1.0 (aynı boyut) ölçeğiyle döndür.
    M_dondurme = cv2.getRotationMatrix2D((cols/2, rows/2), 45, 1.0)
    dondurulmus = cv2.warpAffine(img, M_dondurme, (cols, rows))

    # --- [ ADIM D: EĞME (SHEAR) ] ---
    # Yatayda 0.3 oranında yamultma (Paralelkenar yapma)
    M_shear_x = np.float32([[1, 0.3, 0], [0, 1, 0]])
    egilmis_x = cv2.warpAffine(img, M_shear_x, (cols + 100, rows))

    # --- [ ADIM E: PERSPEKTİF DÜZELTME (SCANNER MODU) ] ---
    # pts1: Kaynak resimdeki 4 yamuk köşe (Örnek koordinatlar)
    # pts2: Bu köşelerin yeni resimde gitmesini istediğimiz yer (Dümdüz bir kare)
    pts1 = np.float32([[56,65], [368,52], [28,387], [389,390]])
    pts2 = np.float32([[0,0], [300,0], [0,300], [300,300]])
    
    M_persp = cv2.getPerspectiveTransform(pts1, pts2)
    tarayici_modu = cv2.warpPerspective(img, M_persp, (300, 300))

    # ---------------------------------------------------------
    # GÖRSELLEŞTİRME
    # ---------------------------------------------------------
    cv2.imshow('1. Otelenmis (Kaydirilmis)', otelenmis)
    cv2.imshow('2. Dondurulmus (45 Derece)', dondurulmus)
    cv2.imshow('3. Egilmis (Shear X)', egilmis_x)
    cv2.imshow('4. Tarayici (Perspektif)', tarayici_modu)

    print("✅ Tüm geometrik dönüşümler uygulandı!")
    cv2.waitKey(0)
    cv2.destroyAllWindows()