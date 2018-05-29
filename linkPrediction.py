# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import csv
import numpy as np
import pandas as pd
import collections

vertex_list = []

#讀csv檔
with open('Period1.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    
    for row in spamreader:
        #一行行切成3段
        string =', '.join(row).split(",",2)
        #將第二段與第三段加進list
        vertex_list.extend([string[1],string[2]])
    
    #測試陣列長度是否為row數量的2倍
    print(len(vertex_list))
    #將陣列值進行處理，排序後將重複的數值刪除，留下唯一值
    sorted(vertex_list)
    vertex_list = [item for item, count in collections.Counter(vertex_list).items() if count > 1]
    #測試陣列長度是否縮短
    print(len(vertex_list))
    
