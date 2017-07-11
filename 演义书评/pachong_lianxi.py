#!/usr/bin/python
# encoding:utf-8

# 为sanguoyy_pa_changpl 做实验正则表达式，有的评论爬不下来
# 在网络爬虫抓取信息的过程中，如果抓取频率高过了网站的设置阀值，将会被禁止访问
import re
import requests
from multiprocessing import Pool
from requests.exceptions import RequestException



urll='https://book.douban.com/review/7666918/'
content = requests.get(urll).text
print(content) #知道是因为爬虫太多，被禁止访问
# 筛选长评论 推荐等级（几颗星“力荐”）及其标题
pattern = re.compile(
    '<h1.*?summary.*?>(.*?)</span>.*?<span.*?allstar.*?title="(.*?)">.*?<div.*?review-content.*?data-url.*?>(.*?)</div>.*?<script.*?type.*?text.*?>',
    re.S)
#<h1.*?summary.*?>(.*?)</span>.*?<span.*?allstar.*?title="(.*?)"></span>.*?<div.*?review-content.*?>(.*?)<script.*?text.*?>
results = re.findall(pattern, content)
print(results)