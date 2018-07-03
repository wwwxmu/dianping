# -*- coding: utf-8 -*-
import scrapy

from dianping_reviews_spider.items import Category


class CategorySpider(scrapy.Spider):
    """
    获取火锅分类下的子分类
    """
    name = 'category'
    allowed_domains = ['www.dianping.com']
    # 大众点评 > 火锅
    start_urls = ['http://www.dianping.com/chengdu/ch10/g110']

    def parse(self, response):
        subClassfy = response.css('#classfy-sub > a')
        categories = subClassfy.css('*::text').extract()
        cate_urls = subClassfy.css('*::attr(href)').extract()
        for index, cate, cate_url in zip(
                range(len(categories)), categories, cate_urls
        ):
            categoryItem = Category()
            categoryItem['index'] = str(index)
            categoryItem['category'] = cate
            categoryItem['url'] = cate_url
            yield categoryItem
        pass
