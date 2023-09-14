from termcolor import cprint, colored
from selenium import webdriver
from settings import stg
from PIL import Image
import io
import re
import time
import random
import psutil
import drawer
import requests
import keyboard
import pyautogui

#detecting the users browser and adjusting its settings
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
        
        except Exception as e:
            cprint(f"ERROR: {str(e)}", "red")

    return driver


def img_download(url, filename):
    try:
        img_content = requests.get(url).content
        img_file = io.BytesIO(img_content)
        stg.file_path = stg.imgs_path / filename
        pil = Image.open(img_file)

        if pil.mode == 'P':
            pil = pil.convert('RGB')

        with open(stg.file_path, 'wb') as f:
            pil.save(f, 'JPEG', quality=95)

    except Exception as e:
        cprint(f"ERROR: {str(e)}", "red")


def img_search(keyword):
    try:
        driver = detect_browser()
        driver.get(f'https:/www.google.com/search?tbm=isch&q= {keyword} clipart')
        time.sleep(0.5)

        img_urls = []
        img_name = f"{search} {stg.date}"
        max_retries = 5
        page_source = driver.page_source

        #loading more images by scrolling down the page
        driver.execute_script("window.scrollBy(0, 1000)")
        time.sleep(0.5)

        #finding all URLs that are images jpg, jpeg or png
        regex = r'"(https://[^"]+\.(jpg|jpeg|png))",(\d+),(\d+)'
        matches = re.findall(regex, page_source)

        for url in matches:
            url = url[0]
            img_urls.append(url)
        
        if img_urls:
            rnd_img = random.choice(img_urls)
            print(colored(f'{len(img_urls)}', 'yellow'), "imagens encontradas // images found.")
            print(f"URL: {rnd_img}")
            img_download(rnd_img, f"{img_name}.jpg")

        else:
            print("Nenhuma imagem encontrada // No images found.")
    
    #retrying the download function in case of errors
    except Exception as e:
        cprint(f"ERROR: {str(e)}", "red")
        retry_count = 0
        while retry_count <= max_retries:
            try:
                rnd_img = random.choice(img_urls)
                print(f"URL: {rnd_img}")
                img_download(rnd_img, f"{img_name}.jpg")
                break

            except Exception as e:
                cprint(f"ERROR: {str(e)}", "red")
                retry_count += 1

        else:
            print("Alguma coisa deu errado, reinicie o programa. // Something went wrong, restart the program.")

    finally:
        driver.quit()
        img_download(rnd_img, f"{img_name}.jpg")
        drawer.draw()


print("Pressione SHIFT no canto superior esquerdo // Press SHIFT in the upper left corner.")
keyboard.wait('shift')
stg.canvas_up = pyautogui.position()
time.sleep(0.3)
print("Pressione SHIFT no canto inferior direito // Press SHIFT in the bottom right corner.")
keyboard.wait('shift')
stg.canvas_down = pyautogui.position()
time.sleep(0.3)
print("Posição do Canvas configurada // Canvas position configured.")
cprint("\nx=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x\n", attrs=["bold", "dark"])

search = input("Pesquisar // Search: ")
img_search(search)
