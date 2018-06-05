# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import csv
import numpy as np
from sklearn import svm
import pandas as pd
from sklearn.linear_model import SGDClassifier

vertex_list = []
train_data = []
label = []
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
        vertex_list.extend([ int(string[1]) , int(string[2]) ])
    
    #將陣列值進行處理，將重複的數值刪除後排序，留下唯一值
    vertex_list = remove_duplicates(vertex_list)
    sorted(vertex_list)
    #測試陣列長度
    print( "Period1 node數: {}".format(len(vertex_list)) )
    
#讀csv檔 (Period2)
with open('Period2.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    
    for row in spamreader:
        #一行行切成3段
        string =', '.join(row).split(",",2)
        #將第二段與第三段加進list
        vertex_list.extend([ int(string[1]) , int(string[2]) ])
    
    #將陣列值進行處理，將重複的數值刪除後排序，留下唯一值
    vertex_list = remove_duplicates(vertex_list)
    sorted(vertex_list)
    #測試陣列長度
    print("Period1,2 node總數: {}".format(len(vertex_list))) 

#讀csv檔 (TestData)
TestData_node = []
with open('TestData.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    
    for row in spamreader:
        #一行行切成3段
        string =', '.join(row).split(",",2)
        #將第二段與第三段加進list
        TestData_node.extend([ int(string[1]) , int(string[2]) ])
    
    #將陣列值進行處理，將重複的數值刪除後排序，留下唯一值
    TestData_node = remove_duplicates(TestData_node)
    sorted(TestData_node)
    #測試陣列長度
    print("TestData node總數: {}".format(len(TestData_node)))
   
#宣告NxN的陣列，且內容均為0
n=len(vertex_list)      
Matrix = np.full( ( n, n ),0 )

#開始填值，將Period2 的 link 以1填入
print("start Period2")
#讀csv檔 ( Period2 )
with open('Period2.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        #一行行切成3段
        string =', '.join(row).split(",",2)
        #將此link標註1
        i= vertex_list.index( int(string[1]) )
        j= vertex_list.index( int(string[2]) )
        Matrix[i][j] = 1
        train_data += [ [ int(string[1]) , int(string[2]) ] ]
        label += [  1  ]
               
print("Period2 done")
    
#開始填值，將Period1 的 link 以1填入
print("start Period1")
#讀csv檔 ( Period1 )
with open('Period1.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        #一行行切成3段
        string =', '.join(row).split(",",2)
        #將此link標註2
        i= vertex_list.index( int(string[1]) )
        j= vertex_list.index( int(string[2]) )
        Matrix[i][j] = 1
        train_data += [ [ int(string[1]) , int(string[2]) ] ]
        label += [  0  ]
            
print("Period1 done")    



#開始用SVM進行trainning
print("start trainning1")
'''
k=0.01
for i in range(n):
    if vertex_list[i] in TestData_node :
        for j in range(n):
            if (vertex_list[j] in TestData_node and Matrix[i][j] != 1 and i!=j ):
                train_data += [ [ vertex_list[i] , vertex_list[j] ] ]
                label += [  Matrix[i][j]  ]
    
    if( i/(n/100) > k ):
        print( "目前進度: {}".format( i/(n/100) ) )
        k+=0.01
'''
print("start trainning2")
classifier = SGDClassifier(loss="hinge", penalty="l2")
classifier.fit( train_data , label )              
print("finish trainning")       

#讀csv檔 (TestData)
answer = []
with open('TestData.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    
    for row in spamreader:
        #一行行切成3段
        string =', '.join(row).split(",",2)
        #i= vertex_list.index(string[1])
        #j= vertex_list.index(string[2])
        #進行辨識
        result = classifier.predict([ [ int(string[1]) , int(string[2]) ] ])
        
        answer.extend([ (result[0]+1)%2 ])


#寫檔 
target_id=np.arange(10000)
dataframe = pd.DataFrame({'target id':target_id , 'label':answer})
dataframe.to_csv("result.csv",index=False,sep=',')

    
    
    
    
    
    
    
    
    
    
    
    
    
