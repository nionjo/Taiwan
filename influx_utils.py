#!/usr/python

import traceback
from influxdb import client as influxdb

class data_base_client():
	
	def __init__(self,ip='localhost' port = 8086,username = 'root', password = 'root', database = 'taiwan'):
		self.ip = ip
		self.port = port
		self.uri = "http://{0}:{1}".format(self.ip,self.port)
		self.user = username
		self.password = password
		self.database = datavase
	
	def get_database_client (self):	
		try:
			return influxdb.InfluxDBClient('localhost', 8086, 'root', 'root', 'example')
		except Exception:
			print traceback.print_exception()

class data_base_controller()
	'''
		Once you get the client you can get the controller and create the database
	'''	
	def __init__(self,db_client = data_base_client.get_database_client() ):
		self.client = db_client

	



