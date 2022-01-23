# -*- coding:UTF-8 -*-
"""
爬取基金列表
"""
from asyncio import exceptions
from email import header
import random
import re
import traceback
from matplotlib.pyplot import cla
import requests
from scipy import rand
from UACamouflage import my_ua


class GetFundList:


    def __init__(self,**kwargs):
        # 基金数量
        self._sum_of_fund = None
        # 迭代基金（code，name）
        self._fund_list_generator = None

        try:
            print("获取基金列表中……")
            self._set_fund_list_generator()
            assert self._fund_list_generator is not None
            print("共发现" + str(self._sum_of_fund) + "个基金")
        except:
            print("获取基金列表失败")
            traceback.print_exc()
    
    def get_fund_list(self):
        return self._fund_list_generator
    def get_sum_of_fund(self):
        return self._sum_of_fund
    def _set_fund_list_generator(self,**kwargs):
        raise NotImplementedError()


class GetFundListFromWeb(GetFundList):
    """
    获取当时的基金列表
    """

    def _set_fund_list_generator(self, **kwargs):
        header = {"User-Agent" : my_ua.random}

        """
        page = requests.get('http://fund.eastmoney.com/Data/Fund_JJJZ_Data.aspx?t=1&lx=1&letter=&gsid=&text=&sort=zdf,'
                            'desc&page=1,&feature=|&dt=1536654761529&atfc=&onlySale=0', headers=header)
        """        

        page = requests.get('http://fund.eastmoney.com/data/fundranking.html#tall;c0;r;s6yzf;pn10000;ddesc;qsd20210122;qed20220122;qdii;zq;gg;gzbd;gzfs;bbzt;sfbb',headers=header)
        fund_list = re.findall(r'"[0-9]{6}",".+?"',page.text)
        self._sum_of_fund = len(fund_list)
        self._fund_list_generator = (f'{i[1:7]},{i[10:-1]}' for i in fund_list)


class Test(GetFundListFromWeb):
    """
    对GetFundListFromWeb进行测试，随机拿取一些结果
    """
    TEST_NUM = 5

    def _set_fund_list_generator(self, **kwargs):
        """
        爬取简单的基金代码名称目录
        return: iterator str 基金编号，基金名称
        """
        super()._set_fund_list_generator()
        head_index= random.randint(0,self._sum_of_fund - self.TEST_NUM)
        fund_list = list(self._fund_list_generator)[from_index:from_index + self.TEST_NUM]
        self._fund_list_generator = (i for i in fund_list)
        self._sum_of_fund = self.TEST_NUM

