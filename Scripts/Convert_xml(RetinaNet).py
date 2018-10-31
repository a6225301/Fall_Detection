import csv,os
import xml.etree.cElementTree as ET
from glob import glob

xmls_files=glob('C:\\Users\\hehe\\Desktop\\FALL_Image\\Annotation\\*.xml')

print (xmls_files[0])

category='Tumble'


def write_csv(xml_file):
	a_list=[]
	tree = ET.ElementTree(file=xml_file)
	for elem in tree.iterfind('path'):
		print (elem.tag, elem.text.split('\\')[-1])
		a_list.append(elem.text)
	for elem in tree.iterfind('object/bndbox/'):
		print (elem.tag, elem.text)
		a_list.append(elem.text)
	a_list.append(category)

	# print (a_list)


	with open('annotation.csv','a') as f:
		writer=csv.writer(f,lineterminator='\n')
		writer.writerow(a_list)

if __name__ == '__main__':
	for xml_file in xmls_files:
		write_csv(xml_file)


	with open('class_mapping.csv','w') as f:
		writer=csv.writer(f,lineterminator='\n')
		writer.writerow(['Tumble',0])