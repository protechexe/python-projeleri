from pytube import YouTube
import time

def videobilgileri_goster():
    print("---Video Bilgilerini Gösterme Paneli---")
    print("-"*75)
    print("Lütfen bekleyin...")
    time.sleep(1)

    try:
        url = YouTube(input("Lütfen bilgisini almak istediğiniz videonun linkini yapıştırın: "))
        print("-"*75)
        print("Bilgiler getiriliyor, lütfen bekleyin...")
        time.sleep(1)

        print("-"*75)
        print("Videonun Başlığı:",url.title)
        print("Videonun Sahibi:",url.author)
        print("İzlenme Sayısı:",url.views)
        print("Video Uzunluğu:",url.length,"Saniye")
        print("-"*75)
    except Exception as e:
        print("Bir hata oluştu, lütfen tekrar deneyin...",e)

def kucukresim_indir():
    print("---Video Küçük Resim İndirme Paneli---")
    print("-"*75)
    print("Lütfen bekleyin...")
    time.sleep(1)

    try:
        url = YouTube(input("Lütfen resmini indirmek istediğiniz videonun linkini yapıştırın: "))
        print("-"*75)
        print("Resim link haline getirilip indiriliyor, lütfen bekleyin...")
        time.sleep(1)

        print("Video Küçük Resmi:",url.thumbnail_url)
        print("-"*75)
    except Exception as e:
        print("Bir hata oluştu, lütfen tekrar deneyin...",e)

def video_indir():
    print("---Video İndirme Paneli---")
    print("-"*75)
    print("Lütfen bekleyin...")
    time.sleep(1)

    try:
        url = YouTube(input("Lütfen indirmek istediğiniz videonun linkini yapıştırın: "))
        print("-"*75)
        print("Video indiriliyor, lütfen bekleyin..")
        print("-"*75)

        video = url.streams.filter(progressive="True").first()
        video.download("C:\\Users\\kullanıcıadı\\Desktop") # buraya indireceğiniz dosya yolunu girin

        print("Video indirildi!")
        print("-"*75)

        print("İndirilen Video Bilgileri:")
        print("-"*75)
        print("Videonun Başlığı:",url.title)
        print("Videonun Sahibi:",url.author)
        print("İzlenme Sayısı:",url.views)
        print("Video Uzunluğu:",url.length,"Saniye")
        print("-"*75)
    except Exception as e:
        print("Bir hata oluştu, lütfen tekrar deneyin...",e)

def ses_indir():
    print("---Ses İndirme Paneli---")
    print("-"*75)
    print("Lütfen bekleyin...")
    time.sleep(1)

    try:
        url = YouTube(input("Lütfen indirmek istediğiniz ses videosunun linkini yapıştırın: "))
        print("-"*75)
        print("Ses indiriliyor, lütfen bekleyin...")
        print("-"*75)

        ses = url.streams.filter(mime_type="audio/mp4").first()
        ses.download("C:\\Users\\kullanıcıadı\\Desktop") # buraya indireceğiniz dosya yolunu girin

        print("Ses indirildi!")
        print("-"*75)

        print("İndirilen ses bilgileri:")
        print("-"*75)
        print("Ses Başlığı:",url.title)
        print("Ses Sahibi:",url.author)
        print("İzlenme Sayısı:",url.views)
        print("Video Uzunluğu:",url.length,"Saniye")
        print("-"*75)
    except Exception as e:
        print("Bir hata oluştu, lütfen tekrar deneyin...",e)


while True:
    print("---Programa Hoş Geldiniz!---")
    print("-"*75)
    print("Lütfen bekleyin...")
    time.sleep(1)

    print("İşlemler: 1/Video Bilgileri Gösterme\n2/Video Küçük Resim İndirme")
    print("3/Video İndirme\n4/Videodan Ses İndirme\n5/Çıkış")
    print("-"*75)

    islem = input("İşleminiz: ")
    if islem == "1":
        videobilgileri_goster()
    elif islem == "2":
        kucukresim_indir()
    elif islem == "3":
        video_indir()
    elif islem == "4":
        ses_indir()
    elif islem == "5":
        print("Program kapatılıyor...")
        break
    else:
        print("Lütfen yapmak istediğiniz işlemi girin..")
