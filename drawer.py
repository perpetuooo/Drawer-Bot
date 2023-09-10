from settings import stg
import pyautogui
import cv2

def draw():
    path = str(stg.file_path)
    
    #values for testing only.
    resizeX = 500
    resizeY = 500
    pyautogui.PAUSE = 0.001

    img = cv2.imread(path)
    img = cv2.resize(img, (resizeX, resizeY), interpolation=cv2.INTER_LINEAR)
    height, width, _ = img.shape

    for y in range(height):
        for x in range(width):
            abs_x = stg.canvas_up[0] + (stg.canvas_down[0] - stg.canvas_up[0]) / 2 - width / 2 + x
            abs_y = stg.canvas_up[1] + (stg.canvas_down[1] - stg.canvas_up[1]) / 2 - height / 2 + y

            pixel_color = img[y, x]
            r, g, b = pixel_color

            if (r, g, b) == (0, 0, 0):
                pyautogui.moveTo(abs_x, abs_y)
                pyautogui.click(button='left')

if __name__ == "__main__":
    pass
