from pathlib import Path
from subprocess import call

from browser import img_search
from resources import utils

import cmd
import os

class CLI(cmd.Cmd):
    prompt = 'AD >> '
    intro = "Simple CLI" #utils.intro()

    last_keyword = None
    default_path = Path.home() / "Pictures" / "AutoDrawer"

    #def do_help(self, line):

    
    def precmd(self, line):
        return line

    
    def do_start(self, line):
        print(f"searching for {line} images...")
        img_search(line, CLI.default_path)


    def do_clear(self, line):
        _ = call('clear' if os.name == 'posix' else 'cls')


    def do_exit(self, line):
        return True
    


if __name__ == '__main__':
    CLI().cmdloop()