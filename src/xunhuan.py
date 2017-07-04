# -*- coding:utf-8 -*- 
'''
Created on 2017��6��29��
@author: lijj
'''
import random

#score =int(input('输入一个数字：'))
score=random.randint(1,100)
'''
if 100>=score>90:
    print('A')
elif 90>=score>60:
    print('B')
elif 60>=score>=0:
    print('C')
else:
    print('输入有误')

x,y=4,5
if x<y:
    small=x
else:
    small=y
# small=x if x<y else y
'''

favourite='lijunjian'
'''
for i in favourite :
    print(i,end=' ')
'''    
'''    
for i in favourite :
    print(i,len(i))
'''
'''
a=range(5)
print(a)
b=list(range(5))
print(b)

for i in range(2,9):
    print(i)
    '''
'''
range(0, 5)  ===a
[0, 1, 2, 3, 4] ===b
2
3
4
5
6
7
8
不包含9，[2,9)
'''
'''for i in range(2,9,3):
    print(i)'''
'''
 2
5
8
'''   
for i in range(10):
    if i%2 !=0:
        print(i)
        continue
    i+=2
    print(i)   
    