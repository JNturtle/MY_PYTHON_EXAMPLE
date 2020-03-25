"""在 iterNext() 中，刪除[0]值"""

def iterNext(iterable):
    i = 0
    while iterable:
        try:
            item = iterable[i]
            yield item
            del iterable[0]
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
print(a)
