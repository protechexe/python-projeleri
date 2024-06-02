from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

def e_devlet():
    chrome_driver_path = r"C:\Users\kullanıcıadı\Desktop\chromedriver-win64\chromedriver.exe" # bu alanda selenium için webdriver yüklemeniz gerekiyor
    service = Service(executable_path=chrome_driver_path)
    driver = webdriver.Chrome(service=service)

    driver.get("https://www.turkiye.gov.tr/")
    time.sleep(1)
    driver.set_window_size(1500,1080)
    time.sleep(1)
    giris_yap = driver.find_element(By.XPATH, "//*[@id='l']/a")
    giris_yap.click()
    time.sleep(1)
    kullanici_adi = driver.find_element(By.XPATH, "//*[@id='tridField']")
    sifre = driver.find_element(By.XPATH, "//*[@id='egpField']")
    kullanici_adi.send_keys("tckimlik") # bu alana tc nizi girin
    time.sleep(1)
    sifre.send_keys("sifre") # bu alana e devlet şifrenizi girin
    time.sleep(1)
    kullanici_giris = driver.find_element(By.XPATH, "//*[@id='loginForm']/fieldset/div[5]/button[2]")
    kullanici_giris.click()
    time.sleep(1)
    time.sleep(3000)


e_devlet()
