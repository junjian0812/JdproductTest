# -*- coding:utf-8 -*- 
'''
Created on 2017年7月3日
@author: lijj
'''
#元祖tuple
tuple1=(1,2,3,4,6)
print(type(tuple1))
'''<class 'tuple'>'''
#，表示一个元祖
tuplle2=2,67,56
print(type(tuplle2))
'''<class 'tuple'>'''
# 常见一个空元祖
tuple3=()
print(type(tuple3))
'''<class 'tuple'>'''
tem=8*(8)
print(tem)
'''64'''
tem2=8*(8,)
print(tem2)
'''(8, 8, 8, 8, 8, 8, 8, 8)'''
#插入一个元素.在第2个元素插入‘意境’
temp=('我爱','北京','天安门','是啊')
temp=temp[:2]+('意境',)+temp[2:]
print(temp)
'''('我爱', '北京', '意境', '天安门', '是啊')'''
#插入一个格式不一样的元素
tuple1=tuple1[:2]+('意境',)+tuple1[2:]
print(tuple1)
'''(1, 2, '意境', 3, 4, 6)'''
#删除元祖中的某个元素，几乎是不怎么用的 ,del删除整个元祖基本也是不用的
del tuple1
#print(tuple1)

#操作符可以使用在元祖：拼接操作符(+,两边必须都是元祖)，重复操作符(*8)，关系操作符（>,<,=），成员操作符（in，not in）,逻辑操作符(and,or)
print( '我爱' in temp )
'''True'''

