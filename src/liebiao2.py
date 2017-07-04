# -*- coding:utf-8 -*- 
'''
Created on 2017��7��2��
@author: lijj
'''
member =['小甲鱼','小布丁','米兔',3.1415,[1,3,4]]

#调换元素位置位置
temp=member[0]
member[0]=member[1]
#print(member)
member[1]=temp
print(member)
''' ['小布丁', '小甲鱼', '米兔', 3.1415, [1, 3, 4]]'''
#从列表中删除元素remove()
member.remove('米兔')
print(member)
'''['小布丁', '小甲鱼', 3.1415, [1, 3, 4]]'''

#del 删除  del member删除整个数组
del member[1]
print(member)
'''['小布丁', 3.1415, [1, 3, 4]] '''
member.extend(['哈哈','呵呵','你好']) 
print(member)
'''['小布丁', 3.1415, [1, 3, 4], '哈哈', '呵呵', '你好']'''  

#pop() 删除最后一个元素
member.pop()
print(member)
'''['小布丁', 3.1415, [1, 3, 4], '哈哈', '呵呵']'''
name=member.pop()
print(name)
'''呵呵'''
#pop(1)获取指定元素
member.pop(1)
print(member)
''' ['小布丁', [1, 3, 4], '哈哈']'''
member.extend(['星期一','星期二','你好']) 
print(member)
''' ['小布丁', [1, 3, 4], '哈哈', '星期一', '星期二', '你好']'''
#列表分片返回[0,3)索引的元素
print(member[:3])
'''['小布丁', [1, 3, 4], '哈哈']'''
#返回1到最后一个索引元素
print(member[1:])
''' [[1, 3, 4], '哈哈', '星期一', '星期二', '你好']'''
#返回所有元素
print(member[:])
'''['小布丁', [1, 3, 4], '哈哈', '星期一', '星期二', '你好']'''

#拷贝数组
member2=member[:]
print(member2)
'''['小布丁', [1, 3, 4], '哈哈', '星期一', '星期二', '你好']'''
member3=member
print(member3)
''' ['小布丁', [1, 3, 4], '哈哈', '星期一', '星期二', '你好']'''

'''
总结：
member3=member（1） 与member2=member[:]（2） 赋值的区别
（1）是索引的指向，（2）是值的拷贝；在内存中（1），还是1个值，但是（2）是两个不同的存值不同的索引
如果对member进行sort（）排序后，member3的值会跟着变，member4的值不会变
'''