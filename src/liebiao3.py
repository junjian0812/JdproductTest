# -*- coding:utf-8 -*- 
'''
Created on 2017��7��2��
@author: lijj
'''

#列表有的方法   测试
#print(dir(list))
'''
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

'''
list1=[123]
list2=[234]
tem=(list1>list2)
print(tem)
'''False'''
#只对比第一个元素  远程仓库
list3=[123,456]
list4=[456,123]
print(list3>list4)
'''False'''

#字符串用+进行串，用*进行多次。
#列表尽可能用append(),extend()进行加入元素
list3 *=3
list3 *=5
print(list3)
''' [123, 456, 123, 456, 123, 456, 123, 456, 123, 456, 123, 456, 123, 456, 123, 456, 123, 456, 123, 456, 123, 456, 123, 456, 123, 456, 123, 456, 123, 456]
'''
#
list1+='小甲鱼'
print(list1)
'''[123, '小', '甲', '鱼']'''
#
tem2=123 in list3
print(tem2)
'''True'''
tem3= '小甲鱼' not in list3
print(tem3)
'''True'''
#123出现的次数
tem4=list3.count(123)
print(tem4)
'''15'''
#123第一个索引的位置
tem5=list3.index(123)
print(tem5)
'''0'''
#123，从第4个元素开始到最后第一次出现的索引
tem6=list3.index(123,3,len(list3) )
print(tem6)
'''4'''
list2.extend([123,456,[123,890]])
print(list2)
'''[234, 123, 456, [123, 890]]
'''
tem7= 890 in list2
print(tem7)
'''False '''
tem8=890 in list2[3]
print(tem8)
'''True'''
print(list2[3][0])
'''123'''

