# -*- coding: utf-8 -*-
import re
from urllib import parse

import scrapy
from scrapy import Request

from dianping_reviews_spider.Tools.data import category_url
from dianping_reviews_spider.Utils.Utils import get_base_url
from dianping_reviews_spider.items import Shop


class ShopSpider(scrapy.Spider):
    name = 'shop'
    allowed_domains = ['www.dianping.com']
    start_urls = list(category_url().keys())

    # 商铺去重机制
    shop_ids = set()

    def parse(self, response):
        index = category_url().get(get_base_url(response.url))
        shopTerm_list = response.css(
            '#shop-all-list ul li .txt'
        )
        for shopTerm in shopTerm_list:
            shop_url = shopTerm.css(
                '.tit a[data-hippo-type="shop"]::attr("href")'
            ).extract_first('')
            shop_id = re.match(r'.*shop/(\d+)', shop_url).group(1)

            # 商铺去重机制的实现，保证入库不出错
            if shop_id in self.shop_ids:
                continue
            self.shop_ids.add(shop_id)

            shop = shopTerm.css(
                '.tit a[data-hippo-type="shop"]::attr("title")'
            ).extract_first('')
            review_num = re.match(
                r'.*?(\d+).*',
                ''.join(list(filter(
                    str.strip, shopTerm.css('.review-num *::text').extract()
                )))
            )
            if review_num:
                review_num = review_num.group(1)
            mean_price = re.match(
                r'.*?(\d+).*',
                ''.join(list(filter(
                    str.strip, shopTerm.css('.mean-price *::text').extract()
                ))).replace('\n', '')
            )
            # 有时候网页没有显示人均价格，有人均价格就抓下来，没有就默认None
            if mean_price:
                mean_price = mean_price.group(1)
            address = list(filter(
                str.strip, shopTerm.css('.tag-addr *::text').extract()
            ))
            recommend = list(filter(
                str.strip, shopTerm.css('.recommend *::text').extract()
            ))[1:]
            comment_list = list(filter(
                str.strip, shopTerm.css('.comment-list *::text').extract()
            ))
            taste = None
            environment = None
            service = None
            if len(comment_list) is 6:
                taste = comment_list[1]
                environment = comment_list[3]
                service = comment_list[5]

            shopItem = Shop()
            shopItem['index'] = index
            shopItem['shop_id'] = str(shop_id)
            shopItem['shop'] = shop
            shopItem['review_num'] = str(review_num)
            shopItem['mean_price'] = str(mean_price)
            shopItem['address'] = str(address)
            shopItem['recommend'] = str(recommend)
            shopItem['taste'] = taste
            shopItem['environment'] = environment
            shopItem['service'] = service
            yield (shopItem)

        next_url = response.css(
            '.shop-wrap .page .next::attr("href")'
        ).extract_first(None)
        if next_url:
            yield Request(url=parse.urljoin(response.url, next_url),
                          callback=self.parse)
        pass
