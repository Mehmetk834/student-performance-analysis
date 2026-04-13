import json
import numpy as np
import matplotlib.pyplot as plt

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
    print("8) Grafik Göster")

    secim = input("Seçiminizi girin: ")

    if secim == "1":
        isim = input("Öğrenci adı girin: ")

        if isim in ogrenciler:
            print("Bu isimde bir öğrenci zaten kayıtlı.")
        else:
            ogrenciler[isim] = []
            kaydet()
            print(f"{isim} adlı öğrenci başarıyla eklendi.")

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
                    print("Not değeri 0 ile 100 arasında olmalıdır.")

            except:
                print("Geçersiz giriş. Lütfen sayısal bir değer girin.")
        else:
            print("Girilen isimde bir öğrenci bulunamadı.")

    elif secim == "3":
        if len(ogrenciler) == 0:
            print("Sistemde kayıtlı öğrenci bulunmamaktadır.")
        else:
            print("\n--- Öğrenci Listesi ---")
            for isim, notlar in ogrenciler.items():
                print(f"{isim} -> Notlar: {notlar}")

    elif secim == "4":
        if len(ogrenciler) == 0:
            print("Analiz yapılabilecek veri bulunmamaktadır.")
        else:
            print("\n--- Detaylı Analiz Sonuçları ---")

            tum_notlar = []

            for isim, notlar in ogrenciler.items():
                if len(notlar) == 0:
                    print(f"{isim} -> Henüz not girilmemiş.")
                else:
                    ortalama = np.mean(notlar)
                    en_yuksek = np.max(notlar)
                    en_dusuk = np.min(notlar)
                    std = np.std(notlar)

                    durum = "Geçti" if ortalama >= 50 else "Kaldı"

                    print(f"{isim} -> Ortalama: {round(ortalama,2)} | En Yüksek: {en_yuksek} | En Düşük: {en_dusuk} | Std: {round(std,2)} | Durum: {durum}")

                    tum_notlar.extend(notlar)

            if len(tum_notlar) > 0:
                genel_ortalama = np.mean(tum_notlar)
                print(f"\nSınıf Ortalaması: {round(genel_ortalama,2)}")

    elif secim == "5":
        en_iyi = ""
        en_yuksek = 0

        for isim, notlar in ogrenciler.items():
            if len(notlar) > 0:
                ortalama = np.mean(notlar)

                if ortalama > en_yuksek:
                    en_yuksek = ortalama
                    en_iyi = isim

        if en_iyi == "":
            print("Değerlendirme yapılacak yeterli veri bulunmamaktadır.")
        else:
            print("\n--- En Başarılı Öğrenci ---")
            print(f"Öğrenci: {en_iyi}")
            print(f"Ortalama: {round(en_yuksek,2)}")

    elif secim == "6":
        print("Çıkış yapıldı.")
        break

    elif secim == "7":
        isim = input("Silinecek öğrencinin adını girin: ")

        if isim in ogrenciler:
            del ogrenciler[isim]
            kaydet()
            print(f"{isim} adlı öğrenci sistemden silindi.")
        else:
            print("Belirtilen isimde bir öğrenci bulunamadı.")

    elif secim == "8":
        isimler = []
        ortalamalar = []

        for isim, notlar in ogrenciler.items():
            if len(notlar) > 0:
                isimler.append(isim)
                ortalamalar.append(np.mean(notlar))

        if len(isimler) == 0:
            print("Grafik oluşturmak için yeterli veri yoktur.")
        else:
            plt.figure()
            plt.bar(isimler, ortalamalar)
            plt.title("Öğrenci Ortalama Notları")
            plt.xlabel("Öğrenciler")
            plt.ylabel("Ortalama")
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()

    else:
        print("Geçersiz seçim. Lütfen menüdeki seçeneklerden birini girin.")
