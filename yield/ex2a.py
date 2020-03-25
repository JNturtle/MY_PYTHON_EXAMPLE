"""類似 for in 的迴圈"""

def iterNext(iterable):
    i = 0
    while 1:
        try:
            item = iterable[i]
            yield item
            i += 1
        except:
            break

def yield_for_iterNext(iterable):
    itertor = iterNext(iterable)
    print("yield_for_iterNext start")
    while 1:
        try:
            item = next(itertor)
            yield item
        except StopIteration:
            """一旦 next() 無法再取得值，就會產生此錯誤"""
            print("yield_for_iterNext StopIteration")
            break
        except:
            print("yield_for_iterNext Other Error")
            break

a = list(range(10))
aG = yield_for_iterNext(a)
for x in aG:
    print(x)
    del a[0]
#
print("-"*20)
#
a = range(10)
aG = yield_for_iterNext(a)
for x in aG:
    print(x)
#
print("-"*20)
#
a = {} #
for i in range(10): a[str(i)] = None
aG = yield_for_iterNext(a)
for x in aG:
    print(x)
for x in zip(a, a.keys(), a.__iter__()):
    print(x)
