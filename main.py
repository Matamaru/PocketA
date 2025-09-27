#************************************
#   Module:     main.py (PocketA)   *
#   Author:     Scavenger4208       *
#   Version:    0.0.1               *
#************************************

#=== Imports

from frontend.cli.interface_entrance import UI_Entrance
from frontend.cli.interface_dashboard import UI_Dashboard

#=== classes and defs

def main():
    # create ui instances
    ui_entrance = UI_Entrance('PocketA') # use later for user login
    # only registered users are granted access to dashboard
    ui_dashboard = UI_Dashboard('PocketA')

    # call dashboard
    ui_dashboard.dashboard()

#=== main program

if __name__ == "__main__":
    main()
