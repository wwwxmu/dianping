"""
@author: fulai
@file: Utils.py
@create: 2018/04/21 21:09:47
"""
import re


def contains(x, y):
    if x in y:
        return x
    else:
        return y


def get_base_url(url):
    if '?' in url:
        url = url.split('?')[0]
        base_url = re.match(r'(.*)p\d+', url).group(1)
        return base_url
    else:
        return url


def str2dct(s):
    if ';' in s:
        s1 = s.split('; ')
        s4 = dict()
        for s2 in s1:
            s3 = s2.split('=')
            s4[str(s3[0])] = s3[1]
        return s4
    else:
        return dict()
    pass
