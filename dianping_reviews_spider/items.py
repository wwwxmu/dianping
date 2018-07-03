# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst


class DianpingReviewsSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

# 定义爬取的数据形式
# 对类的属性设计，同时也是对数据表的字段设计，两者最好保持一致
# 注意因为数据库字段名最好没有大小写之分，所以尽量不要有大小写混拼的定义

class DianpingReviewsItem(scrapy.Item):
    # 商铺id，假设大众点点评网的商铺id是对商铺的唯一标识
    shop_id = scrapy.Field()
    # 顾客id
    customer_id = scrapy.Field()
    # 顾客评价
    review_words = scrapy.Field()
    # 评论的时间
    review_time = scrapy.Field()
    pass


class Category(scrapy.Item):
    # 分类序号
    index = scrapy.Field()
    # 分类名称
    category = scrapy.Field()
    # 分类对应的URL
    url = scrapy.Field()
    pass


class Shop(scrapy.Item):
    # 店铺所在分类的分类序号
    index = scrapy.Field()
    # 商铺id
    shop_id = scrapy.Field()
    # 商铺名称
    shop = scrapy.Field()
    # 评论总数
    review_num = scrapy.Field()
    # 大众点评网给计算出的商铺人均价格
    mean_price = scrapy.Field()
    # 商铺地址
    address = scrapy.Field()
    # 推荐菜
    recommend = scrapy.Field()
    # 商铺的评分
    taste = scrapy.Field()
    environment = scrapy.Field()
    service = scrapy.Field()
    pass


class Dish(scrapy.Item):
    shop_id = scrapy.Field()
    # 菜品id
    menu_id = scrapy.Field()
    # 菜品名称
    dish = scrapy.Field()
    # 菜品价格
    price = scrapy.Field()
    pass


class ReviewsItemLoader(ItemLoader):
    default_output_processor = TakeFirst()
