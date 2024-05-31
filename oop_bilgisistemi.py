import time

class maviyaka:
    def __init__(self,isim=None,soyisim=None,bolum=None,unvani=None,pozisyon=None):
        self.isim = isim
        self.soyisim = soyisim
        self.bolum = bolum
        self.unvani = unvani
        self.pozisyon = pozisyon

    def personel_ekle(self):
        print("---PERSONEL EKLEME PANELİ---")
        print("-"*45)
        personel_isim = input("Personelin ismini girin: ")
        personel_soyisim = input("Personelin soyismini girin: ")
        personel_bolum = input("Personelin bölümünü girin: ")
        personel_unvani = input("Personelin unvanını girin: ")
        personel_pozisyon = input("Personelin pozisyonunu girin: ")

        self.isim = personel_isim
        self.soyisim = personel_soyisim
        self.bolum = personel_bolum
        self.unvani = personel_unvani
        self.pozisyon = personel_pozisyon

        print("Personel ekleniyor...")
        time.sleep(1)
        print("Personel eklendi...")

    def bilgileri_goster(self):
        print("---PERSONEL BİLGİ PANELİ---")
        print("-"*45)
        print(f"Personel İsmi: {self.isim}\nPersonel Soyismi: {self.soyisim}\nPersonel Bölümü: {self.bolum}\n")
        print(f"Personel Unvanı: {self.unvani}\nPersonel Pozisyon: {self.pozisyon}")
        print("-"*45)

class beyazyaka(maviyaka):
    def __init__(self,isim=None,soyisim=None,bolum=None,unvani=None,pozisyon=None,kidem=None):
        super().__init__(isim,soyisim,bolum,unvani,pozisyon)
        self.kidem = kidem

    def personel_ekle(self):
        print("---PERSONEL EKLEME PANELİ---")
        print("-"*45)
        personel_isim = input("Personelin ismini girin: ")
        personel_soyisim = input("Personelin soyismini girin: ")
        personel_bolum = input("Personelin bölümünü girin: ")
        personel_unvani = input("Personelin unvanını girin: ")
        personel_pozisyon = input("Personelin pozisyonunu girin: ")
        personel_tecrube = input("Personelin tecrübe yılını girin: ")

        self.isim = personel_isim
        self.soyisim = personel_soyisim
        self.bolum = personel_bolum
        self.unvani = personel_unvani
        self.pozisyon = personel_pozisyon
        self.kidem = personel_tecrube

        print("Personel ekleniyor...")
        time.sleep(1)
        print("Personel eklendi...")

    def bilgileri_goster(self):
        print("---PERSONEL BİLGİ SİSTEMİ---")
        print("-"*45)
        print(f"Personel İsmi: {self.isim}\nPersonel Soyismi: {self.soyisim}\nPersonel Bölümü: {self.bolum}\n")
        print(f"Personel Unvanı: {self.unvani}\nPersonel Pozisyon: {self.pozisyon}\nPersonel Kıdem: {self.kidem} Yıl")
        print("-"*45)

maviyaka_personel = []
beyazyaka_personel = []

while True:
    print("---PERSONEL PANELİ---")
    print("-"*45)
    print("İşlemler: 1. Mavi Yaka Personel Ekleme\n2. Mavi Yaka Personel Listesi")
    print("3. Beyaz Yaka Personel Ekleme\n4. Beyaz Yaka Personel Listesi\n5. Çıkış")
    print("-"*45)

    islem = input("Lütfen yapmak istediğiniz işlemi girin: ")
    if islem == "1":
        personel = maviyaka()
        personel.personel_ekle()
        maviyaka_personel.append(personel)
    elif islem == "2":
        for personel in maviyaka_personel:
            personel.bilgileri_goster()
    elif islem == "3":
        personel = beyazyaka()
        personel.personel_ekle()
        beyazyaka_personel.append(personel)
    elif islem == "4":
        for personel in beyazyaka_personel:
            personel.bilgileri_goster()
    elif islem == "5":
        print("Çıkış yapılıyor...")
        break
    else:
        print("Lütfen yapmak istediğiniz işlemi girin...")
