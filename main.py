#coding:utf-8
import urllib2
from bs4 import BeautifulSoup
import re
import selenium
import csv
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
watch = ["omega","rolex","longines","tissot","citizen","casio"]
regex = ['.*/http://www.wbiao.cn(:80)?/omega-.{1,5}\.html',
		'.*/http://www.wbiao.cn(:80)?/rolex-g.{1,5}\.html',
		'.*/http://www.wbiao.cn(:80)?/longines-g.{1,5}\.html',
		'.*/http://www.wbiao.cn(:80)?/tissot-g.{1,5}\.html',
		'.*/http://www.wbiao.cn(:80)?/citizen-g.{1,5}\.html',
		'.*/http://www.wbiao.cn(:80)?/casio-g.{1,5}\.html'
		]


watch_initial_url = ["http://web.archive.org/web/20120610034333/http://www.wbiao.cn:80/omega/",
		"http://web.archive.org/web/20120505052057/http://www.wbiao.cn/rolex/",
		"http://web.archive.org/web/20120505013331/http://www.wbiao.cn/longines/",
		"http://web.archive.org/web/20120505020113/http://www.wbiao.cn/tissot/",
		"http://web.archive.org/web/20120920093500/http://www.wbiao.cn/citizen/",
		"http://web.archive.org/web/20120523183243/http://www.wbiao.cn:80/casio/"
		]

url2_tail = ".html"


def get_next_page_url(all_url):
	regex_local = "下一页"
	for link in all_url:
		if re.search(regex_local,(link).encode('utf-8')):
			return link.get('href').encode('utf-8')

def get_watch_url(all_url,watch_url,i):
	for link in all_url:
		if(link.get('href')):
			if re.search(regex[i],link.get('href').encode('utf-8')):
				watch_url.add(link.get('href'))

def write_url_to_csv(watch_url,i):
	with open (watch[i]+".csv","wb") as csvfile:
		csvwriter = csv.writer(csvfile,delimiter =',')
		csvwriter.writerow(['Url'])	
		for url in watch_url:
			csvwriter.writerow([url])


if __name__ == '__main__':
	i=0;
	for item in watch:
		url = watch_initial_url[i]
		watch_url = set()
		while(1):
			print url
			try:
				content = urllib2.urlopen(url)
			except:
				break
			soup = BeautifulSoup(content,"lxml")

			all_url =  soup.find_all('a')
			get_watch_url(all_url,watch_url,i)
			if get_next_page_url(all_url)==None:
				break
			else:
				url = "http://web.archive.org"+get_next_page_url(all_url)
		write_url_to_csv(watch_url,i)
		i= i+1

