# Import library selenium untuk automation browser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# Digunakan untuk mencari element (ID, XPATH, dll)
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# Digunakan untuk menunggu element muncul (dynamic loading)
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Membuka browser Chrome
driver = webdriver.Chrome()
# Membuka halaman Google
driver.get("https://www.google.com")

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.NAME, "q"))
)
# Ambil element search box
input_element = driver.find_element(By.NAME, "q")
input_element.clear()
# Mengisi keyword pencarian + tekan ENTER
input_element.send_keys("tech with team" + Keys.ENTER)

# Menunggu sampai hasil pencarian muncul
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Tech With Tim"))
)
# Ambil link hasil pencarian berdasarkan text
link = driver.find_element(By.PARTIAL_LINK_TEXT, "Tech With Tim")
link.click()

time.sleep(60)

driver.quit()