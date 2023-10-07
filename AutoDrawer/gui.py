import customtkinter as ctk

ctk.set_appearance_mode('System')
ctk.set_default_color_theme('blue')
root = ctk.CTk()
root.title("AutoDrawer")
root.geometry('800x650')

def text_insert(txt):
    pass


frame = ctk.CTkFrame(master=root, corner_radius=0)
frame.pack(pady=10, padx=10, fill= 'both', expand=True)
#frame.grid(row=0, column=0, sticky='nwes', pady=10, padx=10)

sidebar_frame = ctk.CTkFrame(master=frame, width=150, corner_radius=0)
sidebar_frame.pack(side='left', fill='y')
sidebar_frame.pack_propagate(False)

output_box = ctk.CTkTextbox(master=frame,) #state='disabled'
output_box.pack(pady=10, padx=10, fill='both', expand=True)
output_box.insert('end', "Aute deserunt dolore labore sit magna consequat sunt velit est nulla exercitation dolor amet.")

search_entry = ctk.CTkEntry(master=frame, height=30, placeholder_text='Search')
search_entry.pack(pady=10, padx=10, side='bottom', fill='x')


root.mainloop()