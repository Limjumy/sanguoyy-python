#!/usr/bin/python
# encoding:utf-8

# 将一个段落中出现的人物以及地点筛选出来
# 并且将人物与地点去重

import jieba
import codecs
import jieba.posseg as pseg

line_roles_places=[]
names_rp={}
relationships={}
happen={}

jieba.load_userdict("names_sanguoyy.txt")  # 加载字典
jieba.load_userdict("names_pl.txt")  # 加载字典
with codecs.open("2 sanguoyy.txt", "r", "utf-8") as f:
    for line in f.readlines():
        poss = pseg.cut(line)  # 分词并返回该词词性
        line_roles_places.append([])  # 为新读入的一段添加列表
        for w in poss:
            print ('poss '+ w.word+w.flag)
            if w.flag != "na" and w.flag != "pl":  # 当该词语不是人名或者地名时
                continue
            line_roles_places[-1].append(w.word)# 将人名和地名全部汇集到 line_roles_places列表中

#print line_roles_places



with codecs.open("2 roles and places.txt", "a+", "utf-8") as f:
    for line in line_roles_places:  # 每一个段落，即每一个列表
        f.write('\r\n')##换行终于成功了！
        #f.write('\n')
        l2 = []
        #l2 = list(set(line))# 去重 法一：此处去重方法的缺点：顺序会乱
        for i in line:
            if not i in l2:
                l2.append(i) # 去重 法二：顺序不乱
        for list in l2:   #对于列表中的每一个元素
            f.write(list)
            f.write(' ')  # 注意空格
    #f.write('222'+'\n\n')






