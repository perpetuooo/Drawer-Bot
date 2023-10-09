from pyautogui import position
import customtkinter as ctk
from settings import stg
import keyboard
import winsound
import time

root = ctk.CTk()
root.title("AutoDrawer")
root.geometry('950x650')
ctk.set_appearance_mode('Dark')
ctk.set_default_color_theme('blue')

toplevel = None


def change_theme(new_theme):
    ctk.set_appearance_mode(new_theme)

def open_repo():
    pass

def open_toplevel():
    global toplevel

    if toplevel is None or not toplevel.winfo_exists():
        toplevel = create_toplevel()

    else:
        toplevel.focus()

def create_toplevel():

    def shift_press():
        keyboard.wait('shift')
        return position()

    toplevel = ctk.CTkToplevel(root)
    toplevel.geometry('400x200')
    toplevel.title("Canvas Config")
    toplevel.lift()

    label1 = ctk.CTkLabel(master=toplevel, text="Shift Y")
    label1.pack()
    stg.canvasY = shift_press()

    label2 = ctk.CTkLabel(master=toplevel, text="Shift X")
    label2.pack()
    stg.canvasX = shift_press()

    return toplevel


frame = ctk.CTkFrame(master=root, corner_radius=0)
frame.pack(pady=10, padx=10, fill= 'both', expand=True)

sidebar_frame = ctk.CTkFrame(master=frame, width=190, corner_radius=0)
sidebar_frame.pack(side='left', fill='y')
sidebar_frame.pack_propagate(False)

title_text = ctk.CTkLabel(master=sidebar_frame, text="AutoDrawer", font=("Roboto", 28, 'bold'), cursor='hand2')
title_text.pack(pady=15, padx=15, side='top')
title_text.bind("<Button-1>", command="")

theme_option = ctk.CTkOptionMenu(sidebar_frame, values=["Dark", "Light"], command=change_theme)
theme_option.pack(pady=15, padx=10, side='bottom')

output_box = ctk.CTkTextbox(master=frame,) #state='disabled'
output_box.pack(pady=10, padx=10, fill='both', expand=True)
output_box.insert('end', "Aute deserunt dolore labore sit magna consequat sunt velit est nulla exercitation dolor amet.")

canvas_label = ctk.CTkLabel(master=frame, text="X = ?, Y = ?", cursor='hand2')
canvas_label.pack(pady=0, padx=15, side='top', anchor='w')
canvas_label.bind("<Button-1>", lambda e: open_toplevel())

search_entry = ctk.CTkEntry(master=frame, height=30, placeholder_text='Keyword')
search_entry.pack(pady=10, padx=10, side='left', anchor='w', fill='x', expand=True)

search_button = ctk.CTkButton(master=frame, text="Search",
                               fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), cursor='hand2', command=lambda:"")
search_button.pack(pady=10, padx=10, side='right', anchor='e')


def text_insert(txt):
    output_box.configure(state='normal')
    output_box.insert('end', f"\n{stg.log_date} {txt}")
    output_box.configure(state='disabled')


root.mainloop()