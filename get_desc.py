# -*- coding: UTF-8 -*-  
# -*- coding: gbk -*-
import urllib2
from bs4 import BeautifulSoup
import re
from get_title import strQ2B
url = "http://web.archive.org/web/20120517100431/http://www.wbiao.cn/rolex-g11189.html"
url2 = "http://web.archive.org/web/20120619014216/http://www.wbiao.cn:80/omega-g4895.html"
watch_desc = dict()
def name_switch(st):
	if st == (u'机芯').encode('utf-8'):
		return 7
	elif st ==(u'机芯型号').encode('utf-8'):
		return 8
	elif st ==(u'表壳').encode('utf-8'):
		return 9
	elif st ==(u'尺寸').encode('utf-8'):
		return 10
	elif st ==(u'厚度').encode('utf-8'):
		return 11
	elif st ==(u'表冠').encode('utf-8'):
		return 12
	elif st ==(u'表底').encode('utf-8'):
		return 13
	elif st ==(u'表镜').encode('utf-8'):
		return 14
	elif st ==(u'表盘').encode('utf-8'):
		return 15
	elif st ==(u'表带').encode('utf-8'):
		return 16
	elif st ==(u'表带颜色').encode('utf-8'):
		return 17
	elif st ==(u'表扣').encode('utf-8'):
		return 18
	elif st ==(u'防水').encode('utf-8'):
		return 19
	elif st ==(u'功能').encode('utf-8'):
		return 20
	elif st ==(u'推出年份').encode('utf-8'):
		return 21
	else :
		return -1

def get_description(soup,watch_desc):
	if soup.find(attrs = {"class":"goods-attributes"})!=None:
		return get_desc_v1(soup,watch_desc)
	elif soup.find(attrs = {"id":"attrs"})!=None:
		return get_desc_v2(soup,watch_desc)
	else:
		print "description not in both"
		return watch_desc



def get_desc_v1(soup,watch_desc):
	try:
		m = soup.find(attrs = {"class":"goods-attributes"})
	except:
		print "v1 no data"
		pass
	dt_data = m.dt
	dd_data = m.dd
	i = 0
	while dt_data != None and dd_data !=None:
		try:
			name = dt_data.string.encode('utf-8')
			value = strQ2B(dd_data.string).encode('utf-8').strip()
		except:
			return watch_desc
		if(name_switch(name)==-1):
			dt_data = dt_data.find_next("dt")
			dd_data = dd_data.find_next("dd")
			continue
		watch_desc[name_switch(name)] = value
		dt_data = dt_data.find_next("dt")
		dd_data = dd_data.find_next("dd")
		i = i+1
	return watch_desc

def get_desc_v2(soup,watch_desc):
	try:
		m = soup.find(attrs = {"id":"attrs"})
	except:
		print "v2 no data"
		pass
	try:
		dl_data =  m.find_all("dl")
		for item in dl_data:
			name = item.dt.string.encode('utf-8')
			if(name_switch(name)==-1):
				continue
			watch_desc[name_switch(name)] = strQ2B(item.dd.string).strip().encode('utf-8')
	except:
		pass
	return watch_desc

if __name__ == '__main__':
	content = urllib2.urlopen(url)
	soup = BeautifulSoup(content,"html.parser")
	get_description(soup,watch_desc)
	for item in watch_desc:
		print str(item) + " " +watch_desc[item]


	# print soup