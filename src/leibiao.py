# -*- coding:utf-8 -*- 
'''
Created on 2017��7��2��
@author: lijj
'''
member =['小甲鱼','小布丁','米兔',3.1415,[1,3,4]]

#member.append() 加一个元素
member.append('福禄娃娃')
print(member)
'''['小甲鱼', '小布丁', '米兔', 3.1415, [1, 3, 4], '福禄娃娃']'''

#member.extend()  加多个元素，列表形式
member.extend(['意境',3.124])
print(member)
'''['小甲鱼', '小布丁', '米兔', 3.1415, [1, 3, 4], '福禄娃娃', '意境', 3.124]  '''

#member.insert()  加入指定位置
member.insert(1, 'ying')
print(member)
''' ['小甲鱼', 'ying', '小布丁', '米兔', 3.1415, [1, 3, 4], '福禄娃娃', '意境', 3.124]
 '''
member.extend(list([0,3,5]))
print(member)

''' ['小甲鱼', 'ying', '小布丁', '米兔', 3.1415, [1, 3, 4], '福禄娃娃', '意境', 3.124, 0, 3, 5]'''
member.extend(range(10,15))
print(member)
''' ['小甲鱼', 'ying', '小布丁', '米兔', 3.1415, [1, 3, 4], '福禄娃娃', '意境', 3.124, 0, 3, 5, 10, 11, 12, 13, 14]'''
