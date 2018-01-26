import urllib2

from bs4 import BeautifulSoup
print "enter a date in dd/mm/yy format"
dd=raw_input()
mm=raw_input()
yy=raw_input()
url='http://www.rediff.com/issues/'+dd+mm+yy+'hl.html'
page=urllib2.urlopen(url)
soup=BeautifulSoup(page,'html.parser')
div=soup.find('div',attrs={'id':"hdtab1"})
itag=div.find_all('a',attrs={'target':'_new'})
for x in range(1,len(itag)):
    print str(x)+"."+itag[x].text
    

                   
