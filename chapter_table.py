#!/usr/bin/python
# encoding:utf-8

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import jieba
# from wordcloud import WordCloud,ImageColorGenerator
# from ggplot import *

## 读取三国演义（罗贯中）文本
sanguoyy = pd.read_csv("sanguoyy.txt",header=None,names = ["sanguoyy"])
