import urllib2
from bs4 import BeautifulSoup
import re
url = "http://web.archive.org/web/20121110093259/http://www.wbiao.cn:80/omega/"
content = urllib2.urlopen(url)
soup = BeautifulSoup(content,"lxml")
all_url =  soup.find_all('a')

regex = 'class="next".*'
for link in all_url:
	if  re.search(regex,str(link)):
		print "good"
		# print re.search(regex,link).group()
		print re.search(regex,str(link)).group()
		