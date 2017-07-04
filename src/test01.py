# -*- coding:utf-8 -*- 
'''
Created on 2017年6月28日
@author: lijj
'''
import random
from builtins import int
secret=random.randint(1,100)
print("------我的测试程序----------")
print(secret)
#tem = input("不放输入一个数字：")
#guess =int(tem)
guess=0
while guess !=secret:
    tem =input('输入一个数字吧：')
    guess =int(tem)
    if guess==secret:
        print('我曹，猜对了！！')
    else:
        if guess >secret:
            print('歌，大了')
        else:
            print('嘿，小了')
print('游戏结束，不玩啦')
