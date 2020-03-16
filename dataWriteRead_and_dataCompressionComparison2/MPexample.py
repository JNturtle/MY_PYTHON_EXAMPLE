

# 運行主程式
if __name__ == '__main__':

    from StatisticObj import WRStatistic
    from time import sleep
    
    data = [(i,"阿明", "身體狀況", {"體重":78.9, "肝功能": "正常"}, 90, 85, 97, 81,  85, True) for i in range(10000)]

    bjTest = WRStatistic("bstr json", "ex_bj_RWSpeed.txt", data)
    zlTest = WRStatistic("json zlib", "ex_zl_RWSpeed", data, compresslevel = 1)
    xzTest = WRStatistic("json xz", "ex_xz_RWSpeed.xz", data, compresslevel = 6)
    mpbjTest = WRStatistic("mpbj", "mpbj.txt", data)
    mpbjnTest = WRStatistic("mpbjn", "mpbjn.txt", data)
    mpbjjTest = WRStatistic("mpbjj", "mpbjj.txt", data)
    mpbjjnTest = WRStatistic("mpbjjn", "mpbjjn.txt", data)
    mpzlTest = WRStatistic("mpzl", "mpzl.zlib", data)
    mpzlzTest = WRStatistic("mpzlz", "mpzlz.zlib", data)
    mpzlznTest = WRStatistic("mpzlzn", "mpzlzn.zlib", data)
    mpzljzTest = WRStatistic("mpzljz", "mpzljz.zlib", data)
    mpzljznTest = WRStatistic("mpzljzn", "mpzljzn.zlib", data)
    mpxzTest = WRStatistic("mpxz", "mpxz.xz", data)
    mpxzzTest = WRStatistic("mpxzz", "mpxzz.xz", data)
    mpxzzjTest = WRStatistic("mpxzzj", "mpxzzj.xz", data)
    mpxzzjnTest = WRStatistic("mpxzzjn", "mpxzzjn.xz", data)
    # 要執行的測試
    run_test = [bjTest, zlTest, xzTest, mpbjTest, mpbjnTest, mpbjjTest, mpbjjnTest, mpzlTest, mpzlzTest, mpzlznTest, mpzljzTest, mpzljznTest, mpxzTest, mpxzzTest, mpxzzjTest, mpxzzjnTest]#    bjTest, zlTest, xzTest, mpbjTest, mpbjnTest, mpbjjTest, mpbjjnTest, mpzlTest, mpzlzTest, mpzlznTest, mpzljzTest, mpzljznTest, mpxzTest, mpxzzTest, mpxzzjTest, mpxzzjnTest
    runtimes = 1
    from runFuc import *
    for _ in range(runtimes):
        for test in run_test:
            if test is bjTest: runbj(bjTest, data)
            elif test is zlTest: runZlib(zlTest, data)
            elif test is xzTest: runXz(xzTest, data)
            elif test is mpbjTest: runMpbj(mpbjTest, data)
            elif test is mpbjnTest: runMpbjn(mpbjnTest, data)
            elif test is mpbjjTest: runMpbjj(mpbjjTest, data)
            elif test is mpbjjnTest: runMpbjjn(mpbjjnTest, data)
            elif test is mpzlTest: runMpzl(mpzlTest, data)
            elif test is mpzlzTest: runMpzlz(mpzlzTest, data)
            elif test is mpzlznTest: runMpzlzn(mpzlznTest, data)
            elif test is mpzljzTest: runMpzljz(mpzljzTest, data)
            elif test is mpzljznTest: runMpzljzn(mpzljznTest, data)
            elif test is mpxzTest: runMpxz(mpxzTest, data)
            elif test is mpxzzTest: runMpxzz(mpxzzTest, data)
            elif test is mpxzzjTest: runMpxzzj(mpxzzjTest, data)
            elif test is mpxzzjnTest: runMpxzzjn(mpxzzjnTest, data)
            sleep(0.5)
    print("[Statistics]")
    for test in run_test:
        if test is bjTest: bjTest.printTotalStat()
        elif test is zlTest: zlTest.printTotalStat()
        elif test is xzTest: xzTest.printTotalStat()
        elif test is mpbjTest: mpbjTest.printTotalStat() 
        elif test is mpbjnTest: mpbjnTest.printTotalStat() 
        elif test is mpbjjTest: mpbjjTest.printTotalStat() 
        elif test is mpbjjnTest: mpbjjnTest.printTotalStat() 
        elif test is mpzlTest: mpzlTest.printTotalStat()
        elif test is mpzlzTest: mpzlzTest.printTotalStat()
        elif test is mpzlznTest: mpzlznTest.printTotalStat()
        elif test is mpzljzTest: mpzljzTest.printTotalStat()
        elif test is mpzljznTest: mpzljznTest.printTotalStat()
        elif test is mpxzTest: mpxzTest.printTotalStat()  
        elif test is mpxzzTest: mpxzzTest.printTotalStat()  
        elif test is mpxzzjTest: mpxzzjTest.printTotalStat()  
        elif test is mpxzzjnTest: mpxzzjnTest.printTotalStat()  
    #
    #    

