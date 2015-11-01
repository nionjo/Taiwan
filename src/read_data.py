from xmlparser import *
from traffic_dataset_setter import *
import copy
import sys

xmldir = "/home/antonis/DATA_Traffic_XML(20150401-20150630)/2015_4_1/"
xml_files = [  xmldir+"201503312358.xml", xmldir+"201504010033.xml" ]

for xml_file in xml_files:
	try:
		parse(xml_file)
	except:	
		sys.stdout.write("ZOOOONG") 
		exit(1)
	
for datapoint,data in  traffic_dataset_setter().get_dataset().iteritems():
	for key, value in data.iteritems():
		
