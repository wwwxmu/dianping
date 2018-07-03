"""
@author: fulai
@file: data.py
@create: 2018/04/21 18:46:24
"""
from dianping_reviews_spider.settings import cursor


def category_url():
    sql = 'SELECT `index`, `category`, `url` FROM category; '
    cursor.execute(sql)
    result = cursor.fetchall()
    dct = {}
    for res in result[1:]:
        dct[res[2]] = res[0]
    return dct


def shop_id():
    sql = 'SELECT `shop_id` FROM shop; '
    cursor.execute(sql)
    result = cursor.fetchall()
    lst = []
    for res in result:
        lst.append(res[0])
    return lst


if __name__ == '__main__':
    # test
    # print(len(category_url()))
    print(category_url())
    # print(list(category_url().keys()))
    print(shop_id())
    pass
