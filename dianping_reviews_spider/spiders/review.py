# -*- coding: utf-8 -*-
import re
import time
from urllib import parse

import scrapy
from scrapy.http import Request

from dianping_reviews_spider.Utils.Utils import str2dct
from dianping_reviews_spider.items import ReviewsItemLoader, DianpingReviewsItem


class ReviewSpider(scrapy.Spider):
    name = 'review'
    allowed_domains = ['www.dianping.com']
    # 大众点评 > 火锅
    start_urls = ['http://www.dianping.com/chengdu/ch10/g110']
    myCookie = str2dct(
            '_lxsdk_cuid=164369a0118c8-050053550d16dd-19336952-fa000-164369a0119c8; _lxsdk=164369a0118c8-050053550d16dd-19336952-fa000-164369a0119c8; _hc.v=3afdb85d-1b1d-8f15-fada-c828f45f0983.1529924420; dper=61b33f82cef9397ae9cd3d9b47d3a82ad436b479b10908fe6b5c51ed431481301839933e98a438fce9e203c2d83baa1d01ab96df68653b0e5f6e9aa724b7525a3fa2c4398098fe1ce6fce6ad26a9b9afbb9ead3f438f83538ca339d143ffaacb; ua=%E9%9D%99%E6%95%B0%E7%A7%8B%E5%A4%A9w; ctu=9173c9e979df9b749fab54637cb26d43087400ea39df9378dc3719a0e97608d3; s_ViewType=10; ll=7fd06e815b796be3df069dec7836c3df; _lxsdk_s=1645ef96ec9-530-0-0e9%7C%7C586'
        )

    def parse(self, response):
        """
        获取当前页的商铺url列表
        遍历商铺url列表
        访问每个商铺的全部评论主页

        找到下一页的标签
        递归调用
        :param response: 当前列表页的response
        :return:
        """
        print(response.url)
        #shop_url_list = response.css(
        #    '#shop-all-list ul li .txt .tit a[data-hippo-type="shop"]::attr("href")'
        #).extract()

        shop_url_list = response.xpath(
                '//*[@id="shop-all-list"]/ul/li/div[@class="txt"]/div[@class="tit"]/a[@data-hippo-type="shop"]/@href'
        ).extract()
        if shop_url_list:
            for shop_url in shop_url_list:
                time.sleep(3)
                # 需要携带Cookie
                # 携带Cookie才能显示出所有的评论信息内容20条
                # 不携带Cookie的话没有登录状态
                # 每页评论信息只显示10条
                yield Request(url=shop_url + '/review_all',
                              cookies=self.myCookie,
                              callback=self.parse_detail)
                pass

        #next_url = response.css(
        #    '.shop-wrap .page .next::attr("href")'
        #).extract_first(None)
        next_url = response.xpath(
                '//div[@class="shop-wrap"]/div[@class="page"]/a[@class="next"]/@href'
        ).extract_first(None)
        # if next_url and 'g110p2' in next_url:
        if next_url:
            # 这就是下一页的url，尾递归调用继续爬取
            # url = parse.urljoin(response.url, next_url)
            yield Request(url=parse.urljoin(response.url, next_url),
                          callback=self.parse)
        pass

    def parse_detail(self, response):
        """
        获取评论页面的评论列表
        遍历评论列表，组装评论实体，存入数据库

        找到下一页的标签
        递归调用
        :param response: 当前商铺全部评论页的response
        :return:
        """
        shop_id = re.match(r'.*shop/(\d+)', response.url).group(1)

        review_list = response.css('.reviews-items > ul > li')

        # except: len(review_list) == 20
        print(response.url,
              '| the comment number of current page is:', len(review_list))

        if review_list:
            for review in review_list:
                itemLoader = ReviewsItemLoader(
                    item=DianpingReviewsItem(), response=response
                )
                customer_id = review.css(
                    '*::attr("data-user-id")').extract_first(
                    '')
                review_words = ''.join([
                    sentence.strip() for sentence in
                    review.css('.review-words::text').extract()
                ])
                review_time = review.css('.time::text').extract_first(
                    '').strip()

                itemLoader.add_value('shop_id', shop_id)
                itemLoader.add_value('customer_id', customer_id)
                itemLoader.add_value('review_words', review_words)
                itemLoader.add_value('review_time', review_time)
                reviewItem = itemLoader.load_item()
                #yield reviewItem

        next_url = response.css('.NextPage::attr("href")').extract_first(None)
        # 注释掉的代码作用为限制爬虫爬取页数为第一页
        # if next_url and 'p2' in next_url:
        if next_url:
            # 同样这里也需要携带Cookie
            # 凡是请求含有评论信息列表页面的请求的请求头都需要携带Cookie
            yield Request(url=parse.urljoin(response.url, next_url),
                          cookies=self.myCookie,
                          callback=self.parse_detail)
        pass
