#coding:utf-8
import urllib2
from bs4 import BeautifulSoup
import re
import csv
import signal
import sys
from get_title import get_titel_data
from get_desc import get_description
import threading
import time

class Mytheading(threading.Thread):
	def __init__(self,sing_url,watch_datas):
		threading.Thread.__init__(self)
		self.sing_url = sing_url
		self.watch_datas = watch_datas
	def run(self):
		read_single_page_data(self.sing_url,self.watch_datas)

Lock = threading.Lock()
watch = ["omega","rolex","longines","tissot","citizen","casio"]
file_name = ['omega.csv',
'rolex.csv',
'longines.csv',
'tissot.csv',
'citizen.csv',
'casio.csv']
url=[]
headers= [(u'name'.encode('utf-8')),(u'手表款式').encode('utf-8'),
(u'手表品牌').encode('utf-8'),(u'price').encode('utf-8'),(u'ww_price').encode('utf-8'),
(u'商品编号').encode('utf-8'),(u'商品型号').encode('utf-8'),(u'机芯').encode('utf-8'),
(u'机芯型号').encode('utf-8'),(u'表壳').encode('utf-8'),(u'尺寸').encode('utf-8'),
(u'厚度').encode('utf-8'),(u'表冠').encode('utf-8'),(u'表底').encode('utf-8'),
(u'表镜').encode('utf-8'),(u'表盘').encode('utf-8'),(u'表带').encode('utf-8'),
(u'表带颜色').encode('utf-8'),(u'表扣').encode('utf-8'),(u'防水').encode('utf-8'),
(u'功能').encode('utf-8'),(u'推出年份').encode('utf-8')]


def write_data_to_csv(watch_datas,i):
	with open (watch[i]+"_data.csv","wb") as csvfile:
		csvfile.write(u'\ufeff'.encode('utf8'))
		csvwriter = csv.writer(csvfile, delimiter = ',')
		csvwriter.writerow(headers)
		for watch_data in watch_datas:
			try:
				csvwriter.writerow(watch_data.values())
			except:
				print "write on no data"
				pass
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
	with open ("./url/"+str(file_name[i])) as f:
		f_csv = csv.reader(f)
		for row in f_csv:
			for link in row:
				url.append(link)

def read_single_page_data(single_url,watch_datas):
	watch_data = dict()
	single_url = "http://web.archive.org"+single_url
	
	Lock.acquire()
	print single_url
	try:
		content = urllib2.urlopen(single_url)
	except:
		print single_url+" no response!\n"
		Lock.release()
		return
	Lock.release()
	soup = BeautifulSoup(content,"html.parser")
	watch_data = get_titel_data(soup,watch_data)
	watch_data = get_description(soup,watch_data)
	Lock.acquire()
	watch_datas.append(watch_data)
	Lock.release()

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
	for i in range(6):
		watch_datas = []
		threads = []
		read_urls(i)
		for sing_url in url:
			thread = Mytheading(sing_url)
			threads.append(thread)
			thread.start()
		for item in threads:
			item.join()
		print len(watch_datas)
		write_data_to_csv(watch_datas,i)
	print "done!"

	# test
	# i = 1
	# watch_datas = []
	# threads = []
	# read_urls(i)
	# for sing_url in url:
	# 	thread = Mytheading(sing_url,watch_datas)
	# 	threads.append(thread)
	# 	thread.start()
	# for item in threads:
	# 	item.join()
	# print len(watch_datas)
	# write_data_to_csv(watch_datas,i)
	# print "done!"












	# print len(watch_data.keys())
	# for item in watch_data.keys():
	# 	print item