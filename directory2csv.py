import os
from os import listdir
from os.path import isfile, join
import csv
import xmlparser

mypath = '/home/nionjo/Desktop/Taiwan/DATA_Traffic_XML/DATA_Traffic_XML'

directories = listdir(mypath)
csvdir='/home/nionjo/Desktop/Taiwan/Traffic_CSVs'
try:
    os.stat(csvdir)
except:
	os.mkdir(csvdir)  
for d in directories: 
	dirname = join(mypath, d)
	if not d.startswith('.'):
		xmlfiles = listdir(join(mypath, d))
		for xmlname in xmlfiles:
			lanecounter = 0
			csvname = xmlname + ".csv"
			myfile = open(join(csvdir, csvname),'wb')
			wr = csv.writer(myfile,delimiter=";")
			newrow =  ("timestamp","vdid")
			print xmlname
			xmlparser.parse(join(dirname,xmlname))
