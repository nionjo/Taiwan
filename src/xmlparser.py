#/usr/bin/python
from  traffic_dataset_setter import traffic_dataset_setter
import xml.sax

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
			self.traffic_controller = traffic_dataset_setter(vd_id,collect_time)	
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

def parse(xml_file):
	parser = xml.sax.make_parser()
	parser.setFeature(xml.sax.handler.feature_namespaces, 0)
	Handler = xmlparser()
	parser.setContentHandler( Handler )
	parser.parse(xml_file)	

