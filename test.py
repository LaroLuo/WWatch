import urllib2
from bs4 import BeautifulSoup
import re

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

if __name__ == '__main__':
	with open("out","rb") as f:

		soup = BeautifulSoup(f.read(),"html.parser")

		print (soup.li.i.a.string).encode('utf-8')