import settings as stg
import importlib
import pyautogui
import cv2
import os



def draw():

    importlib.reload(stg)
    image_path = f"{os.path.join((os.path.expanduser('~')), 'Pictures')}\{stg.img_name}.jpg"

    canvasX = 825
    canvasY = 525
    resizeX = 150
    resizeY = 150

    img = cv2.imread(image_path)
    img = cv2.resize(img, (resizeX, resizeY), interpolation=cv2.INTER_LINEAR)
    height, width, _ = img.shape

    pyautogui.PAUSE = 0.001
    pyautogui.moveTo(canvasX, canvasY)

    for y in range(height):
        for x in range(width):
            pixel_color = img[y, x]
            r, g, b = pixel_color

            if (r, g, b) != (255, 255, 255):
                pyautogui.moveTo(canvasX + x, canvasY + y)
                pyautogui.click(button='left')

if __name__ == "__main__":
    pass
