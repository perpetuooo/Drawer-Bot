from PIL import Image
from pathlib import Path
from datetime import datetime
from selenium import webdriver

import requests
import psutil
import random
import re
import os
import io


#image scrapping through Google Images.
def img_search(keyword, path):

    #detecting the users browser and adjusting its settings
    def detect_browser():
        for process in psutil.process_iter(['name']):
            try:
                match process.info['name'].lower():
                    case "chrome.exe":
                        options = webdriver.ChromeOptions()
                        options.add_argument("headless")
                        options.add_argument("--log-level=3")
                        return webdriver.Chrome(options=options)

                    case "firefox.exe":
                        options = webdriver.FirefoxOptions()
                        options.add_argument('-headless')
                        options.add_argument("--log-level=error")
                        return webdriver.Firefox(options=options)

                    case "msedge.exe":
                        options = webdriver.FirefoxOptions()
                        options.add_argument('-headless')
                        options.add_argument("--log-level=error")
                        return webdriver.Firefox(options=options)

                    case "safari.exe":
                        options = webdriver.SafariOptions()
                        options.add_argument("headless")
                        options.add_argument("--log-level=3")
                        return webdriver.Safari(options=options)
                    
                    case _:
                        pass
            
            except Exception as e:
                print(f"error: {str(e)}")


    #downloading the image.
    def downloader(img, file_path):
            try:
                if not os.path.exists(path):
                    os.makedirs(path)

                img_content = requests.get(img).content
                img_file = io.BytesIO(img_content)
                img_done = Image.open(img_file).convert('RGB')
                img_done.save(file_path, "JPEG", quality=80)
                print("DONE!")

            #retrying the download function in case of errors.
            except Exception as e:
                print(f"download error: {str(e)}")

                max_retries = 3
                retry_count = 0

                while retry_count <= max_retries:
                    try:
                        downloader(img, file_path)
                        break

                    except Exception:
                        retry_count += 1

                else:
                    print("couldnt download...")


    # last_keyword = None
    driver = detect_browser()
    if not driver:
        print("driver not compatible...")
        return

    driver.get(f'https:/www.google.com/search?tbm=isch&q={keyword} clipart')

    results = []
    source = driver.page_source
    regex = r'"(https://[^"]+\.(jpg|jpeg|png))",(\d+),(\d+)'

    matches = re.findall(regex, source)

    for url in matches:
        results.append(url[0])

    if results:
        chosen_img = random.choice(results)
        date = datetime.now().strftime("%d-%m-%y %H.%M.%S")
        img_name = f"{keyword} {date}.jpg"
        file_path = os.path.join(path, img_name)

        downloader(chosen_img, file_path)
    
    else:
        print("no imgs found...")




if __name__ == '__main__':
    img_search("gecko", Path.home() / "Pictures" / "AutoDrawer")