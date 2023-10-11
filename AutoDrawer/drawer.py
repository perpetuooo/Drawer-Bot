from settings import stg
import pyautogui
import keyboard
import cv2
import numpy as np

def draw():
    try:
        #values for testing only.
        resizeX = 500
        resizeY = 500
        kernel = np.ones((3, 3), np.uint8)
        pyautogui.PAUSE = 0.001

        #image manipulation.
        img = cv2.resize(cv2.imread(str(stg.file_path)), (resizeX, resizeY), interpolation=cv2.INTER_LINEAR) #<-- changes the image size.
        img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #<-- turns the color image to grayscale.
        img_blur = cv2.GaussianBlur(img_grey, (7, 7), 0) #<-- smoothes the image to reduce its noise.
        img_thresh = cv2.adaptiveThreshold(img_blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2) #<-- image binarization to obtain its contour.
        img_erosion = cv2.erode(img_thresh, kernel, iterations=1) #<-- fills the gaps in the contour by increasing its thickness.
        img_done = 255 - img_erosion #<-- inverts the image colors.
        height, width, _ = img.shape#<-- get height and width from the image.   
        
        #goes through every pixel checking if theres anything to draw. 
        for y in range(height):
            for x in range(width):
                if img_done[y, x] != 0:
                    abs_x = stg.canvasY[0] + (stg.canvasX[0] - stg.canvasY[0]) / 2 - width / 2 + x
                    abs_y = stg.canvasY[1] + (stg.canvasX[1] - stg.canvasY[1]) / 2 - height / 2 + y

                    pyautogui.moveTo(abs_x, abs_y)
                    pyautogui.click(button='left')

                if keyboard.is_pressed('esc'):
                    return ("( ! ) Drawing interrupted.")
        
        return ("Drawing completed!")
                
    except Exception as e:
            return (f"( - ) ERROR: {str(e)}")



if __name__ == "__main__":
    pass
