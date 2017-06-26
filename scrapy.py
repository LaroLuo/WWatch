#coding:utf-8
import urllib2
from bs4 import BeautifulSoup
import re
import selenium
import csv
import signal
import sys
from get_title import get_titel_data

name_attri = ["model",""]
make_attri = []
watch_data = dict()
all_urls = []
watch = ["omega","rolex","longines","tissot","citizen","casio"]
file_name = ['omega.csv',
'rolex.csv',
'longines.csv',
'tissot.csv',
'citizen.csv',
'casio.csv']
watch_datas = []
old_version=0
new_version=0
url=[]
headers= [(u'name'.encode('utf-8')),(u'手表款式').encode('utf-8'),
(u'手表品牌').encode('utf-8'),(u'price').encode('utf-8'),(u'ww_price').encode('utf-8'),
(u'商品编号').encode('utf-8'),(u'商品型号').encode('utf-8')]


def write_data_to_csv(watch_datas,i):
	with open (watch[i]+"_data.csv","wb") as csvfile:
		csvfile.write(u'\ufeff'.encode('utf8'))
		csvwriter = csv.writer(csvfile, delimiter = ',')
		csvwriter.writerow(headers)
		
		for watch_data in watch_datas:
			for item in watch_data:
				print watch_data[item]
			csvwriter.writerow([watch_data[0],watch_data[1],
				watch_data[2],watch_data[3],
				watch_data[4],watch_data[5],
				watch_data[6]])
			# csvwriter.writerow({0:watch_data[0],1:watch_data[1],
			# 	2:watch_data[2],3:watch_data[3],
			# 	4:watch_data[4],5:watch_data[5],
			# 	6:watch_data[6]})



			# csvwriter.writerows({(u'name'.encode('utf-8')):watch_data[u"name".encode('utf8')],
			# (u'手表款式').encode('utf8'):watch_data[u"手表款式".encode('utf8')],
			# (u'手表品牌').encode('utf8'):watch_data[u"手表品牌".encode('utf8')],
			# (u'price').encode('utf8'):watch_data[u"price".encode('utf8')],
			# (u'ww_price').encode('utf8'):watch_data[u"ww_price".encode('utf8')],
			# (u'商品编号').encode('utf8'):watch_data[u"商品编号".encode('utf8')],
			# (u'商品型号').encode('utf8'):watch_data[u"商品型号".encode('utf8')]})


def read_urls(i):
	with open (str(file_name[i])) as f:
		f_csv = csv.reader(f)
		for row in f_csv:
			for link in row:
				url.append(link)

def read_single_page_data(single_url):
	single_url = "http://web.archive.org"+single_url
	print single_url
	try:
		content = urllib2.urlopen(single_url)
	except:
		print single_url+" no response!\n"
		return
	soup = BeautifulSoup(content,"lxml")
	watch_datas.append(get_titel_data(soup,watch_data))

# st = soup.get_text().encode('utf-8')
# def get_name(st):
# 	rex = ".*\(价格、报价、图片\)"
# 	# result =  soup.meta
# 	# print len(result)
# 	# for item in result:
# 	# 	print item.encode('utf-8')
# 	m = re.search(rex,st)
# 	if m==None:
# 		rex = ".*(\-万表网)"
# 		m = re.search(rex,st)
# 		if m==None:
# 			print "No data!"
# 			return
# 		name = st[m.start():m.end()-10]
# 	else:
# 		name =  st[m.start():m.end()-26]
# 	print name
# 	watch_data[name] = {}


if __name__ == '__main__':
	i=1
	read_urls(i)
	for sing_url in url:
		read_single_page_data(sing_url)
	print len(watch_datas)
	write_data_to_csv(watch_datas,i)
	# print len(watch_data.keys())
	# for item in watch_data.keys():
	# 	print item