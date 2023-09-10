from pathlib import Path
import datetime

class Config():
    date = datetime.datetime.now().strftime("%d-%m-%y %H.%M.%S")
    imgs_path = Path.home() / "Pictures"/ "src"
    if not imgs_path.exists:
        imgs_path.mkdir(parents=True)

    file_path = None
    canvas_up = None
    canvas_down = None

stg = Config()
