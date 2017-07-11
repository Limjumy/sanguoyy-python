#!/usr/bin/python
# encoding:utf-8


import jieba
import codecs
import jieba.posseg as pseg

names = {}
relationships = {}
lineNames = []

# counts names
jieba.load_userdict("names_sanguoyy.txt")  # 加载字典
jieba.load_userdict("names_pl.txt")
#jieba.load.userdict("sanguo.dict")

with codecs.open("2 sanguoyy.txt", "r", "utf-8") as f:
    for line in f.readlines():
        poss = pseg.cut(line)  # 分词并返回该词词性
        lineNames.append([])  # 为新读入的一段添加人物名称列表
        for w in poss:
            if w.flag != "pl" :
                continue  # 当分词长度小于2或该词词性不为nr时认为该词不为人名
            lineNames[-1].append(w.word)  # 为当前段的环境增加一个人物
            if names.get(w.word) is None:
                names[w.word] = 0
                relationships[w.word] = {}
            names[w.word] += 1  # 该人物出现次数加 1

##打印names看一看
with codecs.open("3 places_times_sanguoyy.txt", "a+", "utf-8") as f:
    f.write("places in sanguo\r\n")
    for name, times in names.items():
        f.write(name + " " + str(times) + "\r\n")

# explore relationships
for line in lineNames:  # 对于每一段，因为readlines就是一段一段地读取文本，不是一行一行。
    for name1 in line:
        for name2 in line:  # 每段中的任意两个人
            if name1 == name2:
                continue
            if relationships[name1].get(name2) is None:  # 若两人尚未同时出现则新建项
                relationships[name1][name2] = 1

            else:
                 relationships[name1][name2] = relationships[name1][name2] + 1  # 两人共同出现次数加 1




# output
with codecs.open("3 places_relationships_sanguoyy.txt", "a+", "utf-8") as f:
    f.write("Source Target Weight\r\n")
    for name, edges in relationships.items():
        for v, w in edges.items():
            if w > 3:
                f.write(name + " " + v + " " + str(w) + "\r\n")



