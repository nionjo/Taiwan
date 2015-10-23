import os
import xml.etree.ElementTree as ET 


ref_path = 'DATA_Traffic_XML(20150401-20150630)';
dates=['2015_4_1', '2015_4_10', '2015_4_11', '2015_4_12'];
#print(dates[1]);
#os.path.join(, 'python', 'bin')
for i in dates:
	dir_path = os.path.join(ref_path, i);
	print(dir_path)
	for filename in os.listdir(dir_path):
		if not filename.endswith('.xml'): continue
		fullname = os.path.join(dir_path, filename)
		tree = ET.parse(fullname)
		print(tree)
#	e = xml.etree.ElementTree.parse('thefile.xml').getroot()
