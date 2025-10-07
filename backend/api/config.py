#****************************************************
#		Module:		backend.api.config (PocketA)	*
#		Author:		Scavenger4208					*
#		Version:	0.0.1							*
#****************************************************

#=== Imports

import os
from dotenv import load_dotenv

#=== defs and classes

def config_api():
	# load env variables
	load_dotenv()

	# create dict for flask-api configuration
	params = {}
	
	# load params into dict
	params['debug'] = os.getenv('DEBUG')
	params['secret_key'] = os.getenv('SECRET_KEY')
	params['server_name'] = os.getenv('SERVER_NAME')

	return params

#=== main


