from scrapy.cmdline import execute
import sys
import os

# print(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

execute(['scrapy', 'crawl', 'review'])
# execute(['scrapy', 'crawl', 'shop'])
# execute(['scrapy', 'crawl', 'category'])
# dish获取采用ajax的方式，需要调大下载间隔时间
# execute(['scrapy', 'crawl', 'dish'])
