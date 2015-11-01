#!/usr/bin/python
import copy

class traffic_dataset_setter(object):

	'''
		Last Comment: For now it seems that it works only for one xml, therefore dataset_data 
		is not correct name, it should be datapoint data. therefore, several changes should be done in this class
		
		This class is dedicated to create the controller for one sensor of traffic
		The abstraction layers that this class has is:
				datapoint:
					many x ( sensor_data
							info : string
							lane : list
							car  : list )
			
	'''	
	dataset_data = {}

	def __init__(self,sensor_id = None,data_collection_time = None):
		self.sensor_id =  sensor_id
		self.data_collection_time = data_collection_time
		self.init_data_point()
		self.__datapoint = self.__get_datapoint(self.data_collection_time)
		self.init_dataset_data()
		
	def init_data_point(self):

		if self.data_collection_time not in self.dataset_data:
                        self.dataset_data[self.data_collection_time] = {}
		
	def __get_datapoint(self,data_collection_time):

		try:
			return self.dataset_data[data_collection_time]
		except KeyError:
			print "key {0} not found in sensor data".format(data_collection_time)	

	def init_dataset_data(self):	

		if self.sensor_id not in self.dataset_data[self.data_collection_time]:
			self.__datapoint[self.sensor_id] = {}
	
	def set_sensor_info(self,status):

		if 'info' not in self.__datapoint[self.sensor_id]:
			self.__datapoint[self.sensor_id]['status'] = status
	
	def set_lane_data(self,key,lane_data):
		
		if key not in self.__datapoint[self.sensor_id]:
			self.__datapoint[self.sensor_id][key] = [ 'lane',lane_data,'cars' ] 
		else:
			self.__datapoint[self.sensor_id][key].append(lane_data)	
		
	def set_car_data(self,key, car_data):
	
		try:	
			self.__datapoint[self.sensor_id][key].append(car_data)	
		except KeyError:
			print "key error but you can increase the debug output for the problem here and write it to the logger in car data information"
	
	def get_dataset(self):
		'''	
			return a shallow copy of the dataset
		'''		
		return copy.copy(self.dataset_data)
