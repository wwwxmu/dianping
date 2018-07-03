# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from twisted.enterprise import adbapi


class DianpingReviewsSpiderPipeline(object):
    def process_item(self, item, spider):
        return item


class BaseMysqlTwistedPipeline(object):
    def __init__(self, dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls, settings):
        dbparam = dict(
            host=settings['MYSQL_HOST'],
            port=settings['MYSQL_PORT'],
            user=settings['MYSQL_USER'],
            password=settings['MYSQL_PASSWORD'],
            db=settings['MYSQL_DB'],
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor,
            use_unicode=True
        )
        dbpool = adbapi.ConnectionPool('pymysql', **dbparam)
        return cls(dbpool)

    def process_item(self, item, spider):
        query = self.dbpool.runInteraction(self.do_insert, item)
        query.addErrback(self.handle_error, item, spider)

    def handle_error(self, failure, item, spider):
        print(failure)
        print(item)

    def do_insert(self, cursor, item):
        raise NotImplementedError(
            '{}.do_insert is not defined'.format(self.__class__.__name__))


class ReviewMysqlTwistedPipeline(BaseMysqlTwistedPipeline):
    def do_insert(self, cursor, item):
        sql = 'INSERT INTO review(`shop_id`, `customer_id`, ' \
              '`review_words`, `review_time`) ' \
              'VALUES (%s, %s, %s, %s); '
        cursor.execute(sql, (
            item['shop_id'], item['customer_id'],
            item['review_words'], item['review_time']
        ))
        return item


class CategoryMysqlTwistedPipeline(BaseMysqlTwistedPipeline):
    def do_insert(self, cursor, item):
        sql = 'INSERT INTO category(`index`, `category`, `url`) ' \
              'VALUES (%s, %s, %s); '
        cursor.execute(sql, (
            item['index'], item['category'], item['url']
        ))
        return item


class ShopMysqlTwistedPipeline(BaseMysqlTwistedPipeline):
    def do_insert(self, cursor, item):
        sql = 'INSERT INTO shop(`index`, `shop_id`, `shop`, ' \
              '`review_num`, `mean_price`, `address`, `recommend`, ' \
              '`taste`, `environment`, `service`) ' \
              'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s); '
        cursor.execute(sql, (
            item['index'], item['shop_id'], item['shop'],
            item['review_num'], item['mean_price'],
            item['address'], item['recommend'],
            item['taste'], item['environment'], item['service']
        ))
        return item


class DishMysqlTwistedPipeline(BaseMysqlTwistedPipeline):
    def do_insert(self, cursor, item):
        sql = 'INSERT INTO dish(`shop_id`, `menu_id`, `dish`, `price`) ' \
              'VALUES (%s, %s, %s, %s); '
        cursor.execute(sql, (
            item['shop_id'], item['menu_id'], item['dish'], item['price']
        ))
        return item
