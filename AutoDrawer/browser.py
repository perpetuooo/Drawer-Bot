from selenium import webdriver
from settings import stg
from PIL import Image
import io
import re
import os
import time
import random
import psutil
import requests


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
            elif "safari" in process.info['name'].lower():
                options = webdriver.SafariOptions()
                options.add_argument("headless")
                options.add_argument("--log-level=3")
                driver = webdriver.Safari(options=options)
                break
        
        except Exception as e:
            break

    return driver


#chooses a random image and tries to download it.
def img_download(img, file_name): 
    try:
        if not os.path.exists(stg.imgs_path):
            os.makedirs(stg.imgs_path)

        img_content = requests.get(img).content
        img_file = io.BytesIO(img_content)
        stg.file_path = stg.imgs_path / file_name
        pil = Image.open(img_file)

        if pil.mode == 'P':
            pil = pil.convert('RGB')

        with open(stg.file_path, 'wb') as f:
            pil.save(f, 'JPEG', quality=95)

    #retrying the download function in case of errors.
    except Exception as e:
        max_retries = 5
        retry_count = 0

        while retry_count <= max_retries:
            try:
                img_download(img, file_name)
                break

            except Exception as e:
                retry_count += 1

        else:
            return("( ! ) Something went wrong, try again.")


#image scrapping through Google Images.
def img_search(keyword):
    try:
        stg.file_path = None
        driver = detect_browser()
        driver.get(f'https:/www.google.com/search?tbm=isch&q= {keyword} clipart')
        time.sleep(0.5)

        img_urls = []
        img_name = f"{keyword} {stg.img_date}"
        page_source = driver.page_source

        #finding all URLs that are images and putting them in the list.
        regex = r'"(https://[^"]+\.(jpg|jpeg))",(\d+),(\d+)'
        matches = re.findall(regex, page_source)

        for url in matches:
            url = url[0]
            img_urls.append(url)
        
        if img_urls:
            rnd_img = random.choice(img_urls) 
            img_download(rnd_img, f"{img_name}.jpg")

        else:
            return ("( ! ) No images found, try again\n")
    
    except Exception as e:
        return (f"( - ) ERROR: {str(e)}")

    finally:
        driver.quit()
        return (f"{len(img_urls)} images were found!\nChoosen image --> {rnd_img}")



if __name__ == '__main__':
    pass