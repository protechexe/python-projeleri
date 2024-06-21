import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
import time
import sys
import os

CURRENT_VERSION = "1.0.0"

class Edevlet():
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = None

    def giris(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("https://www.turkiye.gov.tr/")
        wait = WebDriverWait(self.driver, 10)

        giris_yap = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='l']/a")))
        giris_yap.click()

        usernameInput = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='tridField']")))
        passwordInput = self.driver.find_element(By.XPATH, "//*[@id='egpField']")

        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)

        time.sleep(2)

    def arama_yap(self, arama_metni):
        wait = WebDriverWait(self.driver, 20)
        arama_input = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='searchField']")))
        arama_input.send_keys(arama_metni)
        arama_input.send_keys(Keys.ENTER)

        time.sleep(2)

    def linke_tikla(self, xpath):
        wait = WebDriverWait(self.driver, 20)
        link = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        link.click()

        time.sleep(3)

    def sgk_hizmet_dokumu(self):
        self.giris()
        self.arama_yap("SGK Tescil ve Hizmet Dökümü")
        self.linke_tikla("//*[@id='s01']/div[2]/ul/li[1]/a")
        js_code = "alert('Bu aşamadan sonra işlem yapabilirsiniz. İnstagram: @yuns.eemrree')"
        self.driver.execute_script(js_code)

    def vergi_borcu_sorgula(self):
        self.giris()
        self.arama_yap("Vergi Borcu Sorgulama ve Ödeme")
        self.linke_tikla("//*[@id='s01']/div[2]/ul/li[1]/a")
        js_code = "alert('Bu aşamadan sonra işlem yapabilirsiniz. İnstagram: @yuns.eemrree')"
        self.driver.execute_script(js_code)

    def sosyal_yardim(self):
        self.giris()
        self.arama_yap("Sosyal Yardım Bilgileri Sorgulama")
        self.linke_tikla("//*[@id='s01']/div[2]/ul/li[1]/a")
        js_code = "alert('Bu aşamadan sonra işlem yapabilirsiniz. İnstagram: @yuns.eemrree')"
        self.driver.execute_script(js_code)

    def calisma_hayatim(self):
        self.giris()
        self.arama_yap("Çalışma Hayatım")
        self.linke_tikla("//*[@id='s01']/div[2]/ul/li/a")
        js_code = "alert('Bu aşamadan sonra işlem yapabilirsiniz. İnstagram: @yuns.eemrree')"
        self.driver.execute_script(js_code)

    def ne_zaman_emekli(self):
        self.giris()
        self.arama_yap("Normal Şartlarda Ne Zaman Emekli")
        self.linke_tikla("//*[@id='s01']/div[2]/ul/li/a")
        js_code = "alert('Bu aşamadan sonra işlem yapabilirsiniz. İnstagram: @yuns.eemrree')"
        self.driver.execute_script(js_code)

    def arac_sorgula(self):
        self.giris()
        self.arama_yap("Adıma Tescilli Araç Sorgulama")
        self.linke_tikla("//*[@id='s01']/div[2]/ul/li[1]/a")
        js_code = "alert('Bu aşamadan sonra işlem yapabilirsiniz. İnstagram: @yuns.eemrree')"
        self.driver.execute_script(js_code)

    def dava_sorgula(self):
        self.giris()
        self.arama_yap("Dava Dosyası Sorgulama")
        self.linke_tikla("//*[@id='s01']/div[2]/ul/li[1]/a")
        js_code = "alert('Bu aşamadan sonra işlem yapabilirsiniz. İnstagram: @yuns.eemrree')"
        self.driver.execute_script(js_code)

    def plaka_ceza_sorgula(self):
        self.giris()
        self.arama_yap("Araç Plakasına Yazılan Ceza Sorgulama")
        self.linke_tikla("//*[@id='s01']/div[2]/ul/li[1]/a")
        js_code = "alert('Bu aşamadan sonra işlem yapabilirsiniz. İnstagram: @yuns.eemrree')"
        self.driver.execute_script(js_code)

    def askerligim(self):
        self.giris()
        self.arama_yap("Askerliğim")
        self.linke_tikla("//*[@id='s01']/div[2]/ul/li[1]/a")
        js_code = "alert('Bu aşamadan sonra işlem yapabilirsiniz. İnstagram: @yuns.eemrree')"
        self.driver.execute_script(js_code)

class EdevletThread(QThread):
    finished = pyqtSignal()
    error = pyqtSignal(str)

    def __init__(self, kullanici_adi, parola, islem):
        super().__init__()
        self.kullanici_adi = kullanici_adi
        self.parola = parola
        self.islem = islem

    def run(self):
        try:
            edevlet = Edevlet(self.kullanici_adi, self.parola)
            if self.islem == "1":
                edevlet.giris()
                time.sleep(3000)
            elif self.islem == "2":
                edevlet.sgk_hizmet_dokumu()
                time.sleep(3000)
            elif self.islem == "3":
                edevlet.vergi_borcu_sorgula()
                time.sleep(3000)
            elif self.islem == "4":
                edevlet.sosyal_yardim()
                time.sleep(3000)
            elif self.islem == "5":
                edevlet.calisma_hayatim()
                time.sleep(3000)
            elif self.islem == "6":
                edevlet.ne_zaman_emekli()
                time.sleep(3000)
            elif self.islem == "7":
                edevlet.arac_sorgula()
                time.sleep(3000)
            elif self.islem == "8":
                edevlet.dava_sorgula()
                time.sleep(3000)
            elif self.islem == "9":
                edevlet.plaka_ceza_sorgula()
                time.sleep(3000)
            elif self.islem == "10":
                edevlet.askerligim()
                time.sleep(3000)
            else:
                self.error.emit("Lütfen geçerli bir işlem numarası girin...")
            self.finished.emit()
        except Exception as e:
            self.error.emit(str(e))

class EdevletArayuz(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("E-Devlet Botu")
        self.setGeometry(500, 200, 500, 300)

        self.label_islemler = QLabel("İŞLEMLER")
        self.label_islemler.setStyleSheet("font-weight: bold; font-size: 18px;")

        self.islemler_text = QLabel(
            "1. E-Devlet Giriş\n2. Sgk Tescil ve Hizmet Dökümü Sorgulama\n3. Vergi Borcu Sorgula\n"
            "4. Sosyal Yardım Bilgileri Sorgulama\n5. Çalışma Hayatım\n"
            "6. Normal Şartlarda Ne Zaman Emekli Olabilirim?\n7. Adıma Tescilli Araç Sorgulama\n"
            "8. Dava Dosyası Sorgulama\n9. Araç Plakasına Yazılan Ceza Sorgulama\n10. Askerliğim"
        )

        self.kullanici_adi_label = QLabel("TC Kimlik Numaranız:")
        self.kullanici_adi_input = QLineEdit()

        self.parola_label = QLabel("E-Devlet Şifreniz:")
        self.parola_input = QLineEdit()
        self.parola_input.setEchoMode(QLineEdit.Password)

        self.islem_label = QLabel("Yapmak istediğiniz işlemi numara ile girin:")
        self.islem_input = QLineEdit()

        self.button = QPushButton("Botu Çalıştır")
        self.button.clicked.connect(self.calistir)

        self.update_button = QPushButton("Güncellemeleri Kontrol Et")
        self.update_button.clicked.connect(self.check_for_updates)


        vbox = QVBoxLayout()
        vbox.addWidget(self.label_islemler)
        vbox.addWidget(self.islemler_text)
        vbox.addWidget(self.kullanici_adi_label)
        vbox.addWidget(self.kullanici_adi_input)
        vbox.addWidget(self.parola_label)
        vbox.addWidget(self.parola_input)
        vbox.addWidget(self.islem_label)
        vbox.addWidget(self.islem_input)
        vbox.addWidget(self.button)
        vbox.addWidget(self.update_button)

        self.setLayout(vbox)

    def calistir(self):
        kullanici_adi = self.kullanici_adi_input.text()
        parola = self.parola_input.text()
        islem = self.islem_input.text()

        if not kullanici_adi or not parola or not islem:
            print("Lütfen tüm bilgileri eksiksiz girin...")
            return

        self.thread = EdevletThread(kullanici_adi, parola, islem)
        self.thread.finished.connect(self.islem_bitti)
        self.thread.error.connect(self.hata_olustu)
        self.thread.start()

    def islem_bitti(self):
        print("İşlem başarıyla tamamlandı.")

    def hata_olustu(self, hata):
        print(f"Bir hata oluştu: {hata}")

    def check_for_updates(self):
        try:
            response = requests.get("https://drive.google.com/u/0/uc?id=19LDVWoth6vkZH6XPa3CK-67mortg8qz6&export=download")
            data = response.json()
            latest_version = data['version']
            download_url = data['url']

            if latest_version > CURRENT_VERSION:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setWindowTitle("Güncelleme Mevcut")
                msg.setText(f"Yeni versiyon mevcut: {latest_version}\nİndirmek için tıklayın.")
                msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                msg.buttonClicked.connect(lambda x: self.open_url(download_url) if x.text() == "OK" else None)
                msg.exec_()
            else:
                QMessageBox.information(self, "Güncel", "Programınız güncel.")
        except Exception as e:
            QMessageBox.critical(self, "Hata", f"Güncelleme kontrolünde bir hata oluştu: {str(e)}")

    def open_url(self, url):
        try:
            os.system(f"start {url}")
        except Exception as e:
            QMessageBox.critical(self, "Hata", f"Bağlantı açılırken bir hata oluştu: {str(e)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EdevletArayuz()
    window.show()

    sys.exit(app.exec_())


