import codecs

def dosya_olustur():
    print("***DOSYA OLUŞTURMA***")
    print("-"*30)
    dosya_ismi = input("Lütfen oluşturmak istediğiniz dosya ismini girin: ")
    dosya_NEW = dosya_ismi + ".txt"
    veri_giris = input(f"Lütfen {dosya_NEW} dosyasına veri ekleyin: ")

    with codecs.open(dosya_NEW,"w", encoding="utf-8") as dosya:
        dosya.write(veri_giris)


    while True:
        soru_sor = input("Dosyaya başka veri eklemek ister misiniz? (E/H): ").lower()
        if soru_sor == "E":
            yeni_veri = input("Eklemek istediğiniz verileri girin: ")
            yeni_veri = "\n" + yeni_veri
            with codecs.open(dosya_NEW, "a", encoding="utf-8") as dosya:
                dosya.write(yeni_veri)
            print("Verileriniz güncellendi...")
        elif soru_sor == "H":
            print("Çıkış yapılıyor...")
            break
        else:
            print("Lütfen 'E' veya 'H' girin.")
    return dosya_NEW

def dosya_oku():
    print("***VERİTABANINDA BULUNAN VERİLER***")
    dosya_ismi = input("Lütfen okumak istediğiniz dosya ismini girin: ")
    dosya_yolu = dosya_ismi + ".txt"
    
    try:
        with codecs.open(dosya_yolu, "r", encoding="utf-8") as info:
            a = info.read()
            print("-"*30)
            print(f"{dosya_yolu} adlı dosyanın bayt uzunluğu: {len(a)}'tır.")
            print("-"*30)
            print("Dosyada Bulunan Veriler Aşağıda Sıralanmıştır:")
            print(a)
            print("-"*30)
    except FileNotFoundError:
        print(f"{dosya_yolu} adlı dosya bulunamadı.")

def dosyaya_veri_ekle():
    print("***DOSYA VERİ EKLEME PANELİ***")
    dosya_ismi = input("Veri eklemek istediğiniz dosyanın ismini girin: ")
    dosya_yolu = dosya_ismi + ".txt"

    try:
        with codecs.open(dosya_yolu,"a", encoding="utf-8") as dosya:
            yeni_veri = input(f"{dosya_yolu} dosyasına eklemek istediğiniz verileri girin: ")
            yeni_veri = "\n" + yeni_veri
            dosya.write(yeni_veri)
            print("Verileriniz güncellendi...")
    except FileNotFoundError:
        print(f"{dosya_yolu} adlı dosya bulunamadı...")


while True:
    print("***DOSYA İŞLEMLER PROGRAMI***")
    print("-"*30)
    print("Yapılacak işlemler: 1/Dosya Oluşturma\n2/Dosya Okuma\n3/Dosyaya Veri Ekle\n4/Çıkış")
    islem = input("Yapmak istediğiniz işlemi girin: 1/2/3/4: ")
    if islem == "1":
        dosya_olustur()
    elif islem == "2":
        dosya_oku()
    elif islem == "3":
        dosyaya_veri_ekle()
    elif islem == "4":
        print("Çıkış yapılıyor...")
        break
    else:
        print("Lütfen yapmak istediğiniz işlemi girin...")
