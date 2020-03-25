import sys
import random
from time import perf_counter


def batch_yield(iterable, n=1):
    l = len(iterable)
    for ndx in range(0, l, n): # 跑在迴圈裡
        yield iterable[ndx:min(ndx + n, l)]

def batch_return(iterable, n=1):
    l = len(iterable)
    return [iterable[ndx:min(ndx + n, l)] for ndx in range(0, l, n)]

# 產生一串可迭代的對象
data = range(100000)
data_batch_return = batch_return(data, n=13)
# 分隔線
print("-"*10)
# 抽檢十個index
testIndex = [random.randrange(0, 100000//13, 1) for _ in range(10)]

# generator會保存進度
# ex1
data_batch_yield = batch_yield(data, n=13)
[next(data_batch_yield) for _ in range(800)]  # data_batch_yield 先 next() 八百次
for i, (d2, d1) in enumerate(zip(data_batch_return, data_batch_yield)):
    if i in testIndex: 
        print(d1, d2) 
# ex2
data = range(10)
a = data.__iter__()
for i, item in enumerate(a):
    print(i, item)
    if item % 4 == 3: break
for i, item in enumerate(a):
    print(i, item)
    if item % 4 == 3: break
for i, item in enumerate(a):
    print(i, item)
    if item % 4 == 3: break
for i, item in enumerate(a):
    print(i, item)
    if item % 4 == 3: break

