from browser import img_search
from pyautogui import position
from settings import stg
from drawer import draw
import customtkinter as ctk
import webbrowser
import threading
import winsound
import time

root = ctk.CTk()
root.title("AutoDrawer")
root.geometry('950x650')
ctk.set_appearance_mode('Dark')
ctk.set_default_color_theme('blue')


#theme changer
def change_theme(new_theme):
    ctk.set_appearance_mode(new_theme)


#opening the project repository
def open_repo():
    try:
     webbrowser.open('https://github.com/perpetuooo/Drawer-Bot')
     
    except Exception:
        pass


#configuring the canvas
def canvas_config():

    def get_x_position():
        stg.canvasX = position()
        text_insert("Canvas Ready!", output_box)
        canvas_label.configure(text=f"X = {stg.canvasX.x}px   Y = {stg.canvasY.y}px")
        root.unbind("<Shift_L>")
        root.unbind("<Shift_R>")
        root.bind("<Return>", lambda e: threading_search())
        search_button.configure(state='normal')

    def get_y_position():
        stg.canvasY = position()
        text_insert("Press SHIFT in the bottom right corner", output_box)
        root.bind("<Shift_L>", lambda e: get_x_position())
        root.bind("<Shift_R>", lambda e: get_x_position())

    text_insert("\nPress SHIFT in the upper left corner", output_box)
    root.bind("<Shift_L>", lambda e: get_y_position())
    root.bind("<Shift_R>", lambda e: get_y_position())


#creating another thread to perform the image scrapping
def threading_search():
    keyword = search_entry.get()
    text_insert(f"\nSearching for {keyword} images...", output_box)
    search_thread = threading.Thread(target=search_keyword, args=(keyword, output_box))
    search_thread.start()


#creating another thread to execute the drawer
def threading_drawer():
    text_insert("\nStarting...\n(Press ESC to stop the drawer.)", output_box)
    draw_thread = threading.Thread(target=drawer, args=(output_box,))
    draw_thread.start()


#calling the img_search function and updating the textbox
def search_keyword(keyword, widget):
    result = img_search(keyword)
    root.after(0, lambda: text_insert(result, widget))
    time.sleep(1)

    if not stg.file_path:
        text_insert("( - ) ERROR.", widget)
        return
    
    else:
        #beeps before the drawer starts
        winsound.Beep(800, 400)
        time.sleep(0.5)
        winsound.Beep(800, 400)
        time.sleep(0.5)
        winsound.Beep(1600, 1000)

        threading_drawer()


#calling the draw function and updating the textbox
def drawer(widget):
    result = draw()
    root.after(0, lambda: text_insert(result, widget))


#inserting text into the output_box
def text_insert(txt, widget):
    widget.configure(state='normal')
    widget.insert('end', f"\n{txt}")
    widget.configure(state='disabled')


#GUI
frame = ctk.CTkFrame(master=root, corner_radius=0)
frame.pack(pady=10, padx=10, fill= 'both', expand=True)

sidebar_frame = ctk.CTkFrame(master=frame, width=190, corner_radius=0)
sidebar_frame.pack(side='left', fill='y')
sidebar_frame.pack_propagate(False)

title_text = ctk.CTkLabel(master=sidebar_frame, text="AutoDrawer", font=("Roboto", 28, 'bold'), cursor='hand2')
title_text.pack(pady=15, padx=15, side='top')
title_text.bind("<Button-1>", command=lambda e: open_repo())

theme_option = ctk.CTkOptionMenu(sidebar_frame, values=["Dark", "Light"], command=change_theme)
theme_option.pack(pady=15, padx=10, side='bottom')

output_box = ctk.CTkTextbox(master=frame) 
output_box.pack(pady=10, padx=10, fill='both', expand=True)
output_box.insert('end', "Ready!.")
output_box.configure(state='disabled')

canvas_label = ctk.CTkLabel(master=frame, text="X = ?   Y = ?", cursor='hand2')
canvas_label.pack(pady=0, padx=15, side='top', anchor='w')
canvas_label.bind("<Button-1>", lambda e: canvas_config())

search_entry = ctk.CTkEntry(master=frame, height=30, placeholder_text='Keyword')
search_entry.pack(pady=10, padx=10, side='left', anchor='w', fill='x', expand=True)

search_button = ctk.CTkButton(master=frame, text="Search",
                               fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), cursor='hand2', command=lambda:threading_search())
search_button.pack(pady=10, padx=10, side='right', anchor='e')
search_button.configure(state='disabled')   


root.mainloop()