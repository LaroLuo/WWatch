# -*- coding: UTF-8 -*-  
import re
import csv




def cleanrow(f_csv,f2_writer):
	
	for row in f_csv:
		try:
			row[10] = clean_size(row[10])
			row[11] = clean_thi(row[11])
			row[19] = clean_thi(row[19])
		except:
			continue
		f2_writer.writerow(row)


def clean_size(item):
	reg = '\d+\.*\d*'
	print item
	res = re.search(reg,item)
	if res:
		item = str(round((float)(res.group(0))))
	else:
		if(item==(u'大').encode('utf-8')):
			item= "36"
		elif(item==(u'中').encode('utf-8')):
			item = "30"
		elif(item==(u'小').encode('utf-8')):
			item = "22"
		else:
			pass
	return item

def clean_thi(item):
	reg = '\d+\.*\d*'
	print item
	res = re.search(reg,item)
	if res:
		item =str(round((float)(res.group(0)))) 
		return item
	return item




if __name__ == '__main__':
	file_name = ['rolex_data.csv',
	'omega_data.csv',
	'longines_data.csv',
	'tissot_data.csv',
	'citizen_data.csv',
	'casio_data.csv']
	for name in file_name:
		with open("result/"+name,"r") as f:
			f_csv = csv.reader(f)
			f2 = open("clean/clean_"+name,"wb")
			f2.write(u'\ufeff'.encode('utf8'))
			f2_writer = csv.writer(f2, delimiter = ',')
			print "clean"
			cleanrow(f_csv,f2_writer)
			f2.close()