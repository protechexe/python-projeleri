import time
import codecs

def kayit_ol():
    print("***KULLANICI KAYIT PANELİ***")
    print("-"*30)
    print("Lütfen Bekleyin...")
    time.sleep(1)
    kullanici_adi = input("Kullanıcı adı girin: ")
    kullanici_sifre = input("Şifrenizi Girin: ")
    sifre_tekrar = input("Şifrenizi tekrar girin: ")

    with codecs.open("users.txt","w", encoding="utf-8") as dosya:
        dosya.write(f"{kullanici_adi},{kullanici_sifre}\n")

    if kullanici_sifre == sifre_tekrar:
        print("Kullanıcı adı ve şifre oluşturuldu!")
    else:
        print("Lütfen şifrenizin aynı olmasına dikkat edin!")

def giris_yap():
    print("***KULLANICI GİRİŞ PANELİ***")
    print("-"*30)
    print("Lütfen Bekleyin...")
    time.sleep(1)
    giris_kullanici_adi = input("Kullanıcı adınızı girin: ")
    giris_kullanici_sifre = input("Şifrenizi girin: ")

    try:
        with codecs.open("users.txt","r", encoding="utf-8") as dosya:
            satir = dosya.readline().strip()
            if not satir:
                raise FileNotFoundError
            kayitli_kullanici_adi, kayitli_kullanici_sifre = satir.split(",")

            if giris_kullanici_adi == kayitli_kullanici_adi and giris_kullanici_sifre == kayitli_kullanici_sifre:
                print("Giriş başarılı!")
            else:
                print("Kullanıcı adı ve şifre hatalı, lütfen tekrar deneyin..")
    except FileNotFoundError:
        print("Kullanıcı adı ve şifre bulunamadı, lütfen kayıt olun..")


while True:
    print("***ANA MENÜ***")
    print("-"*30)
    print("Lütfen bekleyin...")
    time.sleep(1)
    print("İşlemler: 1/Kullanıcı Kayıt\n2/Kullanıcı Giriş\n3/Çıkış")

    print("-"*30)
    islem = input("İşleminiz: 1/2/3: ")

    if islem == "1":
        kayit_ol()
    elif islem == "2":
        giris_yap()
    elif islem == "3":
        print("Çıkış yapılıyor...")
        time.sleep(1)
        print("Çıkış yapılıyor...")
        time.sleep(1)
        break
    else:
        print("Lütfen yapmak istediğiniz işlemi girin!")
