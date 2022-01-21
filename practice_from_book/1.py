from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

#关闭https协议验证证书
ssl._create_default_https_context = ssl._create_unverified_context

html = urlopen("https://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html)

nameList = bsObj.find_all("span",{"class":"green"})
for name in nameList:
    print(name.get_text())