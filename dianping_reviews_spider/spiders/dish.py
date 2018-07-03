# -*- coding: utf-8 -*-
import json

import scrapy
from scrapy import FormRequest

from dianping_reviews_spider.Tools.data import shop_id
from dianping_reviews_spider.Utils.Utils import str2dct
from dianping_reviews_spider.items import Dish


class DishSpider(scrapy.Spider):
    name = 'dish'
    allowed_domains = ['www.dianping.com']
    start_urls = ['http://www.dianping.com/chengdu/ch10/g110']

    ajaxUrl = 'http://www.dianping.com/ajax/json/shopDynamic/shopTabs'
    myCookie = str2dct(
        'cy=8; cye=chengdu; _lxsdk_cuid=163b90dbe38c8-093f0e0fe4db66-1125130c-1fa400-163b90dbe39c8; _lxsdk=163b90dbe38c8-093f0e0fe4db66-1125130c-1fa400-163b90dbe39c8; _hc.v=2364b9c9-30b5-b2b4-4052-8b27657d2f31.1527818076; UM_distinctid=163b90dcc6c30c-08987dd68a76d5-1125130c-1fa400-163b90dcc6d8d5; dper=bd62b90833db84f21f9f854cafa2330aed7e4b7fcf0a7d2cafd33596d966c11c73954cc4f7a682b4b5cd109057943afdf745c5f0df6fa2553e61c4bc6e7d3a71d4cfa9621dd09f5b31a34f82fb16c595b9ef6adbfa234db4c14c7e755aaa953f; ll=7fd06e815b796be3df069dec7836c3df; ua=lf48168886; ctu=289cc56522f0935231dc6d49ac500620dc36e2c46c6d5c43d999a86ce89164eb; uamo=15528021262; s_ViewType=10; _lxsdk_s=163bb18bfb6-5ed-1d9-887%7C%7C6')

    def parse(self, response):
        for shopId in shop_id():
            form_data = {
                'shopId': str(shopId),
                # 'cityId': str(8),
                # 'shopType': str(10),
            }
            yield FormRequest(url=self.ajaxUrl,
                              formdata=form_data,
                              cookies=self.myCookie,
                              callback=self.parse_detail)
        pass

    def parse_detail(self, response):
        resp_json = json.loads(response.text)
        if resp_json['code'] == 200:
            allDishes = resp_json['allDishes']
            for dishes in allDishes:
                dish = Dish()
                dish['shop_id'] = resp_json['shop']['shopId']
                dish['menu_id'] = str(dishes['menuId'])
                dish['dish'] = dishes['dishTagName']
                dish['price'] = str(dishes['finalPrice'])
                #yield dish
                print(dish)
        pass
