from selenium import webdriver
from bs4 import BeautifulSoup
from PIL import Image
import io
import time
import random
import psutil
import requests

driver = None

def detect_browser():

    for process in psutil.process_iter(attrs=['pid', 'name']):
        try:
            if "chrome" in process.info['name'].lower():
                options = webdriver.ChromeOptions()
                options.add_argument("headless")
                options.add_argument("--log-level=3")
                driver = webdriver.Chrome(options=options)
                break
            elif "firefox" in process.info['name'].lower():
                options = webdriver.FirefoxOptions()
                options.add_argument('-headless')
                options.add_argument("--log-level=error")
                driver = webdriver.Firefox(options=options)
                break
            elif "msedge" in process.info['name'].lower():
                options = webdriver.EdgeOptions()
                options.use_chromium = True
                options.add_argument("headless")
                options.add_argument("--log-level=3")
                driver = webdriver.Edge(options=options)
                break
        
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    return driver

def img_download(url, filename):
    try:
        download_path = r'C:\\Users\\pedro\\Desktop\\imgs\\'
        img_content = requests.get(url).content
        img_file = io.BytesIO(img_content)
        pil = Image.open(img_file)

        if pil.mode == 'P':
            pil = pil.convert('RGB')

        file_path = download_path + filename

        with open(file_path, 'wb') as f:
            pil.save(f, 'JPEG')

    except Exception as e:
        print("ERROR: ", str(e))

search = input("Pesquisar // Search: ")

driver = detect_browser()
driver.get(f'https:/www.google.com/search?tbm=isch&q= {search} clipart')
time.sleep(0.5)

try:
    img_urls = []

    for i in range(2):
        driver.execute_script("window.scrollBy(0, 1000)")

    time.sleep(1)
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')
    img_elements = soup.find_all('img', class_='rg_i')

    for img in img_elements:
        img_src = img.get('src')
        
        if img_src and img_src.startswith('http'):
            img_urls.append(img_src)

    rnd_img = img_urls[random.randint(0, len(img_urls) - 1)]
    print(f"{len(img_urls)} imagens encontradas // images found.")
    print(f"URL: {rnd_img}")

except Exception as e:
    print("ERROR: ", str(e))

finally:
    img_download(rnd_img, "imagem.jpg")
    driver.quit()
