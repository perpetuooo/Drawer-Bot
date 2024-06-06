import numpy as np
import pyautogui
import keyboard
import cv2
import sys


def draw(path):

    #image manipulation to get the drawing contour.
    def img_manipulation(img):
        img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #<-- turns the color image to grayscale.
        img_blur = cv2.GaussianBlur(img_grey, (7, 7), 0) #<-- smoothes the image to reduce its noise.
        img_thresh = cv2.adaptiveThreshold(img_blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2) #<-- image binarization to obtain its contour.
        img_erosion = cv2.erode(img_thresh, kernel, iterations=1) #<-- fills the gaps in the contour by increasing its thickness.
        img_done = 255 - img_erosion #<-- inverts the image colors.

        return img_done


    #finding the end of the drawing.
    def check_ending(row, start_x):
        for x in range(start_x, width):
             if contour[row, x] == 0:
                return x
            
        return None
    
         
    try:
        img = cv2.resize(cv2.imread(str(path)), (400, 400), interpolation=cv2.INTER_LINEAR)
        kernel = np.ones((3, 3), np.uint8)
        pyautogui.PAUSE = 0.01

        print(f"\npress 'enter' to start drawing...")
        keyboard.wait('enter')

        height, width, _ = img.shape   
        initial_x, initial_y = pyautogui.position()
        contour = img_manipulation(img)

        #going through every pixel checking if there's anything to draw.
        for y in range(height):
            x = 0

            while x < width:
                if contour[y, x] != 0:
                    start_x = x
                    pyautogui.moveTo(x + initial_x, y + initial_y)

                    end_x = check_ending(y, start_x)

                    if end_x:
                        pyautogui.dragTo(end_x + initial_x, y + initial_y, button="left")
                        x = end_x
                    
                    else: break
                
                x += 1

            if keyboard.is_pressed('esc'):
                sys.exit()

    except Exception as e:
            print(f"error: {str(e)}")



if __name__ == "__main__":
    draw("C:/Users/pedro/Desktop/penguim.jpg")
    