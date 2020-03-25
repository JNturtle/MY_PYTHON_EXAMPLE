"""抽球"""
import random

BallPool = []
[BallPool.append("R") for _ in range(20)]
[BallPool.append("Y") for _ in range(10)]
  
def drawBall():
    while BallPool:
        random.shuffle(BallPool) 
        ball =  BallPool.pop(0)
        yield ball
        if ball == "Y": BallPool.extend(["R", "Y"])
        if ball == "R": BallPool.append("B")
        if ball == "B": BallPool.append("G")
        if ball == "G": BallPool.append("W")
        if ball == "W": break

Action_drawBall = drawBall()
print(",".join([str((i+1,ball)) for i, ball in enumerate(Action_drawBall)]))
print(BallPool, len(BallPool))
