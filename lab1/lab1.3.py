# -*- coding: utf-8 -*-
"""
🌟 KONU: Canlı Video Akışı ve Kamera Yönetimi
"""

import cv2

# 1. KAMERAYI BAŞLATALIM
# 0 = Bilgisayarın kendi kamerası. 1 = Harici takılan USB kamera.
cap = cv2.VideoCapture(0) 

# Video bir döngüdür, her seferinde yeni bir 'kare' (frame) yakalarız.
while True:
    # ret: İşlem başarılı mı? (True/False)
    # frame: Yakalanan o anki resim matrisi.
    ret, frame = cap.read() 

    # Eğer kamera bir sebeple görüntü veremezse döngüden çık
    if not ret:
        print("❌ Kameradan görüntü alınamıyor!")
        break

    # ---------------------------------------------------------
    # 2. CANLI İŞLEME (Filtreleme)
    # ---------------------------------------------------------
    # Her bir kareyi canlı olarak gri tonlamaya çeviriyoruz
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # ---------------------------------------------------------
    # 3. GÖRSELLEŞTİRME (Pencereler)
    # ---------------------------------------------------------
    # Orijinal renkli görüntüyü göster
    cv2.imshow('Canli Renkli Yayin', frame)
    
    # Griye çevrilmiş halini ayrı bir pencerede göster
    cv2.imshow('Canli Gri Filtre', gray)

    # ---------------------------------------------------------
    # 4. ÇIKIŞ KONTROLÜ (Tuş Takibi)
    # ---------------------------------------------------------
    # cv2.waitKey(1): 1 milisaniye boyunca bir tuşa basılmasını bekler.
    # ord('q'): Eğer klavyeden 'q' (quit) tuşuna basılırsa döngüyü kırar.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# ---------------------------------------------------------
# 5. TEMİZLİK (Sistemi Kapatma)
# ---------------------------------------------------------
# Kamerayı serbest bırak (başkası kullanabilsin diye)
cap.release() 

# Açılan tüm OpenCV pencerelerini kapat
cv2.destroyAllWindows()