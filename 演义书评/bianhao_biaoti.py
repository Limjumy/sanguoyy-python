#!/usr/bin/python
# encoding:utf-8

import os
import codecs


##遍历filePath下的所有txt文件
# 读取txt文件的第一行 为列表

def bianli_docuname(filepath,list):
    pathDir = os.listdir(filepath)
    n=0
    for allDir in pathDir:  # 对于每一篇评论，每一篇评论是列表list的一个元素
        child = os.path.join('%s%s' % (filepath, allDir))
        #print(child)  # 遍历了目录下的一个个文件名字
        n+=1
        # 读取文件child
        with codecs.open(child, "r", "utf-8") as f:
            counts = 0
            for line in f.readlines():
                if counts==0: # 只读第一行
                    counts=counts+1
                    list.append(line)
                    print(child)
                else:
                    continue
    print(n)
    return list

if __name__ == '__main__':
    review_biaoti=[]

    filePath = "E:\\python_project\\三国演义\\演义书评\\演义长评论\\"
    bianli_docuname(filePath,review_biaoti)
    print(len(review_biaoti))
    for line in review_biaoti: # 将544条评论标题读入了review中
        print(line)
        #print(type(line)) #问题就在于这里的line是列表形式

# 将评论编号写入csv
# 将评论标题希尔同一个csv

# 此处要将编号排个序，因为读取长评论文件夹时，文件夹的顺序是正的。

# 写入
    with codecs.open("reviews_biaoti.txt", "a+","utf-8") as f:
        for line in review_biaoti:
            f.write(line)
