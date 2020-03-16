"""引入多進程用的函式"""
from MPfuc import *
import json, zlib, lzma
import multiprocessing as mp
from time import perf_counter
def runbj(WRS, data):
    """ string json """
    useTimer = perf_counter()      
    writeTimer = perf_counter()  
    with open(WRS.fileName, 'wb') as f:
        f.write(bytes(json.dumps(data),encoding = "ascii"))
    f.close()
    readTimer = perf_counter()     
    with open(WRS.fileName, 'rb') as f:
        result = json.load(f)
    f.close()
    endTimer = perf_counter()
    WRS.addRecord(useTimer, writeTimer, readTimer, endTimer)
    WRS.printThisStat()
def runZlib(WRS, data, compressLevel = 6):
    """ json zlib"""
    if WRS.compresslevel: compressLevel = WRS.compresslevel
    useTimer = perf_counter()      
    writeTimer = perf_counter() 
    with open(WRS.fileName, 'wb') as f: 
        f.write(zlib.compress(bytes(json.dumps(data), encoding="ascii"), level=compressLevel))
    f.close()
    readTimer = perf_counter()     
    with open(WRS.fileName, "rb") as f:
        result = json.loads(zlib.decompress(f.read()))
    f.close()
    endTimer = perf_counter()

    WRS.addRecord(useTimer, writeTimer, readTimer, endTimer)
    WRS.printThisStat()
def runXz(WRS, data, compressLevel = 6):
    """ json xz"""
    if WRS.compresslevel: compressLevel = WRS.compresslevel
    useTimer = perf_counter()      
    writeTimer = perf_counter() 
    with lzma.open(WRS.fileName, 'wb', preset=compressLevel) as f: 
        f.write(bytes(json.dumps(data), encoding="ascii"))
    f.close()
    readTimer = perf_counter()     
    with lzma.open(WRS.fileName, 'rb') as f: 
        res = json.load(f)
    f.close()
    endTimer = perf_counter()
    WRS.addRecord(useTimer, writeTimer, readTimer, endTimer)
    WRS.printThisStat()
def runMpbj(WRS, data, processes = 4):
    def MPwrite(data, fileName, extension, processes = 3):
        """mpbj 先轉換成bytes再分別寫入"""
        mpPool = mp.Pool(processes=processes) # 定义CPU核数量为3    
        bstrData = bytes(json.dumps(data), encoding="ascii")
        sliceUint = len(bstrData) // processes 
        sliceIdx = [None] + [sliceUint*(i+1) for i in range(processes-1)] + [None]               
        mpPool.starmap_async(write, [(bstrData[s[0]:s[1]], fileName + "_{:}.{:}".format(i, extension)) for i,s in zip(range(processes), [(sliceIdx[i], sliceIdx[i+1])for i in range(processes)])])
        mpPool.close()
        mpPool.join()
    def MPread(fileName, extension, processes = 3):
        """mpbj 先將資料分送再轉換型態寫入，多核讀取"""
        mpPool = mp.Pool(processes=processes)
        res = b""
        for i in range(processes):
            with open(fileName + "_{:}.{:}".format(i, extension), 'rb') as f:
                res += f.read()                 
        return json.loads(res)
    def MPread3(fileName, extension, processes = 3):
        """mpbj 先將資料分送再轉換型態寫入，多核讀取"""
        mpPool = mp.Pool(processes=processes)
        res = b""
        for each in mpPool.map_async(read, [fileName + "_{:}.{:}".format(i, extension) for i in range(processes)]).get():
            res += each
        return json.loads(res)
    fn, en = WRS.fileName.split(".")
    useTimer = perf_counter()      
    writeTimer = perf_counter() 
    MPwrite(data, fn, en, processes = processes)
    readTimer = perf_counter()  
    result = MPread(fn, en, processes = processes)
    endTimer = perf_counter()
    WRS.addRecord(useTimer, writeTimer, readTimer, endTimer)
    WRS.printThisStat()
def runMpbjn(WRS, data, processes = 4):
    def MPNwrite(data, fileName, extension, processes = 3):
        """mpbj 先轉換成bytes再分別寫入"""
        mpPool = mp.Pool(processes=processes) # 定义CPU核数量为3 
        timer = perf_counter()   
        bstrData = bytes(json.dumps(data), encoding="ascii")
        sliceUint = len(bstrData) // processes 
        sliceIdx = [None] + [sliceUint*(i+1) for i in range(processes-1)] + [None]               
        mpPool.starmap_async(write, [(bstrData[s[0]:s[1]], fileName + "_{:}.{:}".format(i, extension)) for i,s in zip(range(processes), [(sliceIdx[i], sliceIdx[i+1])for i in range(processes)])])
    def MPNread2(fileName, extension, processes = 3):
        """mpbj 先將資料分送再轉換型態寫入，多核讀取"""
        mpPool = mp.Pool(processes=processes)
        fileNames = [fileName + "_{:}.{:}".format(i, extension) for i in range(processes)]
        res = b""
        p1 = mpPool.apply_async(Nread, args = (fileNames[0],))
        p2 = mpPool.apply_async(Nread, args = (fileNames[1],))
        p3 = mpPool.apply_async(Nread, args = (fileNames[2],))
        p4 = mpPool.apply_async(Nread, args = (fileNames[3],))        
        return json.loads(p1.get() + p2.get() + p3.get() + p4.get())
    def MPNread(fileName, extension, processes = 3):
        """mpbj 先將資料分送再轉換型態寫入，多核讀取"""
        mpPool = mp.Pool(processes=processes)
        res = b""
        for each in mpPool.map_async(Nread, [fileName + "_{:}.{:}".format(i, extension) for i in range(processes)]).get():
            res += each
        return json.loads(res)
    fn, en = WRS.fileName.split(".")
    useTimer = perf_counter()      
    writeTimer = perf_counter() 
    MPNwrite(data, fn, en, processes = processes)
    readTimer = perf_counter()  
    result = MPNread(fn, en, processes = processes)
    endTimer = perf_counter()
    WRS.addRecord(useTimer, writeTimer, readTimer, endTimer)
    WRS.printThisStat()
def runMpbjj(WRS, data, processes = 4):
    """mpbj 資料分批再轉換寫入"""
    def MPJwrite(data, fileName, extension, processes = 3):
        mpPool = mp.Pool(processes=processes)
        sliceUint = len(data) // processes 
        sliceIdx = [None] + [sliceUint*(i+1) for i in range(processes-1)] + [None]       
        mpPool.starmap_async(Jwrite, [(data[s[0]:s[1]], fileName + "_{:}.{:}".format(i, extension)) for i,s in zip(range(processes), [(sliceIdx[i], sliceIdx[i+1])for i in range(processes)])])
        mpPool.close()
        mpPool.join()
    def MPJread(fileName, extension, processes = 3):
        """mpbj 先將資料分送再轉換型態寫入，單核讀取"""
        res = []
        for i in range(processes):
            with open(fileName + "_{:}.{:}".format(i, extension), 'rb') as f:
                res += json.load(f)
        return res
    def MPJread2(fileName, extension, processes = 3):
        """mpbj 先將資料分送再轉換型態寫入，多核讀取"""
        mpPool = mp.Pool(processes=processes)
        res = []
        [res.extend(each) for each in mpPool.map_async(Jread, [fileName + "_{:}.{:}".format(i, extension) for i in range(processes)]).get()]        
        return res
    fn, en = WRS.fileName.split(".")
    useTimer = perf_counter()      
    writeTimer = perf_counter() 
    MPJwrite(data, fn, en, processes = processes)
    readTimer = perf_counter()  
    result = MPJread(fn, en, processes = processes)
    endTimer = perf_counter()

    WRS.addRecord(useTimer, writeTimer, readTimer, endTimer)
    WRS.printThisStat()
def runMpbjjn(WRS, data, processes = 4):
    """mpbj 資料分批再轉換寫入"""
    def MPJwrite(data, fileName, extension, processes = 3):
        mpPool = mp.Pool(processes=processes)
        sliceUint = len(data) // processes 
        sliceIdx = [None] + [sliceUint*(i+1) for i in range(processes-1)] + [None]       
        mpPool.starmap_async(Jwrite, [(data[s[0]:s[1]], fileName + "_{:}.{:}".format(i, extension)) for i,s in zip(range(processes), [(sliceIdx[i], sliceIdx[i+1])for i in range(processes)])])
    def MPJread2(fileName, extension, processes = 3):
        """mpbj 先將資料分送再轉換型態寫入，單核讀取"""
        res = []
        for i in range(processes):
            with open(fileName + "_{:}.{:}".format(i, extension), 'rb') as f:
                res += json.load(f)
        return res
    def MPJread(fileName, extension, processes = 3):
        """mpbj 先將資料分送再轉換型態寫入，多核讀取"""
        mpPool = mp.Pool(processes=processes)
        res = []
        [res.extend(each) for each in mpPool.map_async(JNread, [fileName + "_{:}.{:}".format(i, extension) for i in range(processes)]).get()]        
        return res
    fn, en = WRS.fileName.split(".")
    useTimer = perf_counter()      
    writeTimer = perf_counter() 
    MPJwrite(data, fn, en, processes = processes)
    readTimer = perf_counter()  
    result = MPJread(fn, en, processes = processes)
    endTimer = perf_counter()

    WRS.addRecord(useTimer, writeTimer, readTimer, endTimer)
    WRS.printThisStat()
def runMpzl(WRS, data, processes = 4):
    def MPzlwrite(data, fileName, extension, processes = 3):
        """mpbj 先轉換成bytes再分別寫入"""
        mpPool = mp.Pool(processes=processes) # 定义CPU核数量为3    
        bstrData = zlib.compress(bytes(json.dumps(data), encoding="ascii"),6)
        sliceUint = len(bstrData) // processes 
        sliceIdx = [None] + [sliceUint*(i+1) for i in range(processes-1)] + [None]               
        mpPool.starmap_async(write, [(bstrData[s[0]:s[1]], fileName + "_{:}.{:}".format(i, extension)) for i,s in zip(range(processes), [(sliceIdx[i], sliceIdx[i+1])for i in range(processes)])])
        mpPool.close()
        mpPool.join()
    def MPzlread(fileName, extension, processes = 3):
        """mpbj 先將資料分送再轉換型態寫入，多核讀取"""
        mpPool = mp.Pool(processes=processes)
        res = b""
        for each in mpPool.map_async(read, [fileName + "_{:}.{:}".format(i, extension) for i in range(processes)]).get():
            res += each
        return json.loads(zlib.decompress(res))
    fn, en = WRS.fileName.split(".")
    useTimer = perf_counter()      
    writeTimer = perf_counter()   
    MPzlwrite(data, fn, en, processes = processes)
    readTimer = perf_counter()     
    result = MPzlread(fn, en, processes = processes)
    endTimer = perf_counter()
    WRS.addRecord(useTimer, writeTimer, readTimer, endTimer)
    WRS.printThisStat()
def runMpzlz(WRS, data, processes = 4):
    """mpbj 資料分批再轉換寫入"""
    def MPZZwrite(data, fileName, extension, processes = 3):
        """交給多進程 Z(壓縮) 寫入"""
        mpPool = mp.Pool(processes=processes) # 定义CPU核数量为3   
        bstrData = bytes(json.dumps(data), encoding="ascii")
        sliceUint = len(bstrData) // processes 
        sliceIdx = [None] + [sliceUint*(i+1) for i in range(processes-1)] + [None]  
           
        mpPool.starmap_async(Zwrite, [(bstrData[s[0]:s[1]], fileName + "_{:}.{:}".format(i, extension)) for i,s in zip(range(processes), [(sliceIdx[i], sliceIdx[i+1])for i in range(processes)])])          
        mpPool.close()
        mpPool.join()
    def MPZZread2(fileName, extension, processes = 3):
        """多核讀取"""
        pool = mp.Pool(processes=processes) # 定义CPU核数量为3
        res = b""
        for each in pool.map_async(Zread, [fileName + "_{:}.{:}".format(i, extension) for i in range(processes)]).get():
            res += each              
        return json.loads(res)
    def MPZZread(fileName, extension, processes = 3):
        """單核讀取"""
        res = b""
        for i in range(processes):
            with open(fileName + "_{:}.{:}".format(i, extension), 'rb') as f:
                res += zlib.decompress(f.read())
        return json.loads(res)
    fn, en = WRS.fileName.split(".")
    useTimer = perf_counter()      
    writeTimer = perf_counter()   
    MPZZwrite(data, fn, en, processes = processes)
    readTimer = perf_counter()     
    result = MPZZread(fn, en, processes = processes)
    endTimer = perf_counter()
    WRS.addRecord(useTimer, writeTimer, readTimer, endTimer)
    WRS.printThisStat()
def runMpzlzn(WRS, data, processes = 4):
    """mpbj 資料分批再轉換寫入"""
    def MPZZwrite(data, fileName, extension, mpPool, processes = 3):
        """交給多進程 Z(壓縮) 寫入"""
        bstrData = bytes(json.dumps(data), encoding="ascii")
        sliceUint = len(bstrData) // processes 
        sliceIdx = [None] + [sliceUint*(i+1) for i in range(processes-1)] + [None]
        tem = [(sliceIdx[i], sliceIdx[i+1])for i in range(processes)]
        fileNames = [fileName + "_{:}.{:}".format(i, extension) for i in range(processes)]
        for i in range(processes):
            mpPool.apply_async(Zwrite, args = (bstrData[tem[i][0]:tem[i][1]], fileNames[i]))


        #mpPool.starmap_async(Zwrite, [(bstrData[s[0]:s[1]], fileName + "_{:}.{:}".format(i, extension)) for i,s in zip(range(processes), [(sliceIdx[i], sliceIdx[i+1])for i in range(processes)])])  
            
    def MPZZread(fileName, extension, mpPool, processes = 3):
        """多核讀取"""
        res = b""
        for each in mpPool.map_async(ZNread, [fileName + "_{:}.{:}".format(i, extension) for i in range(processes)]).get():
            res += each              
        return json.loads(res)
    def MPZZread0(fileName, extension, mpPool, processes = 3):
        """單核讀取"""
        res = b""
        for i in range(processes):
            with open(fileName + "_{:}.{:}".format(i, extension), 'rb') as f:
                res += zlib.decompress(f.read())
        return json.loads(res)
    fn, en = WRS.fileName.split(".")
    useTimer = perf_counter()      
    writeTimer = perf_counter()  
    mpPool = mp.Pool(processes=processes) # 定义CPU核数量为3           
    MPZZwrite(data, fn, en, mpPool, processes = processes)
    readTimer = perf_counter()     
    result = MPZZread(fn, en, mpPool, processes = processes)
    endTimer = perf_counter()
    WRS.addRecord(useTimer, writeTimer, readTimer, endTimer)
    WRS.printThisStat()
def runMpzljz(WRS, data, processes = 4):
    def MPZJwrite(data, fileName, extension,  processes = 3):
        """交給多進程 J(格式化) Z(壓縮) 寫入"""
        mpPool = mp.Pool(processes=processes)
        dataSize = len(data)
        sliceUint = dataSize // processes    
        sliceIdx = [None] + [sliceUint*(i+1) for i in range(processes-1)] + [None]   
        mpPool.starmap_async(JZwrite, [(data[s[0]:s[1]], fileName + "_{:}.{:}".format(i, extension)) for i,s in zip(range(processes), [(sliceIdx[i], sliceIdx[i+1])for i in range(processes)])])
        mpPool.close()
        mpPool.join()
    def MPZJread(fileName, extension, processes = 3):
        """確認版"""
        res = []
        for i in range(processes):
            with open(fileName + "_{:}.{:}".format(i, extension), 'rb') as f:
                res += json.loads(zlib.decompress(f.read())) 
        return res
    def MPZJread2(fileName, extension, processes = 3):
        """mpzl 先將資料分送再轉換型態寫入，多核讀取"""
        mpPool = mp.Pool(processes=processes)
        res = []
        [res.extend(each) for each in mpPool.map_async(JZread, [fileName + "_{:}.{:}".format(i, extension) for i in range(processes)]).get()]        
        return res 
    fn, en = WRS.fileName.split(".")
    useTimer = perf_counter()      
    writeTimer = perf_counter()   
    MPZJwrite(data, fn, en, processes = processes)
    readTimer = perf_counter()     
    result = MPZJread(fn, en, processes = processes)
    endTimer = perf_counter()
    WRS.addRecord(useTimer, writeTimer, readTimer, endTimer)
    WRS.printThisStat()
def runMpzljzn(WRS, data, processes = 4):
    def MPZJwrite(data, fileName, extension,  processes = 3):
        """交給多進程 J(格式化) Z(壓縮) 寫入"""
        mpPool = mp.Pool(processes=processes)
        dataSize = len(data)
        sliceUint = dataSize // processes    
        sliceIdx = [None] + [sliceUint*(i+1) for i in range(processes-1)] + [None]   
        mpPool.starmap_async(JZwrite, [(data[s[0]:s[1]], fileName + "_{:}.{:}".format(i, extension)) for i,s in zip(range(processes), [(sliceIdx[i], sliceIdx[i+1])for i in range(processes)])])
    def MPZJread2(fileName, extension, processes = 3):
        """確認版"""
        res = []
        for i in range(processes):
            with open(fileName + "_{:}.{:}".format(i, extension), 'rb') as f:
                res += json.loads(zlib.decompress(f.read())) 
        return res
    def MPZJread(fileName, extension, processes = 3):
        """mpzl 先將資料分送再轉換型態寫入，多核讀取"""
        mpPool = mp.Pool(processes=processes)
        res = []
        [res.extend(each) for each in mpPool.map_async(JZNread, [fileName + "_{:}.{:}".format(i, extension) for i in range(processes)]).get()]        
        return res 
    fn, en = WRS.fileName.split(".")
    useTimer = perf_counter()      
    writeTimer = perf_counter()   
    MPZJwrite(data, fn, en, processes = processes)
    readTimer = perf_counter()     
    result = MPZJread(fn, en, processes = processes)
    endTimer = perf_counter()
    WRS.addRecord(useTimer, writeTimer, readTimer, endTimer)
    WRS.printThisStat()
def runMpxz(WRS, data, processes = 4):
    def MPxzwrite(data, fileName, extension,  processes = 3):
        """交給多進程 J(格式化) Z(壓縮) 寫入"""
        mpPool = mp.Pool(processes=processes)
        bstrData = lzma.compress(bytes(json.dumps(data), encoding="ascii"), preset = 6)
        dataSize = len(bstrData)
        sliceUint = dataSize // processes    
        sliceIdx = [None] + [sliceUint*(i+1) for i in range(processes-1)] + [None]   
        mpPool.starmap_async(write, [(bstrData[s[0]:s[1]], fileName + "_{:}.{:}".format(i, extension)) for i,s in zip(range(processes), [(sliceIdx[i], sliceIdx[i+1])for i in range(processes)])])
        mpPool.close()
        mpPool.join()
    def MPxzread(fileName, extension, processes = 3):
        res = b""
        for i in range(processes):
            with open(fileName + "_{:}.{:}".format(i, extension), 'rb') as f:
                res += f.read()
        return json.loads(lzma.decompress(res))
    """ json xz"""
    fn, en = WRS.fileName.split(".")
    useTimer = perf_counter()      
    writeTimer = perf_counter() 
    MPxzwrite(data, fn, en, processes = processes)
    readTimer = perf_counter()     
    result = MPxzread(fn, en, processes = processes)
    endTimer = perf_counter()
    WRS.addRecord(useTimer, writeTimer, readTimer, endTimer)
    WRS.printThisStat()
    pass
def runMpxzz(WRS, data, processes = 4):
    def MPXwrite(data, fileName, extension,  processes = 3):
        mpPool = mp.Pool(processes=processes)
        bstrData = bytes(json.dumps(data), encoding="ascii")
        dataSize = len(bstrData)
        sliceUint = dataSize // processes    
        sliceIdx = [None] + [sliceUint*(i+1) for i in range(processes-1)] + [None]   
        mpPool.starmap_async(Xwrite, [(bstrData[s[0]:s[1]], fileName + "_{:}.{:}".format(i, extension)) for i,s in zip(range(processes), [(sliceIdx[i], sliceIdx[i+1])for i in range(processes)])])
        mpPool.close()
        mpPool.join()
    def MPXread2(fileName, extension, processes = 3):
        res = b""
        for i in range(processes):
            with lzma.open(fileName + "_{:}.{:}".format(i, extension), 'rb') as f:
                res += f.read()
        return json.loads(res)
    def MPXread(fileName, extension, processes = 3):
        """mpzl 先將資料分送再轉換型態寫入，多核讀取"""
        mpPool = mp.Pool(processes=processes)
        res = []
        [res.extend(each) for each in mpPool.map_async(Xread, [fileName + "_{:}.{:}".format(i, extension) for i in range(processes)]).get()]        
        return res 

    """ json xz"""
    fn, en = WRS.fileName.split(".")
    useTimer = perf_counter()      
    writeTimer = perf_counter() 
    MPXwrite(data, fn, en, processes = processes)
    readTimer = perf_counter()     
    result = MPXread(fn, en, processes = processes)
    endTimer = perf_counter()
    WRS.addRecord(useTimer, writeTimer, readTimer, endTimer)
    WRS.printThisStat()
    pass
def runMpxzzj(WRS, data, processes = 4):
    def MPXJwrite(data, fileName, extension,  processes = 3):
        """交給多進程 J(格式化) Z(壓縮) 寫入"""
        mpPool = mp.Pool(processes=processes)
        dataSize = len(data)
        sliceUint = dataSize // processes    
        sliceIdx = [None] + [sliceUint*(i+1) for i in range(processes-1)] + [None]   
        mpPool.starmap_async(JXwrite, [(data[s[0]:s[1]], fileName + "_{:}.{:}".format(i, extension)) for i,s in zip(range(processes), [(sliceIdx[i], sliceIdx[i+1])for i in range(processes)])])
        mpPool.close()
        mpPool.join()
    def MPXJread(fileName, extension, processes = 3):
        res = []
        for i in range(processes):
            with lzma.open(fileName + "_{:}.{:}".format(i, extension), 'rb') as f:
                res += json.load(f) 
        return res
    def MPXJread2(fileName, extension, processes = 3):
        """mpzl 先將資料分送再轉換型態寫入，多核讀取"""
        mpPool = mp.Pool(processes=processes)
        res = []
        [res.extend(each) for each in mpPool.map_async(JXread, [fileName + "_{:}.{:}".format(i, extension) for i in range(processes)]).get()]        
        return res 
    """ json xz"""
    fn, en = WRS.fileName.split(".")
    useTimer = perf_counter()      
    writeTimer = perf_counter() 
    MPXJwrite(data, fn, en, processes = processes)
    readTimer = perf_counter()     
    result = MPXJread(fn, en, processes = processes)
    endTimer = perf_counter()
    WRS.addRecord(useTimer, writeTimer, readTimer, endTimer)
    WRS.printThisStat()
    pass
def runMpxzzjn(WRS, data, processes = 4):
    def MPXJwrite(data, fileName, extension,  processes = 3):
        """交給多進程 J(格式化) Z(壓縮) 寫入"""
        mpPool = mp.Pool(processes=processes)
        dataSize = len(data)
        sliceUint = dataSize // processes    
        sliceIdx = [None] + [sliceUint*(i+1) for i in range(processes-1)] + [None]   
        mpPool.starmap_async(JXwrite, [(data[s[0]:s[1]], fileName + "_{:}.{:}".format(i, extension)) for i,s in zip(range(processes), [(sliceIdx[i], sliceIdx[i+1])for i in range(processes)])])
    def MPXJread2(fileName, extension, processes = 3):
        res = []
        for i in range(processes):
            with lzma.open(fileName + "_{:}.{:}".format(i, extension), 'rb') as f:
                res += json.load(f) 
        return res
    def MPXJread(fileName, extension, processes = 3):
        """mpzl 先將資料分送再轉換型態寫入，多核讀取"""
        mpPool = mp.Pool(processes=processes)
        res = []
        [res.extend(each) for each in mpPool.map_async(JXNread, [fileName + "_{:}.{:}".format(i, extension) for i in range(processes)]).get()]        
        return res 
    """ json xz"""
    fn, en = WRS.fileName.split(".")
    useTimer = perf_counter()      
    writeTimer = perf_counter() 
    MPXJwrite(data, fn, en, processes = processes)
    readTimer = perf_counter()     
    result = MPXJread(fn, en, processes = processes)
    endTimer = perf_counter()
    #remove(fn, en, processes = processes)
    WRS.addRecord(useTimer, writeTimer, readTimer, endTimer)
    WRS.printThisStat()
    pass
