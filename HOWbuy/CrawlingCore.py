# -*- coding:UTF-8 -*-
from email import header
from unittest import result
from matplotlib.pyplot import cla
from UACamouflage import my_ua
from abc import ABC

from bs4 import BeautifulSoup

class GetPage:
    def __init__(self):
        self._task_queue = None
        self._result_queue = None

class GetPageByWeb(GetPage,ABC):
    @classmethod
    def get_page_context(cls,url,timeout,*args) -> tuple:


        header = {"User-Agent" : my_ua.random}
        import requests
        try:
            page = requests.get(url,headers=header,timeout=timeout)
            page.encoding = 'utf-8'
            if page.text:
                result = ('Success',page.text,*args)
            else:
                result = ('Error',url,*args)
        except(requests.exceptions.ConnectionError,requests.exceptions.Timeout,requests.exceptions.HTTPError):
                result = ('Error',url,*args)
        return result

html = GetPageByWeb.get_page_context("https://www.howbuy.com/fund/fundranking/",3)
print(html[0])
print(html[1])