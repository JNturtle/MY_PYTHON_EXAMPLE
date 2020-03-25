"""球池 yield 類別 class版"""
import random

class BallPool():
    def __init__(self):
        self.BallPool = []
        [self.BallPool.append("R") for _ in range(20)]
        [self.BallPool.append("Y") for _ in range(10)]
        self.times = 0
    def __call__(self):
        return next(self.__drawBall__())
    def __str__(self):
        return str(sorted(self.BallPool)) # sorted()會回傳新串列，自身沒變。而List.sort()是修改自身
    def __iter__(self):
        return self.__drawBall__() # yeild得到一個產生器，回傳這個產生器給for in使用
    def __drawBall__(self):
        while self.BallPool:
            random.shuffle(self.BallPool) 
            ball =  self.BallPool.pop(0)
            self.times += 1
            yield ball, self.times
            if ball == "Y": self.BallPool.extend(["R", "Y"])
            if ball == "R": self.BallPool.append("B")
            if ball == "B": self.BallPool.append("G")
            if ball == "G": self.BallPool.append("W")
            if ball == "W": break

myBallPool = BallPool()
print("當前球池", myBallPool)
print("call", myBallPool()) # 先抽一球
print("For in 迴圈", ",".join([str(each) for each in myBallPool]))
print("球池剩餘", myBallPool)
print("For in 迴圈2", ",".join([str(each) for each in myBallPool]))
print("球池剩餘", myBallPool)