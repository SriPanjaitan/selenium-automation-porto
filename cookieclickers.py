# Import library selenium untuk automation browser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# Digunakan untuk mencari element (ID, XPATH, dll)
from selenium.webdriver.common.by import By
# Digunakan untuk menunggu element muncul (dynamic loading)
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Membuka browser Chrome
driver = webdriver.Chrome()
# Membuka website Cookie Clicker
driver.get("https://orteil.dashnet.org/cookieclicker/")

# Menyimpan ID element penting di dalam variable
cookie_id = "bigCookie"
cookies_id = "cookies"
product_price_prefix = "productPrice"
product_prefix = "product"

# Menunggu sampai tombol "English" muncul (karena website load dynamic)
WebDriverWait(driver,5).until(
    EC.presence_of_element_located((By.XPATH,"//*[contains(text(),'English')]"))
)
# Klik tombol bahasa English
language = driver.find_element(By.XPATH,"//*[contains(text(),'English')]")
language.click()

# Menunggu sampai cookie besar muncul
WebDriverWait(driver,5).until(
    EC.presence_of_element_located((By.ID, cookie_id))
)
# Ambil element cookie besar
cookie = driver.find_element(By.ID, cookie_id)
#click untuk memulai game
cookie.click()
# Tunggu 10 detik agar game stabil / load
time.sleep(10)

# Loop tanpa henti (bot jalan terus)
while True:
    # Klik cookie (ini inti dari game)
    cookie.click()
    # Ambil jumlah cookies yang dimiliki (text)
    cookies_count = driver.find_element(By.ID, cookies_id).text.split (" ")[0]
    # Hapus koma lalu ubah ke integer
    cookies_count = int(cookies_count.replace(",",""))

    # Loop untuk cek 4 upgrade pertama
    for i in range(4):
        # Ambil harga produk (upgrade)
        product_price = driver.find_element(By.ID, product_price_prefix + str(i)).text.replace(",","")
        
        # Kalau bukan angka (misalnya kosong), skip
        if not product_price.isdigit():
            continue
        # Ubah harga ke integer
        product_price = int(product_price)

        if cookies_count >= product_price:
            product = driver.find_element(By.ID,product_prefix + str(i))
            product.click()
            break
