from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html,'lxml')
for sibling in bsObj.find("table",{"id":"giftList"}).tr:
 print(sibling.get_text())