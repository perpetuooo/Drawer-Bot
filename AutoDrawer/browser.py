from selenium import webdriver
from settings import stg
from PIL import Image
import io
import re
import os
import art
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
            print(f"(-) ERROR: {str(e)}")
            print("Pressione CTRL+C para sair do programa // Press CTRL+C to exit the program")
            keyboard.wait('ctrl+c')
            exit(1)

    return driver


#chooses a random image and tries to download it.
def img_download(img_list, file_name): 
    try:
        if not os.path.exists(stg.imgs_path):
            os.makedirs(stg.imgs_path)

        rnd_img = random.choice(img_list)
        print(f"Imagem escolhida // Choosen image --> {rnd_img}")

        img_content = requests.get(rnd_img).content
        img_file = io.BytesIO(img_content)
        stg.file_path = stg.imgs_path / file_name
        pil = Image.open(img_file)

        if pil.mode == 'P':
            pil = pil.convert('RGB')

        with open(stg.file_path, 'wb') as f:
            pil.save(f, 'JPEG', quality=95)
            print(stg.file_path)

    #retrying the download function in case of errors.
    except Exception as e:
        print('\n')
        print(f"(-) ERROR: {str(e)}")
        max_retries = 5
        retry_count = 0

        while retry_count <= max_retries:
            try:
                rnd_img = random.choice(img_list)
                print(f"Imagem escolhida // Choosen image --> {rnd_img}")
                img_download(img_list, file_name)
                break

            except Exception as e:
                print('\n')
                print(f"(-) ERROR: {str(e)}")
                retry_count += 1

        else:
            print("(!) Alguma coisa deu errado // Something went wrong")
            print("Pressione CTRL+C para sair do programa // Press CTRL+C to exit the program")
            keyboard.wait('ctrl+c')
            exit(1)


#image scrapping through Google Images.
def img_search():
    try:
        keyword = input("Pesquisar // Search: ")
        driver = detect_browser()
        driver.get(f'https:/www.google.com/search?tbm=isch&q= {keyword} clipart')
        time.sleep(0.5)

        img_urls = []
        img_name = f"{keyword} {stg.date}"
        page_source = driver.page_source

        #finding all URLs that are images and putting them in the list.
        regex = r'"(https://[^"]+\.(jpg|jpeg))",(\d+),(\d+)'
        matches = re.findall(regex, page_source)

        for url in matches:
            url = url[0]
            img_urls.append(url)
        
        if img_urls:
            print(f"{len(img_urls)} imagens encontradas // images found")
            img_download(img_urls, f"{img_name}.jpg")

        else:
            print("(!) Nenhuma imagem encontrada, tente novamente // No images found, try again\n")
            img_search()
    
    except Exception as e:
        print(f"(-) ERROR: {str(e)}")

    finally:
        driver.quit()
        drawer.draw() 
        menu_state = False  
        
        #menu loop.
        while True:
            if not menu_state:
                print(f"Para desenhar outro(a) {keyword}, pressione SHIFT + F1 // To draw another {keyword}, press SHIFT + F1")
                print(f"Para pesquisar outra palavra, pressione SHIFT + F2 // To search another word, press SHIFT + F2")
                print(f"Para sair do programa, pressione SHIFT + ESC // To exit the program, press SHIFT + ESC")
                menu_state = True

            if keyboard.is_pressed('shift + f1'):
                print('\n')
                img_name = f"{keyword} {stg.date}"
                img_download(img_urls, f"{img_name}.jpg")
                drawer.draw()
                menu_state = False
                
            elif keyboard.is_pressed('shift + f2'):
                print('\n')
                img_search()

            elif keyboard.is_pressed('shift + esc'):
                exit(0)


art.tprint("Auto Drawer")
print("https://github.com/perpetuooo\n")

#canvas configuration.
print(f"Pressione SHIFT no canto superior esquerdo // Press SHIFT in the upper left corner")
keyboard.wait('shift')
stg.canvas_up = pyautogui.position()
time.sleep(0.3)
print(f"Pressione SHIFT no canto inferior direito // Press SHIFT in the bottom right corner")
keyboard.wait('shift')
stg.canvas_down = pyautogui.position()
time.sleep(0.3)
print("Posição do Canvas configurada // Canvas position configured")
print("\nx=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x\n")

img_search()
    