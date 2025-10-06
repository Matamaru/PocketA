#************************************************************
#	Module:			backend.datamodule.datamodule (PocketA)	*
#	Author:			Scavenger4208							*
#	Version:		0.0.1									*
#************************************************************

#=== Imports

import psycopg2

#=== Defs and classes

class DataBase:
	def __init__(self, params):
		self.params = params

	def connect(self):
		self.conn = psycopg2.connect(**self.params)
		self.cursor = self.conn.cursor()
		self.conn.autocommit = True

	def close_conn(self):
		if self.cursor is not None:
			self.cursor.close()
		if self.conn is not None:
			self.conn.close()
		print('Connection to database closed.')

	def check_conn(self):
		if self.conn:
			print('Connection to database established.')
		else:
			print('No connection to database.')
