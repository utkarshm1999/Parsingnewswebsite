import urllib2

from bs4 import BeautifulSoup
print "enter a date in dd/mm/yy format"
dd=raw_input()
mm=raw_input()
yy=raw_input()
#rediff has the urls in this kind Eg: http:.....issues/250118h1.html for 25thjan2018
url='http://www.rediff.com/issues/'+dd+mm+yy+'hl.html'
page=urllib2.urlopen(url)
soup=BeautifulSoup(page,'html.parser')
#since i only need the headlines and not sports,etc related stuffs I am segregating the division containing the headlines
div=soup.find('div',attrs={'id':"hdtab1"})
#searching for all the a tags in the headlines
itag=div.find_all('a',attrs={'target':'_new'})
#started LOOP from 1 and not 0 since element with index 0 shows live news,last point is obviously the lenght of itag
for x in range(1,len(itag)):
 #to print in this format 1."HEADLINE1"    
    print str(x)+"."+itag[x].text
    

                   
