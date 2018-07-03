# dianping_reviews_spider

> `clone from [fuerlai](https://github.com/fuerlai)`

获取大众点评网的用户评论内容
=========================

评论信息格式：
------------

### shop_id: 
    商铺的ID,通过这个ID可以链接到商铺的信息页面
### customer_id: 
    用户的ID,通过这个ID可以链接到用户主页
### review_words: 
    评论的内容，支持emoji表情的解析和入库
### review_time: 
    评论的发表时间

使用说明：
--------

    可以以商铺来逐个获取用户的评论内容
    项目抓取的是火锅分类下的商铺的用户评论，当然支持扩展到其他分类下的商铺的用户评论信息
    
### 爬取三类数据，信息格式见SQL文件描述

### 爬取只需要设置main.py文件和setting.py文件
    比如爬取review时候，
    只要打开main.py中的执行review的行，注释其他两行
    打开setting.py中的review的pipeline，让系统进行入库review操作，注释掉其他两行
  

开发环境：
---------

### scrapy 1.5.0
### pymysql
### (我自己使用Anaconda3，其中包括了以上两个依赖库，当然也可以不必安装Anaconda3，但是一定要是python3平台)
### Pycharm2018.1
### MySQL5.5 + Navicat12
### Ubuntu1604(开发环境)
### Windows10(运行环境)
