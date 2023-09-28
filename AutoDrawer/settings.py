from pathlib import Path
import datetime

#configuration of global variables.
class Config():
    date = datetime.datetime.now().strftime("%d-%m-%y %H.%M.%S")
    imgs_path = Path.home() / "Pictures" / "src"

    file_path = None
    canvas_up = None
    canvas_down = None

stg = Config()
