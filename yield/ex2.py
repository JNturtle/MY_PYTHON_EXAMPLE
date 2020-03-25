def yield_for(iterable):
    itertor = iterable.__iter__()
    print("yield_for start")
    while 1:
        try:
            item = next(itertor)
            yield item
        except StopIteration:
            """一旦 next() 無法再取得值，就會產生此錯誤"""
            print("yield_for StopIteration")
            break
        except:
            print("yield_for Other Error")
            break

a = list(range(10))
aG = yield_for(a)
for x in aG:
    print(x)
    del a[0]
#
print("-"*20)
#
a = range(10)
aG = yield_for(a)
for x in aG:
    print(x)
#
print("-"*20)
#
a = {} 
for i in range(10): a[str(i)] = None
aG = yield_for(a)
"""
字典dict的__iter__()等於keys()
"""
for x in zip(aG, a, a.keys(), a.__iter__()):
    print(x)
