#!/usr/bin/python
# encoding:utf-8
import re
import requests
from multiprocessing import Pool

from requests.exceptions import RequestException


# 修改正则表达式后，程序运行很快，93条长评论
# 去合适的网页打印出所需要的用户评论，且每条评论写入不同的txt中
# 将编码存入列表
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


def add_urll(urll,list):# 爬取长评论，将list的元素加入urll ,这里list是列表的元素 即bianhao[0]
    urll=urll+list
    return urll


def main(offset):
    bianhao=[]
    a=[]
    url = 'https://book.douban.com/subject/1926289/reviews?start='+ str(offset)
    urll='https://book.douban.com/review/'
    html = get_one_page(url)
    for item in parse_one_page(html):
        print(item)
        bianhao.append(item) #bianhao 为每一页长评论的编码，一次循环是一页
    print(bianhao)
    # 爬取长评论
    for line in bianhao:# 对于每一页的每一个编码，遍历
        urll = add_urll(urll, line)  # urll为网址,line是列表的每个元素
        print(urll)
        docu_name=line+'.txt'       # 存储的文件名，是编码.txt
        content = requests.get(urll).text
        urll='https://book.douban.com/review/'
        # 筛选长评论 推荐等级（几颗星“力荐”）及其标题
        pattern = re.compile(
            '<h1.*?summary.*?>(.*?)</span>.*?<span.*?allstar.*?title="(.*?)"></span>.*?<div.*?review-content.*?>.*?(.*?)<script.*?text.*?>', re.S)
        results = re.findall(pattern, content)
        with open(docu_name, 'a', encoding='utf-8') as f:
            for result in results:  # 列表中的列表
                for i in result:
                    f.write(i)
                    f.write('\n')
            f.close()





# 将编码加入网址
#url='https://book.douban.com/review/'
#a=['1','2']
#print(type(a))
#url=url+a[0]
#print(url) 试验成功，字符串+列表元素=新的字符串

if __name__ == '__main__':
    pool = Pool()
    pool.map(main, [i*20 for i in range(5)])#5页
    pool.close()
    pool.join()
