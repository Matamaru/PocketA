#****************************************************
#   Module:     frontent.cli.interface.py (PocketA) *
#   Author:     Scavenger4208                       *
#   Version:    0.0.1                               *
#****************************************************

#=== Imports

import inquirer
import platform
import os
import sys

#===

class Interface():
    def __init__(self, title: str):
        self.title = title

    def clear_screen(self):
        '''
        Clears the screen for any main OS
        '''
        cur_system = platform.system()
        if cur_system == 'Windows':
            os.system('cls')
        else:
            os.system('clear')

    def display_title_bar(self):
        '''
        Displays the title name of the Interface instance.
        '''
        print((len(self.title) + 10) * "*")
        print(f'***   {self.title}   ***')
        print(len((self.title) + 10) * "*")

    def _exit(self):
        '''
        Exits the CLI. 
        '''
        self.clear_screen()
        sys.exit()



