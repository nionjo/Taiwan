import xml.sax
import copy
xmldir = "/home/antonis/taiwan/DATA_Traffic_XML(20150401-20150630)/2015_4_1/"
xmlfile = xmldir+"201503312358.xml"
xmlfile2 = xmldir+"201504010033.xml"

class traffic_dataset_sender(object):
	'''
		it will send the data to model for updates, creates
	'''	
	
	
	def __init__(self,datapoint):
		self.datapoint = datapoint
	
	def get_datapoint(self,timestamp):
		try:
			return self.dataset[timestamp]
		except KeyError:
			print "datapoint at time {0} not found".format(timestamp)

	def get_sensor_object(self,datapoint,sensor_id):
		try:
			return datapoint[sensor_id]
		except KeyError:
			print "error"	

	def get_sensor_info(self,sensor):
		try:
			return sensor['info']
		except KeyError:
			print "error"

	
	

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
	
class xmlparser(xml.sax.ContentHandler):
	
	"""
		XML_Head [(u'listname', u'VD\u4e94\u5206\u9418\u52d5\u614b\u8cc7\u8a0a'), (u'updatetime', u'2015/04/01 00:33:00'), (u'version', u'1.1'), (u'interval', u'300')]

		lane [(u'vsrdir', u'0'), (u'laneoccupy', u'2'), (u'speed', u'85'), (u'vsrid', u'1')]
		cars [(u'volume', u'19'), (u'carid', u'S')]
		cars [(u'volume', u'0'), (u'carid', u'T')]
		cars [(u'volume', u'0'), (u'carid', u'L')]
		lane [(u'vsrdir', u'0'), (u'laneoccupy', u'0'), (u'speed', u'0'), (u'vsrid', u'2')]
		cars [(u'volume', u'0'), (u'carid', u'S')]
		cars [(u'volume', u'0'), (u'carid', u'T')]
		cars [(u'volume', u'0'), (u'carid', u'L')]
	"""
		
	def __init__(self):
		self.traffic_controller = None
		

	def startElement(self, tag, attributes):
		'''
			parse xml's
		'''
		if str(tag).lower() ==  'xml_head':
			print "New xml came\n\n"

		if str(tag).lower() == 'info':
			vd_id =  attributes.get('vdid','')
			collect_time = attributes.get('datacollecttime','')
			self.traffic_controller = traffic_dataset_setter(vd_id,collect_time) #initialize controller for that sensor		
			self.traffic_controller.set_sensor_info(attributes.get('status'))
	
		if str(tag).lower() == 'lane':
			key = (attributes.get('vsrdir',''), attributes.get('vsrid',''))
			lane_data = [attributes.get('laneoccupy',''),attributes.get('speed','')]
			self.traffic_controller.set_lane_data(key,lane_data)
			self.temp = key		
	
		if str(tag).lower() == 'cars':
			key = self.temp
			car_data = [attributes.get('volume',''),attributes.get('carid')]
			self.traffic_controller.set_car_data(key,car_data)

	def parse_attributes(self,attributes):
		pass

	def endElement(self, tag):
		pass



parser = xml.sax.make_parser()
parser.setFeature(xml.sax.handler.feature_namespaces, 0)
Handler = xmlparser()
parser.setContentHandler( Handler )   
parser.parse(xmlfile2)
#parser.parse(xmlfile)
for datapoint,data in  traffic_dataset_setter().get_dataset().iteritems():
	for key, value in data.iteritems():
		print key,value
