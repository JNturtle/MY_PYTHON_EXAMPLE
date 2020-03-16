import json, gzip, lzma, bz2, zlib
from time import perf_counter
from StatisticObj import WRStatistic

data = [("阿明", "身體狀況", {"體重":78.9, "肝功能": "正常"}, 90, 85, 97, 81,  85, True)]*50000
runtimes = 10

# 運行主程式
if __name__ == '__main__':
    bjTest = WRStatistic("bstr json", "ex_sj_RWSpeed.txt", data) 
    zlTest = WRStatistic("json zlib", "ex_zl_RWSpeed", data, compresslevel = 6)
    sjTest = WRStatistic("str json", "ex_sj_RWSpeed.txt", data)
    gzTest = WRStatistic("json gz", "ex_gz_RWSpeed.gz", data, compresslevel = 9)
    xzTest = WRStatistic("json xz", "ex_xz_RWSpeed.xz", data, compresslevel = 6)
    jjTest = WRStatistic("json json", "ex_jj_RWSpeed.txt", data)
    sbTest = WRStatistic("bstr list", "ex_sb_RWSpeed.txt", data)
    slTest = WRStatistic("str str (list)", "ex_sl_RWSpeed.txt", data)
    stTest = WRStatistic("str str (tuple)", "ex_st_RWSpeed.txt", data)
    bzTest = WRStatistic("json bz", "ex_bz_RWSpeed", data, compresslevel = 9)
    # 在這裡擺入想執行的測試
    run_test = [bjTest, zlTest, sjTest, gzTest, xzTest, jjTest, sbTest, slTest, stTest, bzTest] 

    def runBj(WRS):
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
    def runZlib(WRS, compressLevel = 6):
        """ json zlib"""
        if WRS.compresslevel: compressLevel = WRS.compresslevel
        useTimer = perf_counter()      
        writeTimer = perf_counter() 
        with open(WRS.fileName, 'wb') as f: 
            f.write(zlib.compress(bytes(json.dumps(data), encoding="ascii"), level=compressLevel))
        f.close()
        readTimer = perf_counter()     
        with open(WRS.fileName, "rb") as f:
            res = json.loads(zlib.decompress(f.read()))
        f.close()
        endTimer = perf_counter()
        WRS.addRecord(useTimer, writeTimer, readTimer, endTimer)
        WRS.printThisStat()
    def runSj(WRS):
        """ string json """
        useTimer = perf_counter()      
        writeTimer = perf_counter()  
        with open(WRS.fileName, 'w') as f:
            f.write(json.dumps(data))
        f.close()
        readTimer = perf_counter()     
        with open(WRS.fileName, 'r') as f:
            result = json.load(f)
        f.close()
        endTimer = perf_counter()
        WRS.addRecord(useTimer, writeTimer, readTimer, endTimer)
        WRS.printThisStat()
    def runGz(WRS, compressLevel = 9):
        """ json gz"""
        if WRS.compresslevel: compressLevel = WRS.compresslevel
        useTimer = perf_counter()      
        writeTimer = perf_counter() 
        with open(WRS.fileName, 'wb') as f: 
            f.write(gzip.compress(bytes(json.dumps(data), encoding="ascii"), compresslevel = compressLevel))
        f.close()
        readTimer = perf_counter()     
        with gzip.open(WRS.fileName, "rb" ) as f:
            res = json.load(f)
        f.close()
        endTimer = perf_counter()
        WRS.addRecord(useTimer, writeTimer, readTimer, endTimer)
        WRS.printThisStat()
    def runXz(WRS, compressLevel = 6):
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
    def runJj(WRS):
        """ json json"""
        useTimer = perf_counter()      
        writeTimer = perf_counter()  
        with open(WRS.fileName, 'w') as f:
            json.dump(data, f)
        f.close()
        readTimer = perf_counter()     
        with open(WRS.fileName, 'r') as f:
            result = json.load(f)
        f.close()
        endTimer = perf_counter()
        WRS.addRecord(useTimer, writeTimer, readTimer, endTimer)
        WRS.printThisStat()
    def runSb(WRS):
        """ string list"""
        useTimer = perf_counter()
        writeTimer = perf_counter()  
        with open(WRS.fileName, 'wb') as f:
            f.write(bytes(str(data), encoding = "utf8"))
        f.close()
        readTimer = perf_counter()         
        with open(WRS.fileName, 'rb') as f:
            result = list(eval(f.read()))
        f.close()
        endTimer = perf_counter()
        WRS.addRecord(useTimer, writeTimer, readTimer, endTimer)
        WRS.printThisStat()
    def runSl(WRS):
        """ string list"""
        useTimer = perf_counter()
        writeTimer = perf_counter()  
        with open(WRS.fileName, 'w') as f:
            f.write(str(data))
        f.close()
        readTimer = perf_counter()         
        with open(WRS.fileName, 'r') as f:
            result = list(eval(f.read()))
        f.close()
        endTimer = perf_counter()
        WRS.addRecord(useTimer, writeTimer, readTimer, endTimer)
        WRS.printThisStat()
    def runSt(WRS):
        """ string tuple"""
        useTimer = perf_counter()      
        writeTimer = perf_counter()  
        with open(WRS.fileName, 'w') as f:
            f.write(str(data))
        f.close()
        readTimer = perf_counter()     
        with open(WRS.fileName, 'r') as f:
            result = tuple(eval(f.read()))
        f.close()
        endTimer = perf_counter()
        WRS.addRecord(useTimer, writeTimer, readTimer, endTimer)
        WRS.printThisStat()
    def runBz(WRS, compressLevel = 9):
        """ json bz"""
        if WRS.compresslevel: compressLevel = WRS.compresslevel
        useTimer = perf_counter()      
        writeTimer = perf_counter() 
        with bz2.open(WRS.fileName, 'wb', compresslevel = compressLevel) as f: 
            f.write(bytes(json.dumps(data), encoding="ascii"))
        f.close()
        readTimer = perf_counter()     
        with bz2.open(WRS.fileName, 'rb') as f: 
            res = json.load(f)
        f.close()
        endTimer = perf_counter()
        WRS.addRecord(useTimer, writeTimer, readTimer, endTimer)
        WRS.printThisStat()
    for _ in range(runtimes):
        for test in run_test:
            if test is bjTest: runBj(bjTest)            
            elif test is zlTest: runZlib(zlTest)
            elif test is sjTest: runSj(sjTest)
            elif test is gzTest: runGz(gzTest)
            elif test is xzTest: runXz(xzTest)
            elif test is jjTest: runJj(jjTest)
            elif test is sbTest: runSb(sbTest)
            elif test is slTest: runSl(slTest)
            elif test is stTest: runSt(stTest)
            elif test is bzTest: runBz(bzTest)
    print("[Statistics]")
    if bjTest.runtimes: bjTest.printTotalStat()    
    if zlTest.runtimes: zlTest.printTotalStat()
    if sjTest.runtimes: sjTest.printTotalStat()
    if gzTest.runtimes: gzTest.printTotalStat()
    if xzTest.runtimes: xzTest.printTotalStat()
    if jjTest.runtimes: jjTest.printTotalStat()
    if sbTest.runtimes: sbTest.printTotalStat()
    if slTest.runtimes: slTest.printTotalStat()
    if stTest.runtimes: stTest.printTotalStat()
    if bzTest.runtimes: bzTest.printTotalStat()






