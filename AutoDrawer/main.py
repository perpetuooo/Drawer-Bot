from subprocess import call

from browser import img_search
from resources import utils

import keyboard
import argparse
import cmd2
import sys
import os

class CLI(cmd2.Cmd):
    prompt = 'AD >> '
    intro = "Simple CLI"

    
    def __init__(self):
        super().__init__()

        self.last_keyword = None
        self.add_settable(cmd2.Settable('last_keyword', str, 'last keyword', self))


    def do_search(self, line):
        '''given a keyword, search and donwload an equivalent image'''
        print(f"searching for {line} images...")
        img_search(line, CLI.default_path)


    def do_load(self, line):
        ''''''
        print(self.last_keyword)
        self.last_keyword = "whale"
        print(self.last_keyword)


    def do_start(self, line):
        ''''''
        pass


    def do_clear(self, line):
        '''clear'''
        _ = call('clear' if os.name == 'posix' else 'cls')


    def do_quit(self, line):
        return True
    
    do_exit = do_quit
    


if __name__ == '__main__':
    c = CLI()
    sys.exit(c.cmdloop())