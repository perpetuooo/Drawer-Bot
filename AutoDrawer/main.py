from browser import img_search
from painter import draw

import customtkinter as ctk
import threading
import time

window = ctk.CTk()
window.title("AutoDrawer")
window.attributes('-topmost', True)
window.iconbitmap('')
window.minsize(300, 425)
window.maxsize(600, 850)

display_width = window.winfo_screenwidth()
display_height = window.winfo_screenheight()







#displaying the program in the center of the screen.
left = int(display_width / 2 - 600 / 2 )
top = int(display_height / 2 - 850 / 2)
window.geometry(f'600x850+{left}+{top}')

#window.bind('<Escape>', lambda event: window.quit())
window.mainloop()

"""
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
    window.after(0, lambda: text_insert(result, widget))
    time.sleep(1)

    threading_drawer()
"""