from termcolor import colored 
from pathlib import Path
import datetime

#configuration of global variables.
class Config():
    date = datetime.datetime.now().strftime("%d-%m-%y %H.%M.%S")
    imgs_path = Path.home() / "Pictures"/ "src"
    if not imgs_path.exists:
        imgs_path.mkdir(parents=True)

    #declaring colored variables here to use them twice in one string (couldnt find another way).
    esc = colored("ESC", "yellow", attrs=["bold"])
    shift = colored("SHIFT", "yellow", attrs=["bold"])
    shift_f1 = colored("SHIFT + F1", "yellow", attrs=["bold"])
    shift_f2 = colored("SHIFT + F2", "yellow", attrs=["bold"])
    shift_esc = colored("SHIFT + ESC", "yellow", attrs=["bold"])

    file_path = None
    canvas_up = None
    canvas_down = None

stg = Config()
