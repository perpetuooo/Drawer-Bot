from pathlib import Path
import datetime

#configuration of global variables.
class Config():
    img_date = datetime.datetime.now().strftime("%d-%m-%y %H.%M.%S")
    imgs_path = Path.home() / "Pictures" / "AutoDrawer"

    file_path = None
    canvasY = None
    canvasX = None

stg = Config()
