import csv
import difflib
import pandas as pd
import os
path =os.path.join('C:'+os.sep,'Users','PBl','Desktop','Automation _data','file.xlsx')
data1 = pd.read_excel(path)
path1 =os.path.join('C:'+os.sep,'Users','PBl','Desktop','Automation _data','cts.xlsx')
data2 = pd.read_excel(path1)

def similar(seq1, seq2):
   return difflib.SequenceMatcher(a=seq1.lower(), b=seq2.lower()).ratio()

with open('output.csv', 'w',newline='') as file:
   writer = csv.writer(file)
   writer.writerow(['abc_category', 'cde_Classpath'])
   for index1 in data1.index:
       score1 = []
       print(index1)
       for index2 in data2.index:
           score = similar(data1['Category'][index1], data2['ClassPath'][index2])
           score1.append(score * 100)
       ind = score1.index(max(score1))
       product = (data1['Category'][index1],data2['ClassPath'][ind])
       writer.writerow(product)
