#!/usr/bin/python
# encoding:utf-8
import json
from multiprocessing import Pool
import requests
from requests.exceptions import RequestException
import re
# 爬虫采集评论编号
def get_one_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None

def parse_one_page(html):
    pattern = re.compile('<div.*?main-bd.*?>.*?<div.*?review\w(.*?)\wshort.*?>', re.S)
    items = re.findall(pattern, html)
    return items #是列表，此处返回每一页评论编号

def write_to_file(content):
    with open('bianhao_star4.txt', 'a', encoding='utf-8') as f:
        f.write(content)
        f.write('\n')# bianhao_review2.txt
        #f.write(' ') # bianhao_review3.txt
        f.close()

def main(offset):
    url = 'https://book.douban.com/subject/1483894/reviews?rating=4&start='+ str(offset)
    html = get_one_page(url)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)


if __name__ == '__main__':
    pool = Pool()
    pool.map(main, [i*20 for i in range(12)])#15页 五星级评价 四星级12页
    pool.close()
    pool.join()


