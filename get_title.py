# -*- coding: UTF-8 -*-  
import urllib2
from bs4 import BeautifulSoup
import re
url = "http://web.archive.org/web/20120517100431/http://www.wbiao.cn/rolex-g11189.html"
url2 = "http://web.archive.org/web/20120619014216/http://www.wbiao.cn:80/omega-g4895.html"
url3 = "http://web.archive.org/web/20120307175154/http://www.wbiao.cn/omega-g6394.html"

def get_titel_data(soup,watch_title_data):
	if soup.find(attrs={"class": "goods-main-info-1"})!=None:
		return get_title_data_v1(soup,watch_title_data)
	elif soup.find(attrs={"class": "info"})!=None:
		return get_title_data_v2(soup,watch_title_data)
	else:
		print "title not in both"
	return watch_title_data

def strQ2B(ustring):
    rstring = ""
    for uchar in ustring:
        inside_code=ord(uchar)
        if inside_code == 12288:                                    
            inside_code = 32 
        elif (inside_code >= 65281 and inside_code <= 65374): 
            inside_code -= 65248
        rstring += unichr(inside_code)
    return rstring

def name_switch(st):
	if st == (u'name').encode('utf-8'):
		return 0
	elif st ==(u'手表款式').encode('utf-8'):
		return 1
	elif st == (u'手表品牌').encode('utf-8'):
		return 2
	elif st == (u'price').encode('utf-8'):
		return 3
	elif st == (u'ww_price').encode('utf-8'):
		return 4
	elif st == (u'商品编号').encode('utf-8'):
		return 5
	elif st == (u'商品型号').encode('utf-8'):
		return 6
	else :
		return -1


def get_title_data_v1(soup,watch_title_data):
	m = soup.find(attrs={"class": "goods-main-info-1"})
	if m != None and m.h1 != None:
		watch_title_data[0] = m.h1.string.encode('utf-8')
	m = soup.find(attrs={"class": "goods-main-info-2"})
	if m !=None and m.find_all('li')!= None:
		for item in m.find_all('li'):
			if item != None and item.i !=None and item.b !=None:
				name = (strQ2B(item.b.string).rstrip(":")).encode('utf-8')
				if(name_switch(name)==-1):
					continue
				if item.i.string!=None:
					value = strQ2B(item.i.string).encode('utf-8')
				else:
					value = strQ2B(item.i.a.string).encode('utf-8')
				watch_title_data[name_switch(name)] = value
	m =soup.find(attrs ={"class": "goods-main-info-3"})
	if m != None:
		watch_title_data[3] = strQ2B(m.find("del").string[1:]).encode('utf-8')
		watch_title_data[4] = strQ2B(m.find("ins").string[1:]).encode('utf-8')
	return watch_title_data

def get_title_data_v2(soup,watch_title_data):
	m = soup.find(attrs={"class": "info"})
	if m != None and m.h1 != None:
		watch_title_data[0] = m.h1.string.encode('utf-8')
	if m.find(attrs={"class": "props"}) !=None:
		for item in m.find(attrs={"class": "props"}).find_all("dl"):
			if item != None:
				name = (strQ2B(item.dt.string).rstrip(":")).encode('utf-8')
			if(name_switch(name)==-1):
				continue
			value = strQ2B(item.dd.string).encode('utf-8')
			watch_title_data[name_switch(name)] =  value
	try:
		reulst_set =  m.find(attrs={"class": "price"}).find_all("dl")
	except:
		return
	try:
		watch_title_data[4] = strQ2B(m.find("ins").string[1:]).encode('utf-8')
	except:
		return
	try:
		watch_title_data[3] = strQ2B(m.find("del").string[1:]).encode('utf-8')
	except:
		return
	return watch_title_data
	# for item in m:
	# 	print item
	# 	watch_title_data[item.encode('utf-8')] =  

if __name__ == '__main__':
	watch_title_data = dict()
	content = urllib2.urlopen(url3)
	soup = BeautifulSoup(content,"html.parser")
	get_titel_data(soup,watch_title_data)
	print watch_title_data.keys()