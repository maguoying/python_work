from urllib.request import urlopen

url = urlopen("https://movie.douban.com/chart");
#print(url.read());
filename = 'urltext.html';
with open(filename,'w') as fo:
    fo.write(str(url.read()));
