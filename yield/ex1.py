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
data = range(10000000)
# yield法
timer = perf_counter()
data_batch_yield = batch_yield(data, n=13)
ustTime = perf_counter() - timer
useSize = sys.getsizeof(data) + sys.getsizeof(data_batch_yield) + sys.getsizeof(batch_yield)
print("yield 花費時間{:}秒 總共使用size: {:}".format(ustTime, useSize))
# return法
timer = perf_counter()
data_batch_return = batch_return(data, n=13)
ustTime = perf_counter() - timer
useSize = sys.getsizeof(data) + sys.getsizeof(data_batch_return) + sys.getsizeof(batch_return)
print("return 花費時間{:}秒 總共使用size: {:}".format(ustTime, useSize))
# 分隔線
print("-"*10)
# 抽檢十個index
testIndex = [random.randrange(0, 10000000//13, 1) for _ in range(10)]
for i, (d1, d2) in enumerate(zip(data_batch_yield, data_batch_return)):
    if i in testIndex: 
        print(d1, d2)        
