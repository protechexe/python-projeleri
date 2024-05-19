import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit, QMessageBox
from PyQt5.QtGui import QCursor, QFont
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QDesktopServices  
from tldextract import extract
import requests
from urllib3.exceptions import MaxRetryError, NameResolutionError
import ssl

ssl_context = ssl.create_default_context()
ssl_context.check_hostname = True
ssl_context.verify_mode = ssl.CERT_REQUIRED

safe_extensions = ["com", "biz", "net", "org", "info", "tr", "asia", "gov", "int", "mil", "com.tr", "gov.tr"]

class SSLChecker(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SSL Sertifikası Kontrol Programı")
        self.setStyleSheet("background-color: #1c1c1c; color: white;")
        self.setGeometry(100, 100, 600, 600)

        self.init_ui()

    def init_ui(self):
        title_label = QLabel("SSL Sertifikası Kontrol Programı", self)
        title_label.setStyleSheet("font-size: 20px; font-weight: bold; color: #3498db; margin-bottom: 20px;")

        self.url_label = QLabel("Link:", self)
        self.url_input = QLineEdit(self)
        self.url_input.setStyleSheet("background-color: #2c3e50; color: white;")
        self.url_input.setFont(QFont("Arial", 8))  

        self.result_text = QTextEdit(self)
        self.result_text.setStyleSheet("background-color: #34495e; color: white;")

        self.check_button = QPushButton("Kontrol Et", self)
        self.check_button.setStyleSheet("background-color: #2980b9; color: white;")
        self.check_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.check_button.clicked.connect(self.check_ssl)

        self.visit_button = QPushButton("Siteye Güvenli Git", self)  
        self.visit_button.setStyleSheet("background-color: #2ecc71; color: white;")
        self.visit_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.visit_button.clicked.connect(self.open_link)  

        vbox = QVBoxLayout(self)
        vbox.addWidget(title_label)
        vbox.addWidget(self.url_label)
        vbox.addWidget(self.url_input)
        vbox.addWidget(self.check_button)
        vbox.addWidget(self.result_text)
        vbox.addWidget(self.visit_button) 

        self.setLayout(vbox)

    def check_ssl(self):
        url = self.url_input.text()
        try:
            response = requests.get(url, timeout=5, verify=True)
            domain = extract(url).suffix

            if domain.lower() in [ext.lower() for ext in safe_extensions]:
                self.result_text.append(f"{url} güvenli bir uzantıya sahiptir. Siteye güvenle gidebilirsiniz.")
            else:
                self.result_text.append(f"{url} potansiyel olarak saldırgan bir uzantıya sahip olabilir.")
        except requests.exceptions.SSLError:
            self.result_text.append(f"{url} SSL sertifikası bulunamadı. Bağlantı güvensiz olabilir.")
            QMessageBox.critical(self, "Hata", "SSL sertifikası bulunamadı. Bağlantı güvensiz olabilir.")
        except requests.exceptions.ConnectionError:
            self.result_text.append(f"{url} bağlantısı başarısız. Ağ ayarlarınızı kontrol edin.")
            QMessageBox.critical(self, "Hata", "Bağlantı başarısız. Ağ ayarlarınızı kontrol edin.")
        except Exception as e:
            self.result_text.append(f"Hata: {e}")
            QMessageBox.critical(self, "Hata", f"Hata: {e}")

    def open_link(self):  
        url = self.url_input.text()
        QDesktopServices.openUrl(QUrl(url))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SSLChecker()
    window.show()
    sys.exit(app.exec_())
