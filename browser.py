from selenium import webdriver
from bs4 import BeautifulSoup
import time
import random
import psutil

def detect_browser():
    browser = None

    for process in psutil.process_iter(attrs=['pid', 'name']):
        try:
            if "chrome" in process.info['name'].lower():
                browser = "chrome"
                break
            elif "firefox" in process.info['name'].lower():
                browser = "firefox"
                break
            elif "msedge" in process.info['name'].lower():
                browser = "edge"
                break
        
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    return browser

search = input("Pesquisar: ")
search = f"{search} clipart"

default_browser = detect_browser()

if default_browser == "chrome":
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    options.add_argument("--log-level=3")
    driver = webdriver.Chrome(options=options)
    
elif default_browser == "firefox":
    options = webdriver.FirefoxOptions()
    options.add_argument('-headless')
    options.add_argument("--log-level=error")
    driver = webdriver.Firefox(options=options)

elif default_browser == "edge":
    options = webdriver.EdgeOptions()
    options.use_chromium = True
    options.add_argument("headless")
    options.add_argument("--log-level=3")
    driver = webdriver.Edge(options=options)

else: 
    print("Navegador não suportado.")

driver.get('https://www.google.com/search?tbm=isch&q='+ search)
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

    print(f"{len(img_urls)} imagens encontradas")
    rnd_img = random.randint(0, len(img_urls) - 1)
    print(f"URL: {img_urls[rnd_img]}")

except Exception as e:
    print("ERROR: ", str(e))

finally:
    driver.quit()
