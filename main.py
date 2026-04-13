import json
import numpy as np

try:
    with open("ogrenciler.json", "r") as file:
        ogrenciler = json.load(file)
except FileNotFoundError:
    ogrenciler = {}

def kaydet():
    with open("ogrenciler.json", "w") as file:
        json.dump(ogrenciler, file, indent=4)

while True:
    print("\n===== Öğrenci Performans Sistemi =====")
    print("1) Öğrenci Ekle")
    print("2) Not Ekle")
    print("3) Öğrencileri Listele")
    print("4) Detaylı Analiz")
    print("5) En Başarılı Öğrenci")
    print("6) Çıkış")
    print("7) Öğrenci Sil")

    secim = input("Seçiminizi girin: ")

    if secim == "1":
        isim = input("Öğrenci adı girin: ")

        if isim in ogrenciler:
            print("Bu isimde bir öğrenci zaten kayıtlı.")
        else:
            ogrenciler[isim] = []
            kaydet()
            print(f"{isim} başarıyla eklendi.")

    elif secim == "2":
        isim = input("Not eklenecek öğrencinin adını girin: ")

        if isim in ogrenciler:
            try:
                not_degeri = int(input("Not girin (0-100): "))

                if 0 <= not_degeri <= 100:
                    ogrenciler[isim].append(not_degeri)
                    kaydet()
                    print(f"{isim} için not başarıyla eklendi.")
                else:
                    print("Not 0 ile 100 arasında olmalıdır.")

            except:
                print("Geçersiz giriş! Lütfen sayısal bir değer girin.")
        else:
            print("Girilen isimde bir öğrenci bulunamadı.")

    elif secim == "3":
        if len(ogrenciler) == 0:
            print("Henüz kayıtlı öğrenci bulunmamaktadır.")
        else:
            print("\n--- Öğrenci Listesi ---")
            for isim, notlar in ogrenciler.items():
                print(f"{isim} -> Notlar: {notlar}")

    elif secim == "4":
        if len(ogrenciler) == 0:
            print("Henüz analiz yapılacak öğrenci bulunmamaktadır.")
        else:
            print("\n--- Detaylı Analiz ---")

            tum_notlar = []

            for isim, notlar in ogrenciler.items():
                if len(notlar) == 0:
                    print(f"{isim} -> Henüz not girilmemiş.")
                else:
                    ortalama = np.mean(notlar)
                    en_yuksek = np.max(notlar)
                    en_dusuk = np.min(notlar)
                    std = np.std(notlar)

                    if ortalama >= 50:
                        durum = "Geçti"
                    else:
                        durum = "Kaldı"

                    print(f"{isim} -> Ortalama: {round(ortalama,2)} | Max: {en_yuksek} | Min: {en_dusuk} | Std: {round(std,2)} | Durum: {durum}")

                    tum_notlar.extend(notlar)

            if len(tum_notlar) > 0:
                genel_ortalama = np.mean(tum_notlar)
                print(f"\nSınıf Ortalaması: {round(genel_ortalama,2)}")

    elif secim == "5":
        if len(ogrenciler) == 0:
            print("Henüz değerlendirme yapılacak veri bulunmamaktadır.")
        else:
            en_iyi = ""
            en_yuksek = 0

            for isim, notlar in ogrenciler.items():
                if len(notlar) > 0:
                    ortalama = np.mean(notlar)

                    if ortalama > en_yuksek:
                        en_yuksek = ortalama
                        en_iyi = isim

            if en_iyi == "":
                print("Hiçbir öğrenci için not girilmemiş.")
            else:
                print("\n--- En Başarılı Öğrenci ---")
                print(f"Öğrenci: {en_iyi}")
                print(f"Ortalama: {round(en_yuksek,2)}")

    elif secim == "6":
        print("Program sonlandırıldı.")
        break

    elif secim == "7":
        isim = input("Silinecek öğrencinin adını girin: ")

        if isim in ogrenciler:
            del ogrenciler[isim]
            kaydet()
            print(f"{isim} silindi.")
        else:
            print("Böyle bir öğrenci bulunamadı.")

    else:
        print("Geçersiz seçim yaptınız. Lütfen tekrar deneyin.")