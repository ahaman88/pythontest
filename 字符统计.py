#!/usr/bin/python
#_*_coding:UTF-8-*-
import os,fileinput,re

def jshu(str_a):
    str_zip=[]
    count_temp=[]
    for i in str_a:
        if i not in str_zip:
            str_zip.append(i)
    for i in range(len(str_zip)):
        p=str_a.count(str_zip[i])
        count_temp.append([str_zip[i],p])
    count_p (count_temp)
    return

def count_p(a):
    a.sort(key=lambda x:x[1],reverse=True)
    for i in range(len(a)):
        print('字符：',a[i][0],'字数为',a[i][1])
    return

sy="[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）]+\n -:;<=>)"
str_temp=""

with open ('dump.txt','r') as f:
    for line in fileinput.input('dump.txt'):
        for i in line:
            if i not in sy:
                str_temp+=i.lower()

jshu(str_temp)



#print(re.sub("[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）]+",str_temp))
#print(type(str_x),str_x)



