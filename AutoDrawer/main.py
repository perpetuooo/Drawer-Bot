from subprocess import call

from browser import img_search
from resources import utils

import keyboard
import argparse
import cmd2
import os

class CLI(cmd2.Cmd):
    prompt = 'AD >> '
    intro = "Simple CLI"

    #def do_help(self, line):

    
    def precmd(self, line):
        return line

    
    def do_start(self, line):
        print(f"searching for {line} images...")
        img_search(line, CLI.default_path)


    def do_clear(self, line):
        _ = call('clear' if os.name == 'posix' else 'cls')


    def do_quit(self, line):
        return True
    
    do_exit = do_quit
    


if __name__ == '__main__':
    CLI().cmdloop()