#************************************************************
#   Module:     frontend.cli.interface_dashboard (PocketA)  *
#   Author:     Scavenger4208                               *
#   Version:    0.0.1                                       *
#************************************************************

#===== Imports

import inquirer
from frontend.cli.interface import Interface

#===== defs and classes

class UI_Dashboard(Interface):

    def __init__(self, title: str):
        self.title = title
#--- end def __init__(self, title)

    def dashboard(self):
        '''
        runs the main dashboard interface.
        '''
        self.clear_screen()
        print('#========================================#')
        print('#               Dashboard                #')
        print('#                 Main                   #')
        print('#                                        #')
        print('#========================================#')
        print('')

        q = [
                inquirer.List(
                    'dashboard',
                    message = 'What kind of task do you want us to manage?',
                    choices = [
                        'Planning and organizing',
                        'Documents',
                        'People',
                        'Network',
                        'Exit'
                        ]
                    )
                ]

        a = inquirer.prompt(q)
        print(a['dashboard'])

        # create for each choice for new ui defs
        if a['dashboard'] == 'Planning and organizing':
            self.ui_planning()
        elif a['dashboard'] == 'Documents':
            self.ui_documents()
        elif a['dashboard'] == 'People':
            self.ui_people()
        elif a['dashboard'] == 'Network':
            self.ui_network()
        elif a['dashboard'] == 'Exit':
            self._exit()
#--- end def dashboard(self)

    def ui_planning(self):
        self.clear_screen()
        print('#========================================#')
        print('#               Dashboard                #')
        print('#         Planning & Organizing          #')
        print('#                                        #')
        print('#========================================#')
        print('')

        q = [
               inquirer.List(
                   'planning',
                   message = 'Choose planning tool',
                   choices = [
                       'To-Do-List',
                       'Weekplan',
                       '90-day-plan',
                       '5-yearplpan',
                       'Calendar',
                       'Projectmanagement',
                       'Back to dashboard',
                       'Exit PocketA'
                       ]
                   )
               ]

        a = inquirer.prompt(q)
        print(a['planning'])

        if a['planning'] == 'To-Do-List':
              self.ui_todolist()
        elif a['planning'] == 'Weekplan':
              self.ui_weekplan()
        elif a['planning'] == '90-day-plan':
              self.ui_90dayplan()
        elif a['planning'] == '5-yearplan':
              self.ui_fiveyearplan()
        elif a['planning'] == 'Calendar':
              self.ui_calendar()
        elif a['planning'] == 'Projectmanager':
              self.ui_projectmanager()
        elif a['planning'] == 'Back to dashboard':
              self.dashboard()
        elif a['planning'] == 'Exit PocketA':
              self._exit()
#--- end def ui_planning(self)

    def ui_todolist(self):
        pass

    def ui_weekplan(self):
        pass

    def ui_90dayplan(self):
        pass

    def ui_fiveyearplan(self):
        pass

    def ui_projectmanager(self):
        pass

    def ui_documents(self):
        self.clear_screen()
        print('#========================================#')
        print('#               Dashboard                #')
        print('#               Documents                #')
        print('#                                        #')
        print('#========================================#')
        print('')


        q = [
               inquirer.List(
                   'documents',
                   choices = [
                       'Writer',
                       'Spreadsheet',
                       'Presentation',
                       'Back to dashboard',
                       'Exit PocketA'
                       ]
                   )
               ]

        a = inquirer.prompt(q)
        print(a['documents'])

        if a['documents'] == 'Writer':
              self.writer()
        elif a['documents'] == 'Spreadsheet':
              self.spreadsheet()
        elif a['documents'] == 'Presentation':
              self.presentation()
        elif a['documents'] == 'Back to dashboard':
              self.dashboard()
        elif a['documents'] == 'Exit PocketA':
              self._exit()

    def writer(self):
        pass

    def spreadsheet(self):
        pass

    def presentation(self):
        pass

    def ui_people(self):
        self.clear_screen()
        print('#========================================#')
        print('#               Dashboard                #')
        print('#                People                  #')
        print('#                                        #')
        print('#========================================#')
        print('')

        q = [
            inquirer.List(

                'people',
                message = 'Specify the task',
                choices = [
                    'Addressbook',
                    'Run Caesars Assistant',
                    'Back to dashboard',
                    'Exit PocketA'
                    ]
                )
            ]

        a = inquirer.prompt(q)
        print(a['people'])

        if a['people'] == 'Addressbook':
              self.ui_addressbook()
        elif a['people'] == 'Run Caesars Assistant':
              self.caesar()
        elif a['people'] == 'Back to dashboard':
              self.dashboard()
        elif a['people'] == 'Exit PocketA':
              self._exit()


    def ui_addressbook(self):
        pass
    
    def caesar(self):
        pass

    def ui_network(self):
        self.clear_screen()
        print('#========================================#')
        print('#               Dashboard                #')
        print('#                Network                 #')
        print('#                                        #')
        print('#========================================#')
        print('')

        q = [
                inquirer.List(
                    'network',
                    message = 'Choose task',
                    choices = [
                        'ip',
                        'Back to dashboard',
                        'Exit PocketA'
                        ]
                    )
                ]

        a = inquirer.prompt(q)
        print(a['network'])

        if a['network'] == 'ip':
            self.ip()
        elif a['network'] == 'Back to dashboard':
              self.dashboard()
        elif a['network'] == 'Exit PocketA':
              self._exit()

    def ip(self):
        pass
