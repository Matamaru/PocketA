#************************************************************
#   Module:     frontend.cli.interface_entrance (PocketA)   *
#   Author:     Scavenger4208                               *
#   Version:    0.0.1                                       *
#************************************************************

#=== Imports

from frontend.cli.interface import Interface

#=== defs and classes

class UI_Entrance(Interface):
    def __init__(self, title):
        self.title = title

    def entrance(self):
        q = [
                inquirer.List(
                    'entrance',
                    message='Login or exit?',
                    choices=['Login', 'Exit']
                    )
                ]
        a = inquirer.prompt(q)

        if a['entrance'] == 'Login':
            self._login()
        elif a['entrance'] == 'Exit':
            self._exit()

    def _login(self):
        self.clear_screen()
        print('Login')
