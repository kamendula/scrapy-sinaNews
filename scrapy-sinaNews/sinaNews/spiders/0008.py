from bs4 import BeautifulSoup
from urllib import urlopen

r = urlopen('http://sports.sina.com.cn//g//pl//2015-04-25//10267586694.shtml').read()
soup = BeautifulSoup(r)
#print soup
t = soup.find('div', class_='img_wrapper')
print t.img['src']
#print t
#print type(t)
#s=''
#for p in t[0].find_all("p"):
#    s = s + p.get_text()+'\n'

#print s



