import sqlite3

db = sqlite3.connect("borcluismi.db")

yetki = db.cursor()

yetki.execute("CREATE TABLE IF NOT EXISTS borclular (isim,borcmiktar)")

while True:
    print("***VERESİYE PROGRAMI***")
    print("-"*30)

    print("Yapılacak İşlemler: 1/Borçlu Ekle\n2/Borçlu Kişi Listele\n3/Borçlu Kişi Sil\n4/Çıkış")
    print("-"*30)
    sor = input("İşleminiz: ")
    if sor == "1":
        print("-----VERESİYE BOÇ EKLEME PANELİ-----")
        print("-"*30)
        
        isim_sor = input("Borçlu kişinin ismini ve soyismini girin: ")
        borc_sor = input("Borç miktarını girin: ")
        yetki.execute(f"INSERT INTO borclular VALUES('{isim_sor}','{borc_sor}')")
        db.commit()
        print(f"İşlem tamamlandı! Eklenen kişi: {isim_sor}")

    elif sor == "2":
        print("-----BORÇLU KİŞİ LİSTE PANELİ-----")

        yetki.execute("SELECT *FROM borclular")
        yazdir = yetki.fetchall()
        db.commit()
        say = 1

        for i in yazdir:
            print("-"*30)
            print(f"{say}: Borçlu kişinin ismi: {i[0]}\nBorç Miktarı: {i[1]}")
            print("-"*30)
            say += 1
    
    elif sor == "3":
        print("-----BORÇLU KİŞİ SİLME PANELİ-----")

        kisi_sor = input("Silinecek kişinin ismini ve soyismini girin: ")
        yetki.execute(f"DELETE FROM borclular WHERE isim='{kisi_sor}'")
        yetki.execute(f"DELETE FROM borclular WHERE borcmiktar='{kisi_sor}'")
        db.commit()

        print(f"Silme işlemi tamamlandı! Silinen kişi ismi: {kisi_sor}")

    elif sor == "4":
        print("Çıkış yapılıyor...")
        break
    
    else:
        print("Lütfen yapmak istediğiniz işlemi girin...")
