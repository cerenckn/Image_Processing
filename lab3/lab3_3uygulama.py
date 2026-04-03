# -*- coding: utf-8 -*-
"""
🌟 KONU: Akıllı Hareket Algılama ve Gürültü Filtreleme
"""
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

# İlk kareyi referans (arka plan) alıyoruz
ret, ilk_kare = cap.read()
ilk_gri = cv2.cvtColor(ilk_kare, cv2.COLOR_BGR2GRAY)
ilk_gri = cv2.GaussianBlur(ilk_gri, (21, 21), 0)

while True:
    ret, kare = cap.read()
    if not ret: break

    # Görüntü hazırlama
    guncel_gri = cv2.cvtColor(kare, cv2.COLOR_BGR2GRAY)
    guncel_gri = cv2.GaussianBlur(guncel_gri, (21, 21), 0)

    # Farkı bulma
    fark = cv2.absdiff(ilk_gri, guncel_gri)
    
    # Eşikleme (Hata düzeltilmiş: _ , esik yapısı)
    _, esik = cv2.threshold(fark, 25, 255, cv2.THRESH_BINARY)
    
    # İYİLEŞTİRME: Genişletme (Küçük parçaları birleştirir)
    esik = cv2.dilate(esik, None, iterations=3)

    # Kontur tespiti
    konturlar, _ = cv2.findContours(esik.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for kontur in konturlar:
        # İYİLEŞTİRME: Alan Filtresi (Sadece büyük hareketleri yakala)
        if cv2.contourArea(kontur) < 5000:
            continue

        (x, y, w, h) = cv2.boundingRect(kontur)
        cv2.rectangle(kare, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(kare, "HAREKET!", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    cv2.imshow("Akilli Kamera", kare)
    cv2.imshow("Islemden Gecmis Maske", esik)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

# =============================================================================
# 🧐 NEDEN İYİLEŞTİRME YAPTIK? (DERS NOTLARI)
# =============================================================================
# 1. GAUSSIAN BLUR NEDEN VAR?: 
#    Kamera pikselleri biz dururken bile "titrer" (Noise/Gürültü). 
#    Eğer bulandırma yapmazsak, bilgisayar bu minik karıncalanmaları 
#    'hareket' sanır ve her yerde minik kutular çıkarır.
#
# 2. DILATE (GENİŞLETME) NEDEN VAR?: 
#    Hareket ederken kolun, yüzün ve gövden arasında boşluklar kalabilir. 
#    Dilation, beyaz pikselleri şişirerek bu boşlukları kapatır ve 
#    seni parça parça kutular yerine tek bir büyük kutu içinde gösterir.
#
# 3. CONTOUR AREA > 5000 NEDEN VAR?: 
#    Ekranda uçan bir sinek veya kameranın önündeki bir toz tanesi 
#    güvenlik sistemini tetiklememeli. Bu eşik değeri, "Sadece 
#    belirli bir boyuttan büyük (insan gibi) nesneleri ciddiye al" demektir.
#
# 4. ABSDIFF NEDEN VAR?: 
#    Normal çıkarma (-) işleminde negatif değerler sıfırlanır. 
#    Absolute Difference (Mutlak Fark) ise her türlü değişimi yakalar.
# =============================================================================s