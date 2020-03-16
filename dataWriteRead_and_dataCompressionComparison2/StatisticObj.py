import os, sys

class WRStatistic():
    """用來紀錄並統計數據"""
    
    def __init__(self, name, fileName, data, compresslevel = None):
        self.name = name
        self.Wtime, self.Rtime, self.Utime = [], [], []
        self.fileName = fileName
        self.dataSize = sys.getsizeof(data)  
        self.fileSize = 0
        if compresslevel: self.compresslevel = compresslevel 
        self.runtimes = 0

    def addRecord(self, useTimer, writeTimer, readTimer, endTimer):
        self.Wtime.append(readTimer - writeTimer - (writeTimer - useTimer))
        self.Rtime.append(endTimer - readTimer - (writeTimer - useTimer))
        self.Utime.append(self.Wtime[-1] + self.Rtime[-1])   
        self.runtimes += 1

    def printThisStat(self):
        print("method: {:}, Wtime:{:.5f}, Rtime:{:.5f}, Utime:{:.5f}".format(self.name, self.Wtime[-1], self.Rtime[-1], self.Utime[-1]))
        self.delFile()

    def delFile(self):
        """刪除檔案， 如果沒有紀錄檔案大小，那就紀錄"""
        if self.fileSize == 0:
            if os.path.isfile(self.fileName): self.fileSize = os.path.getsize(self.fileName)
            else: self.fileSize = sum([os.path.getsize(name) for name in os.listdir() if name.split('_')[0] == self.fileName.split(".")[0]])
        if os.path.isfile(self.fileName):
            os.remove(self.fileName)
        else:
            [os.remove(name) for name in os.listdir() if name.split('_')[0] == self.fileName.split(".")[0]]

    def printTotalStat(self):    
        print("Method: {:}, Compress Ratio: {:.2f}：1".format(self.name, self.dataSize/self.fileSize))
        print("Average Use Time: avgWtime:{:.5f}, avgRtime:{:.5f}, avgUtime:{:.5f}".format(self.avgWT, self.avgRT, self.avgUT))
        print("Data size: {:}({:.2f}MB), Wspeed:{:.5f} MB/s, Rspeed:{:.5f} MB/s, Uspeed:{:.5f} MB/s".format(self.dataSize, self.dataSize / 1024000, self.dWspeed, self.dRspeed, self.dUspeed))
        print("File size: {:}({:.2f}MB), Wspeed:{:.5f} MB/s, Rspeed:{:.5f} MB/s, Uspeed:{:.5f} MB/s".format(self.fileSize, self.fileSize / 1024000, self.Wspeed, self.Rspeed, self.Uspeed))

    @property
    def avgWT(self): return sum(self.Wtime) / self.runtimes
    @property
    def avgRT(self): return sum(self.Rtime) / self.runtimes
    @property
    def avgUT(self): return sum(self.Utime) / self.runtimes
    @property
    def dWspeed(self): return self.dataSize / self.avgWT / 1024000
    @property
    def dRspeed(self): return self.dataSize / self.avgRT / 1024000
    @property
    def dUspeed(self): return self.dataSize / self.avgUT / 1024000
    @property
    def Wspeed(self): return self.fileSize / self.avgWT / 1024000
    @property
    def Rspeed(self): return self.fileSize / self.avgRT / 1024000
    @property
    def Uspeed(self): return self.fileSize / self.avgUT / 1024000


