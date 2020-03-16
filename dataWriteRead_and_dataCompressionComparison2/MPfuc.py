# bstr json
def write(data, fileName):
    with open(fileName, 'wb') as f:
        f.write(data)
def read(fileName):
    with open(fileName, 'rb') as f:
        return f.read()
def Nread(fileName):
    from os.path import getsize
    from os.path import isfile
    from time import sleep
    while not isfile(fileName) or getsize(fileName) == 0:
        sleep(0.01)
    with open(fileName, 'rb') as f:
        return f.read()   
def Jwrite(data, fileName):
    from json import dumps    
    with open(fileName, 'wb') as f:
        f.write(bytes(dumps(data), encoding="ascii"))
    f,close()
def Jread(fileName):
    from json import load
    with open(fileName, 'rb') as f:
        return load(f)
def JNread(fileName):
    from os.path import getsize
    from os.path import isfile
    from time import sleep
    from json import load
    while not isfile(fileName) or getsize(fileName) == 0:
        sleep(0.01)
    with open(fileName, 'rb') as f:
        return load(f)
# zlib
def Zwrite(data, fileName):
    from zlib import compress
    with open(fileName, 'wb') as f: 
        f.write(compress(data, 1))
def Zread(fileName):
    from zlib import decompress
    with open(fileName, 'rb') as f:
        return decompress(f.read())
def ZNread(fileName):
    from os.path import getsize
    from time import sleep
    from zlib import decompress
    with open(fileName, 'rb') as f:
        while getsize(fileName) == 0:
            sleep(0.01)
        return decompress(f.read())
def JZwrite(data, fileName):
    from json import dumps
    from zlib import compress
    with open(fileName, 'wb') as f: 
        f.write(compress(bytes(dumps(data), encoding="ascii"), 3))
def JZread(fileName):
    from json import loads
    from zlib import decompress
    with open(fileName, 'rb') as f:
        return loads(decompress(f.read()))
def JZNread(fileName):
    from os.path import getsize
    from os.path import isfile
    from time import sleep
    from json import loads
    from zlib import decompress
    while not isfile(fileName) or getsize(fileName) == 0:
       sleep(0.1)
    with open(fileName, 'rb') as f:
        return loads(decompress(f.read()))
# xz
def Xwrite(data, fileName):
    from lzma import open as lzOpen
    with lzOpen(fileName, 'wb') as f: 
        f.write(data)
def Xread(fileName):
    from lzma import open as lzOpen
    with lzOpen(fileName, 'rb') as f:
        return f.read()
def JXwrite(data, fileName):
    from json import dumps
    from lzma import compress
    with open(fileName, 'wb') as f:
        f.write(compress(bytes(dumps(data), encoding="ascii"), preset=6))
def JXread(fileName):
    from json import load
    from lzma import open as lzOpen
    with lzOpen(fileName, 'rb') as f:
        return load(f)
def JXNread(fileName):
    from os.path import getsize
    from os.path import isfile
    from time import sleep
    from json import load
    from lzma import open as lzOpen
    while not isfile(fileName) or getsize(fileName) == 0:
        sleep(0.01)
    with lzOpen(fileName, 'rb') as f:
        return load(f)

