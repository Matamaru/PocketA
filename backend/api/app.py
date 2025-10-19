#************************************************
#		Module:		backend.api.app (PocketA)	*
#		Author:		Scavenger4208				*
#		Version:	0.0.1						*
#************************************************

#=== Import

from flask import Flask

from backend.api.config import config_api

#=== defs and classes


def create_app():
	# get api_params from ENV
	api_params = config_api()

	# create and configure the app
	app = Flask('__name__')
	app.config.from_mapping(
			SECRET_KEY=api_params['secret_key'],
			DEBUG=api_params['debug']
			)

	@app.route('/')
	def home():
		return 'Home'

	return app
	



#=== main

if __name__ == "__main__":
	main()
