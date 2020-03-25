"""
球池 yield 類別 class版2
新增 self.__generator__ ，不會有一直產生新的產生器。 
"""
import random

class BallPool():
    def __init__(self):
        self.BallPool = []
        [self.BallPool.append("R") for _ in range(20)]
        [self.BallPool.append("Y") for _ in range(10)]
        self.times = 0
        self.__generator__ = self.__drawBall__()
    def __call__(self):
        return next(self.__generator__)
    def __str__(self):
        return str(sorted(self.BallPool)) 
    def __iter__(self):
        return self.__generator__ 
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
