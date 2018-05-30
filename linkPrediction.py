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


def remove_duplicates(values):
    output = []
    seen = set()
    for value in values:
        # If value has not been encountered yet,
        # ... add it to both list and set.
        if value not in seen:
            output.append(value)
            seen.add(value)
    return output


################### main ####################################
#讀csv檔 (Period1)
with open('Period1.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    
    for row in spamreader:
        #一行行切成3段
        string =', '.join(row).split(",",2)
        #將第二段與第三段加進list
        vertex_list.extend([string[1],string[2]])
    
    #將陣列值進行處理，排序後將重複的數值刪除，留下唯一值
    sorted(vertex_list)
    vertex_list = remove_duplicates(vertex_list)
    #測試陣列長度
    print(len(vertex_list))
    
#讀csv檔 (Period2)
with open('Period2.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    
    for row in spamreader:
        #一行行切成3段
        string =', '.join(row).split(",",2)
        #將第二段與第三段加進list
        vertex_list.extend([string[1],string[2]])
    
    #將陣列值進行處理，排序後將重複的數值刪除，留下唯一值
    
    vertex_list = remove_duplicates(vertex_list)
    sorted(vertex_list)
    #測試陣列長度
    print(len(vertex_list))      
    
    """測試有無重複值
    for content1 in vertex_list:
        count=0
        for content2 in vertex_list:
            if content1==content2:
                count+=1
            if count>=2:
                print(content1)
    """           
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
