# -*- coding:utf-8 -*- 
'''
Created on 2017��6��29��
@author: lijj
'''
'''
python �������
整形，布尔型，浮点型，e记法
'''
#a=0.000000000000000000000000000000025
#b=15e10
#print(a)
#print(b)
'''
2.5e-32
150000000000.0
'''
#true 1,false 0
#int,str,float

#a='520'
#b=int(a)
#print(b)
c=5
d=1.93458
e=c+d
f=int(d)
g=float(c)
m=str(d)
n=True
print(e)
print(f)
print(g)
print(m)
'''
6.93458
1
5.0
'''
#type() 获取变量类型
print(type(m))
print(type(True))

#isinstance(obj, class_or_tuple) 判断类型是否一致，返回bool值
print(isinstance(m,str))
print(isinstance(n,bool))

mem='你好'
mem2='是的'
mem3=mem+mem2
mem4=mem*4
print(mem3)
print(mem4)
print(mem3,mem4)
'''6.93458
1
5.0
1.93458
<class 'str'>
<class 'bool'>
True
True
你好是的
你好你好你好你好
你好是的 你好你好你好你好
'''


