from termcolor import cprint, colored
from settings import stg
import pyautogui
import keyboard
import cv2
import numpy as np

def draw():
    print(f"\nComeçando... // Starting...\n(Pressione {stg.esc} para interromper o desenho // Press {stg.esc} to stop the drawer)")

    #values for testing only.
    resizeX = 500
    resizeY = 500
    kernel = np.ones((3, 3), np.uint8)
    pyautogui.PAUSE = 0.001

    #image manipulation.
    img = cv2.resize(cv2.imread(str(stg.file_path)), (resizeX, resizeY), interpolation=cv2.INTER_LINEAR) #Altera o tamanho da imagem.
    img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #Transforma a imagem em cores para cinza.
    img_blur = cv2.GaussianBlur(img_grey, (7, 7), 0) #Suaviza a imagem para reduzir seu ruído.
    img_thresh = cv2.adaptiveThreshold(img_blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2) #Binarização da imagem para obter seu contono.
    img_erosion = cv2.erode(img_thresh, kernel, iterations=1) #Aumenta a expessura da imagem e preenche lacunas entre os contornos.
    img_done = 255 - img_erosion #Inverte as cores da imagem.
    height, width, _ = img.shape

    #goes through every pixel checking if theres anything to draw. 
    for y in range(height):
        for x in range(width):
            if img_done[y, x] != 0:
                abs_x = stg.canvas_up[0] + (stg.canvas_down[0] - stg.canvas_up[0]) / 2 - width / 2 + x
                abs_y = stg.canvas_up[1] + (stg.canvas_down[1] - stg.canvas_up[1]) / 2 - height / 2 + y

                pyautogui.moveTo(abs_x, abs_y)
                pyautogui.click(button='left')

            if keyboard.is_pressed('esc'):
                cprint("Desenho interrompido... // Drawing interrupted...", "red")
                return
    
    print("Desenho finalizado! // Drawing completed!")

if __name__ == "__main__":
    pass
