#************************************
#   Module:     main.py (PocketA)   *
#   Author:     Scavenger4208       *
#   Version:    0.0.1               *
#************************************

#=== Imports

from frontend.cli.interface_entrance import UI_Entrance
from frontend.cli.interface_dashboard import UI_Dashboard
from backend.datamodule.config import config_db
from backend.datamodule.datamodule import DataBase
from backend.api.config import config_api

#=== classes and defs

def main():
	
    # get db_params from ENV
	db_params = config_db()

    # Connect to database
	db = DataBase(db_params)
	db.connect()
	db.check_conn()
	db.close_conn()

	# get api_params from ENV
	api_params = config_api()
	print(api_params)


#    # create ui instances
#    ui_entrance = UI_Entrance('PocketA') # use later for user login
#    # only registered users are granted access to dashboard
#    ui_dashboard = UI_Dashboard('PocketA')
#
#    # call dashboard
#    ui_dashboard.dashboard()
    
#=== main program

if __name__ == "__main__":
    main()
