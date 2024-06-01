from bs4 import BeautifulSoup
import requests
import codecs
import time


def kod_yazdir():
    print("----HTML KOD YAZDIRMA PANELİ----")
    print("-"*45)
    print("Lütfen bekleyin...")
    time.sleep(1)

    print("Programda yazdırmak istediğiniz sitenin linkini girin.")
    time.sleep(1)
    print("Linki girdikten sonra sitenin statü kodu taranır ve statü karşılanırsa kod yazdırılır.")
    print("-"*45)

    url = input("Lütfen link girin: ")

    url = requests.get(url)

    if url.status_code == 200:
        soup = BeautifulSoup(url.content, "html.parser")

        formatted_html = soup.prettify()

        with codecs.open("main.txt", "w", encoding="utf-8") as dosya:
            dosya.write(formatted_html)

        print("Html kodları başarıyla main.txt dosyasına yazdırıldı.")
    else:
        print(f"Siteden veri çekilemez.. Statü kodu: {url.status_code}")


kod_yazdir()
