import time
import random

def tahmin_oyunu():
    print("---Tahmin Oyununa hoş geldiniz!---")
    print("-"*45)
    print("Lütfen bekleyin")
    time.sleep(1)

    print("Tahmin aralıkları: 1/1-9 2/10-50 3/51-100 şeklindedir. Tercihleri 1/2/3 şeklinde yapabilirsiniz.")
    print("-"*45)
    time.sleep(1)
    print("Toplam 5 adet tahmin hakkınız bulunmakta. Tahmin hakkınız kalmadığı zaman oyun biter.")
    print("-"*45)
    time.sleep(1)

    islem = input("İşleminiz: ")
    if islem == "1":
        print("Oyun başlıyor..")
        time.sleep(1)
        print("-"*45)

        rastgele_sayi = random.randint(1,10)
        tahmin_hakki = 5

        while tahmin_hakki > 0:
            try:
                print(f"Kalan tahmin hakkınız: {tahmin_hakki}")
                tahmin = int(input("1 ile 9 arasında bir sayı girin: "))

                if tahmin == rastgele_sayi:
                    print(f"Tebrikler, sayıyı bildiniz! Sayı: {rastgele_sayi}")
                    break
                elif tahmin < rastgele_sayi:
                    print("Daha büyük bir sayı girin...")
                else:
                    print("Daha küçük bir sayı girin...")
            except ValueError:
                print("Lütfen doğru değer girin...")
            except Exception as e:
                print("Bir hata oluştu..",e)

            tahmin_hakki -= 1

        if tahmin_hakki == 0:
            print(f"Tahmin hakkınız kalmadı. Doğru sayı: {rastgele_sayi}")
    elif islem == "2":
        print("Oyun başlıyor...")
        time.sleep(1)
        print("-"*45)

        rastgele_sayi2 = random.randint(10,51)
        tahmin_hakki2 = 5

        while tahmin_hakki2 > 0:
            try:
                print(f"Kalan tahmin hakkınız: {tahmin_hakki2}")
                tahmin2 = int(input("10 ile 50 arasında bir sayı girin: "))

                if tahmin2 == rastgele_sayi2:
                    print(f"Tebrikler, sayıyı bildiniz! Sayı: {rastgele_sayi2}")
                    break
                elif tahmin2 < rastgele_sayi2:
                    print("Daha büyük bir sayı girin...")
                else:
                    print("Daha küçük bir sayı girin...")
            except ValueError:
                print("Lütfen doğru değer girin...")
            except Exception as e:
                print("Bir hata oluştu..",e)
                
            tahmin_hakki2 -= 1

        if tahmin_hakki2 == 0:
            print(f"Tahmin hakkınız kalmadı. Doğru sayı: {rastgele_sayi2}")
    elif islem == "3":
        print("Oyun başlıyor...")
        time.sleep(1)
        print("-"*45)

        rastgele_sayi3 = random.randint(50,101)
        tahmin_hakki3 = 5

        while tahmin_hakki3 > 0:
            try:
                print(f"Kalan tahmin hakkınız: {tahmin_hakki3}")
                tahmin3 = int(input("50 ile 100 arasında bir sayı girin: "))

                if tahmin3 == rastgele_sayi3:
                    print(f"Tebrikler, sayıyı bildiniz! Sayı: {rastgele_sayi3}")
                    break
                elif tahmin3 < rastgele_sayi3:
                    print("Daha büyük bir sayı girin...")
                else:
                    print("Daha küçük bir sayı girin...")
            except ValueError:
                print("Lütfen doğru değer girin...")
            except Exception as e:
                print("Bir hata oluştu..",e)

            tahmin_hakki3 -= 1
        
        if tahmin_hakki3 == 0:
            print(f"Tahmin hakkınız kalmadı. Doğru sayı: {rastgele_sayi3}")
    else:
        print("Lütfen yapmak istediğiniz işlemi girin...")

def matematik_oyunu():
    print("---Matematik Oyununa Hoş Geldiniz!---")
    print("-"*45)
    print("Lütfen bekleyin...")
    time.sleep(1)

    print("İşlemler: 1/Toplama\n2/Çıkartma\n3/Çarpma\n4/Bölme")
    print("-"*45)
    time.sleep(1)
    
    islem = input("İşleminiz: ")
    if islem == "1":
        print("---Toplama Oyunu---")
        print("-"*45)
        time.sleep(1)
        print("Oyun başlıyor...")
        time.sleep(1)
        print("-"*45)

        print("Kaç basamaklı işlem yapmak istersiniz? 1/2 basamaklı\n2/3 basamaklı\n3/4 basamaklı")
        print("-"*45)

        while True:
            veri = input("İşleminiz: ")
            if veri == "1":
                rastgele_sayi1 = random.randint(1,100)
                rastgele_sayi2 = random.randint(1,100)

                try:
                    toplama = int(input(f"{rastgele_sayi1} + {rastgele_sayi2} = "))
                    topla = rastgele_sayi1 + rastgele_sayi2

                    if toplama == topla:
                        print("Tebrikler, doğru cevap!")
                        break
                    else:
                        print("Yanlış cevap, pes etme tekrar dene :)")
                except ValueError:
                    print("Lütfen doğru değer girin...")
                except Exception as e:
                    print("Bir hata oluştu..",e)

            elif veri == "2":
                rastgele_sayi3 = random.randint(100,1000)
                rastgele_sayi4 = random.randint(100,1000)

                try:
                    toplama2 = int(input(f"{rastgele_sayi3} + {rastgele_sayi4} = "))
                    topla2 = rastgele_sayi3 + rastgele_sayi4

                    if toplama2 == topla2:
                        print("Tebrikler, doğru cevap!")
                        break
                    else:
                        print("Yanlış cevap, pes etme tekrar dene :)")
                except ValueError:
                    print("Lütfen doğru değer girin...")
                except Exception as e:
                    print("Bir hata oluştu..",e)

            elif veri == "3":
                rastgele_sayi5 = random.randint(1000,10000)
                rastgele_sayi6 = random.randint(1000,10000)

                try:
                    toplama3 = int(input(f"{rastgele_sayi5} + {rastgele_sayi6} = "))
                    topla3 = rastgele_sayi5 + rastgele_sayi6

                    if toplama3 == topla3:
                        print("Tebrikler, doğru cevap!")
                        break
                    else:
                        print("Yanlış cevap, pes etme tekrar dene :)")
                except ValueError:
                    print("Lütfen doğru değer girin...")
                except Exception as e:
                    print("Bir hata oluştu..",e)
                    
            else:
                print("Lütfen yapmak istediğiniz işlemi girin...")
    elif islem == "2":
        print("---Çıkarma Oyunu---")
        print("-"*45)
        time.sleep(1)
        print("Oyun başlıyor...")
        time.sleep(1)
        print("-"*45)

        print("Kaç basamaklı işlem yapmak istersiniz? 1/2 basamaklı\n2/3 basamaklı\n3/4 basamaklı")
        print("-"*45)

        while True:
            veri = input("İşleminiz: ")
            if veri == "1":
                rastgele_sayi7 = random.randint(1,100)
                rastgele_sayi8 = random.randint(1,100)

                try:
                    cikarma = int(input(f"{rastgele_sayi7} - {rastgele_sayi8} = "))
                    cikar = rastgele_sayi7 - rastgele_sayi8

                    if cikarma == cikar:
                        print("Tebrikler, doğru cevap!")
                        break
                    else:
                        print("Yanlış cevap, pes etme tekrar dene :)")
                except ValueError:
                    print("Lütfen doğru değer girin...")
                except Exception as e:
                    print("Bir hata oluştu..",e)

            elif veri == "2":
                rastgele_sayi9 = random.randint(100,1000)
                rastgele_sayi10 = random.randint(100,1000)

                try:
                    cikarma2 = int(input(f"{rastgele_sayi9} - {rastgele_sayi10} = "))
                    cikar2 = rastgele_sayi9 - rastgele_sayi10

                    if cikarma2 == cikar2:
                        print("Tebrikler, doğru cevap!")
                        break
                    else:
                        print("Yanlış cevap, pes etme tekrar dene :)")
                except ValueError:
                    print("Lütfen doğru değer girin...")
                except Exception as e:
                    print("Bir hata oluştu..",e)

            elif veri == "3":
                rastgele_sayi11 = random.randint(1000,10000)
                rastgele_sayi12 = random.randint(1000,10000)

                try:
                    cikarma3 = int(input(f"{rastgele_sayi11} - {rastgele_sayi12} = "))
                    cikar3 = rastgele_sayi11 - rastgele_sayi12

                    if cikarma3 == cikar3:
                        print("Tebrikler, doğru cevap!")
                        break
                    else:
                        print("Yanlış cevap, pes etme tekrar dene :)")
                except ValueError:
                    print("Lütfen doğru değer girin...")
                except Exception as e:
                    print("Bir hata oluştu..",e)

            else:
                print("Lütfen yapmak istediğiniz işlemi girin...")
    elif islem == "3":
        print("---Çarpma Oyunu---")
        print("-"*45)
        time.sleep(1)
        print("Oyun başlıyor...")
        time.sleep(1)
        print("-"*45)

        print("Kaç basamaklı işlem yapmak istersiniz? 1/2 basamaklı\n2/3 basamaklı\n3/4 basamaklı")
        print("-"*45)

        while True:
            veri = input("İşleminiz: ")
            if veri == "1":
                rastgele_sayi13 = random.randint(1,100)
                rastgele_sayi14 = random.randint(1,100)

                try:
                    carpma = int(input(f"{rastgele_sayi13} x {rastgele_sayi14} = "))
                    carp = rastgele_sayi13 * rastgele_sayi14

                    if carpma == carp:
                        print("Tebrikler, doğru cevap!")
                        break
                    else:
                        print("Yanlış cevap, pes etme tekrar dene :)")
                except ValueError:
                    print("Lütfen doğru değer girin...")
                except Exception as e:
                    print("Bir hata oluştu..",e)

            elif veri == "2":
                rastgele_sayi15 = random.randint(100,1000)
                rastgele_sayi16 = random.randint(100,1000)

                try:
                    carpma2 = int(input(f"{rastgele_sayi15} x {rastgele_sayi16} = "))
                    carp2 = rastgele_sayi15 * rastgele_sayi16

                    if carpma2 == carp2:
                        print("Tebrikler, doğru cevap!")
                        break
                    else:
                        print("Yanlış cevap, pes etme tekrar dene :)")
                except ValueError:
                    print("Lütfen doğru değer girin...")
                except Exception as e:
                    print("Bir hata oluştu..",e)

            elif veri == "3":
                rastgele_sayi17 = random.randint(1000,10000)
                rastgele_sayi18 = random.randint(1000,10000)

                try:
                    carpma3 = int(input(f"{rastgele_sayi17} x {rastgele_sayi18} = "))
                    carp3 = rastgele_sayi17 * rastgele_sayi18

                    if carpma3 == carp3:
                        print("Tebrikler, doğru cevap!")
                        break
                    else:
                        print("Yanlış cevap, pes etme tekrar dene :)")
                except ValueError:
                    print("Lütfen doğru değer girin...")
                except Exception as e:
                    print("Bir hata oluştu..",e)

            else:
                print("Lütfen yapmak istediğiniz işlemi girin...")

    elif islem == "4":
        print("---Bölme Oyunu---") # bölme işlemleri tamsayı olarak hesaplanır.
        print("-"*45) # bölme işlemini yaparken cevapları tamsayı olarak vermeniz gerekiyor.
        time.sleep(1)
        print("Oyun başlıyor...")
        time.sleep(1)
        print("-"*45)

        print("Kaç basamaklı işlem yapmak istersiniz? 1/2 basamaklı\n2/3 basamaklı\n3/4 basamaklı")
        print("-"*45)

        while True:
            veri = input("İşleminiz: ")
            if veri == "1":
                rastgele_sayi19 = random.randint(1,100)
                rastgele_sayi20 = random.randint(1,100)
                while rastgele_sayi20 > rastgele_sayi19: #burada ikinci sayının ilk sayıdan büyük olmasını engellemek için bir döngüye alıyoruz.
                    rastgele_sayi20 = random.randint(1,100)

                try:
                    bolme = int(input(f"{rastgele_sayi19} % {rastgele_sayi20} = "))
                    bol = rastgele_sayi19 // rastgele_sayi20

                    if bolme == bol:
                        print("Tebrikler, doğru cevap!")
                        break
                    else:
                        print("Yanlış cevap, pes etme tekrar dene :)")
                except ValueError:
                    print("Lütfen doğru değer girin..")
                except ZeroDivisionError:
                    print("Sayı 0'a bölünemez..")
                except Exception as e:
                    print("Bir hata oluştu..",e)

            elif veri == "2":
                rastgele_sayi21 = random.randint(100,1000)
                rastgele_sayi22 = random.randint(100,1000)
                while rastgele_sayi22 > rastgele_sayi21:
                    rastgele_sayi21 = random.randint(100,1000)

                try:
                    bolme2 = int(input(f"{rastgele_sayi21} % {rastgele_sayi22} = "))
                    bol2 = rastgele_sayi21 // rastgele_sayi22
                    bolum = int(bol2)

                    if bolme2 == bolum:
                        print("Tebrikler, doğru cevap!")
                        break
                    else:
                        print("Yanlış cevap, pes etme tekrar dene :)")
                except ValueError:
                    print("Lütfen doğru değer girin..")
                except ZeroDivisionError:
                    print("Sayı 0'a bölünemez..")
                except Exception as e:
                    print("Bir hata oluştu..",e)

            elif veri == "3":
                rastgele_sayi23 = random.randint(1000,10000)
                rastgele_sayi24 = random.randint(1000,10000)
                while rastgele_sayi24 > rastgele_sayi23:
                    rastgele_sayi23 = random.randint(1000,10000)

                try:
                    bolme3 = int(input(f"{rastgele_sayi23} % {rastgele_sayi24} = "))
                    bol3 = rastgele_sayi23 // rastgele_sayi24

                    if bolme3 == bol3:
                        print("Tebrikler, doğru cevap!")
                        break
                    else:
                        print("Yanlış cevap, pes etme tekrar dene :)")
                except ValueError:
                    print("Lütfen doğru değer girin..")
                except ZeroDivisionError:
                    print("Sayı 0'a bölünemez..")
                except Exception as e:
                    print("Bir hata oluştu..",e)
            else:
                print("Lütfen yapmak istediğiniz işlemi girin...")

while True:
    print("---PYTHON OYUN PROGRAMINA HOŞ GELDİNİZ!---")
    print("-"*45)
    print("Lütfen bekleyin...")
    time.sleep(1)
    print("-"*45)
    print("İşlemler: 1/Sayı Tahmin Oyunu\n2/Matematik Oyunu\n3/Çıkış")
    print("-"*45)

    islem = input("İşleminiz: ")
    if islem == "1":
        tahmin_oyunu()
    elif islem == "2":
        matematik_oyunu()
    elif islem == "3":
        print("Çıkış yapılıyor..")
        break
    else:
        print("Lütfen geçerli bir işlem giriniz..")
