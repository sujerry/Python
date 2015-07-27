#!/usr/bin/python
#coding: utf-8

import sys

#read the data
try:
    f1 = open('./A-large-practice.in', 'r')
    f2 = open('./small-out.txt', 'w')

    #t = int(input())
    t = int(f1.readline())
    f1.readline()
    for l in range(t):
        #s = int(input())
        s = int(f1.readline())
        data = []
        for j in range(s):
            data.insert(j, [int(ti) for ti in f1.readline().split()])
            #data.insert(j, [int(ti) for ti in input().split()])



        #Creating the 'sign' table
        sign = []
        for i in range(s*s+1):
            sign.insert(i, 0)
        sign[s*s] = 1

        for i in range(s):
            for j in range( s): 
                flag = data[i][j]  
                if (i>0 and data[i-1][j]==flag+1) or (i+1<s and data[i+1][j]==flag+1) or (j>0 and data[i][j-1]==flag+1) or (j+1<s and data[i][j+1]==flag+1) :
                    sign[flag] = 1
        #Caculating the result
        flag = 1
        num = 0
        tmp = 0
        for i in range(s*s+1):
            if sign[i]==0 : 
                if i-flag+1>num : 
                    num = i - flag + 1  
                    tmp = flag
                flag = i + 1

        if s*s+1-flag>num :
            num = s * s + 1 - flag 
            tmp = flag 

        f2.write('Case #' + str(l+1) + ': ' + str(tmp) + ' ' + str(num) + '\n')
        #print('Case #' + str(l+1) + ': ' + str(tmp) + ' ' + str(num))

finally:
    if f1: 
        f1.close()
    if f2:
        f2.close()

