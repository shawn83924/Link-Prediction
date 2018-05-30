# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import csv
import numpy as np

vertex_list = []

#刪除陣列中重複數值的函示
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
    
    #將陣列值進行處理，將重複的數值刪除後排序，留下唯一值
    vertex_list = remove_duplicates(vertex_list)
    sorted(vertex_list)
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
    
    #將陣列值進行處理，將重複的數值刪除後排序，留下唯一值
    vertex_list = remove_duplicates(vertex_list)
    sorted(vertex_list)
    #測試陣列長度
    print(len(vertex_list))      
    
    
#宣告NxN的陣列，且內容均為0
n=len(vertex_list)      
Matrix = np.full( ( n, n ),0 )

#開始填值，將Period2 的 link 以1填入
print("start Period2")
count=0
with open('Period2.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        #一行行切成3段
        string =', '.join(row).split(",",2)
        i= vertex_list.index(string[1])
        j= vertex_list.index(string[2])
        Matrix[i][j] = 1
        count+=1
#98353
print(count)        
print("done")
    
#開始填值，將Period1 的 link 以2填入
print("start Period1")
count=0
with open('Period1.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        #一行行切成3段
        string =', '.join(row).split(",",2)
        i= vertex_list.index(string[1])
        j= vertex_list.index(string[2])
        Matrix[i][j] = 2
        count+=1
#154836
print(count)        
print("done")    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
