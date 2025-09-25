#************************************
#   Module:     main.py (PocketA)   *
#   Author:     Scavenger4208       *
#   Version:    0.0.1               *
#************************************

#=== Imports

from frontend.cli.interface import Interface

#=== classes and defs

def main():
    interface = Interface("main")
    print(type(interface))
    print(f'interface_title: {interface.title}')

#=== main program

if __name__ == "__main__":
    main()
