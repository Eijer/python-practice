from email import header
import imp
from lib2to3.pgen2.pgen import generate_grammar
from urllib import request
from UACamouflage import my_ua
import requests
import re


header = {"User-Agent" : my_ua.random}

page = requests.get('http://fund.eastmoney.com/Data/Fund_JJJZ_Data.aspx?t=1&lx=1&letter=&gsid=&text=&sort=zdf,'
                            'desc&page=1,&feature=|&dt=1536654761529&atfc=&onlySale=0', headers=header)

page = requests.get('http://fund.eastmoney.com/Data/Fund_JJJZ_Data.aspx?t=1&lx=1&letter=&gsid=&text=&sort=zdf,'
                            , headers=header)

fund_list = re.findall(r'"[0-9]{6}",".+?"',page.text)
sum = len(fund_list)
length = (f'{i[1:7]},{i[10:-1]}' for i in fund_list)

print(fund_list[0])
print(sum)