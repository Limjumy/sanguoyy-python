#!/usr/bin/python
# encoding:utf-8

import re

x_sen=[]
x="我是张飞。张飞杀我。刘备是忠诚。曹操没人性"
x_sen=x.split('。')
print(x_sen)
x_sen_fei=[]

for line in x_sen:
    if '张飞' in line:
        x_sen_fei.append(line)

print(x_sen_fei)