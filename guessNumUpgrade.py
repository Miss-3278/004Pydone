
#! /urs/bin/env python
# coding=utf-8

import random

# 建一个类

class guessNum(object):
    
    # 初始化
    def __init__(self):
        self.count = 0 # 统计猜测次数
        self.usrNums = [] # 用户输入的猜测数字
        self.sysNum = '' # 系统生成的数字
        self.results = [] # 猜测结果
        self.winner = False
        
    # 打印游戏规则
    def printRules(self) :  
        print("""游戏用 0-9 生成一个 4 位数，每个数位上的数字不重复，且首位数字不为零，如 1942。
用户输入 4 位数进行猜测，程序返回相应提示：A代表数字正确位置正确，B代表数字正确位置错误。 
如正确答案为 3689，而猜的人猜 3568，则是 1A2B，其中有一个 3 的位置对了，记为1A;
6 和 8 这两个数字对了，而位置没对，因此记为 2B，合起来就是 1A2B。 
接着猜的人再根据出题者的几A几B继续猜，直到猜中（即 4A0B）为止，最多有 10 次猜测机会。""") 

    # 随机生成一个四位数字的字符串
    def randomNum(self):
        numStr = '0123456789'
        randomNum = ''
        for i in range(4):
            n = random.choice(numStr)
            randomNum += n
            numStr = numStr.replace(n, '')
        self.sysNum = randomNum

    # 输入数字，类型也是字符串
    def inputNum(self):
        self.count += 1  
        num = input('输入一个四位数字数字: ')
        self.usrNums.append(num)  
        return num
    
    # 判断
    def numJudge(self, sysNum, usrNum):
        countA = 0  
        countB = 0  
        for i in range(4) :  
            if usrNum[i] in sysNum: # 字符串切片  
                if i == sysNum.find(usrNum[i]) :  
                    countA += 1  
                else :  
                    countB += 1  
        result = '%dA%dB' % (countA, countB)  
        self.results.append(result)  
        if countA == 4 :  
            self.winner = True
        
            
    # 显示猜测结果
    def showResults(self, usrNums, results) :  
        print('-' * 20)  
        for i in range(self.count) :  
            print('%d. %s ---> %s' % (i + 1, usrNums[i], results[i]) )  
        print('-' * 20)  
        if self.winner :  
            print('共猜测: %d 次。' % self.count)
            print('恭喜你！答对了！！' )  
            
    # 运行
    def run(self):
        self.printRules()
        self.randomNum()
        while self.count < 10 and not self.winner:
            num = self.inputNum()
            self.numJudge(self.sysNum, num)
            self.showResults(self.usrNums, self.results)
        print("游戏结束！再来一局！！")
        
#主函数  
def main():  
    guessNumber = guessNum()  
    guessNumber.run()  
if __name__ == '__main__' :  
    main()  






