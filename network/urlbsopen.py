from urllib.request import urlopen
from bs4 import BeautifulSoup
url = urlopen("https://movie.douban.com/chart");
#print(url.read());
bsObj = BeautifulSoup(url.read());

#needPrint = bsObj.find("div",{"class":"pl2"}).children;
#print(needPrint);
filename = 'urlbstext.txt';
with open(filename,'w',encoding="utf-8") as fo:
    for word in bsObj.find("div",{"class":"pl2"}).children:
        fo.write(str(word)+'\n');
