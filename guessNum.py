
#! /urs/bin/env python
# coding=utf-8

# 一个猜数字的小游戏

import random

r = random.randint(1, 20)

for guessTaken in range(1, 11):
    Guess = int(input("请输入数字："))

    if Guess < r:
        print('比正确答案小了')
    elif Guess > r:
        print('比正确答案大了')
    else:
        break
        
if Guess == r:
    print("答案正确，答案就是 " + str(r) + "\n结束")
    
        











