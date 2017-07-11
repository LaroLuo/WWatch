# -*- coding: UTF-8 -*- 
import re
import csv
from scrapy import headers
from collections import OrderedDict
i = 0 

data_dict = [OrderedDict() for x in range(12)]

# 1 f 
dic_list = [7,9,10,11,12,13,14,15,16,17,18,19]

def processRow(data_row,f2_writer):
	for i in range(12):
		data_row[dic_list[i]] = search(data_dict[i],data_row[dic_list[i]])
	f2_writer.writerow(data_row)

def search(data_dictionary, item):
	temp_list = data_dictionary.keys()
	for i in range(len(temp_list)):
		if item == temp_list[i]:
			return i
	data_dictionary[item] = 1
	return len(data_dictionary.keys())-1




if __name__ == '__main__':
	file_name = ['rolex_data.csv',
	'omega_data.csv',
	'longines_data.csv',
	'tissot_data.csv',
	'citizen_data.csv',
	'casio_data.csv']
	watch = ["omega", "rolex", "longines", "tissot", "citizen", "casio"]
	for i in range(6):
		with open("clean/clean_"+file_name[i],"r") as f:
			f_csv = csv.reader(f)
			with open("final/final_"+file_name[i],"wb") as f2:
				f2.write(u'\ufeff'.encode('utf8'))
				f2_writer = csv.writer(f2, delimiter = ',')
				f2_writer.writerow(headers)
				for row in f_csv:
					processRow(row,f2_writer)
	with open("dict/dict","wb") as f3:
		for i in range(12):
			f3.write("*****************************************************************************\n")
			key_list = data_dict[i].keys()
			for index in range(len(key_list)):
				output = str(index) + "    " + str(key_list[index])+"\n"
				f3.write(output)




