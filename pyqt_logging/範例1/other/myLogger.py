""" 
myLogger 
最後有一個mylogger，各個程式都引入此物件，操作會比較統一。
"""
import logging
from logging import config
import datetime
import os

class mylog():
    def __init__(self):
        self.folderPath = os.path.split(os.path.realpath(__file__))[0] + "\\"
        self.logName = self.folderPath + r"running.log"
        self.configPath = self.folderPath + r'logging.conf'
        self.DateFmt = "%Y-%m-%d %H:%M:%S"
        self.FileHandlerLevel = "ERROR" # 預設新生的 Logger 的 FileHandler level
        self.Fmt = logging.Formatter("%(asctime)s,%(name)s,%(levelname)s,%(message)s", self.DateFmt)        
        config.fileConfig(self.configPath)        
        self.AppFileHandler = logging.FileHandler(self.logName, mode='a')
        self.AppFileHandler.setFormatter(self.Fmt)
        self.AppFileHandler.setLevel("DEBUG")
        self.logData = ""
    def getLogger(self, name, fileName=None, Fmt=None, level = None, FHLevel = None):
        """取得帶有預設的Logger """
        logger = logging.getLogger(name)
        logger.addHandler(self.AppFileHandler)
        if fileName is not None: self.addFileHandler(logger, fileName, Fmt=Fmt, level = FHLevel)
        logger.addHandler(self.AppFileHandler)
        if level is not None: logger.setLevel(level)
        return logger
    def addFileHandler(self, logger, fileName, Fmt=None, level = None):
        FileHandler = logging.FileHandler(self.folderPath + fileName, mode='a')
        if Fmt is None: FileHandler.setFormatter(self.Fmt)            
        else: FileHandler.setFormatter(Fmt)        
        if level is None: FileHandler.setLevel(self.FileHandlerLevel)
        else: FileHandler.setLevel(level)
        logger.addHandler(FileHandler)
    def clearLog(self, filePath = ""):
        if filePath == "": filePath = self.logName
        with open(filePath, "w") as f:
            pass
        f.close()
    def getLogData(self):
        with open(self.logName, "r") as f:      
            self.logData = f.read().split("\n")
        del self.logData[-1]
        f.close()
    def queryLastestLog(self, time, seconds = 10):
        """取得最新的logData 
        seconds : 秒數
        """
        self.getLogData()
        for i in reversed(range(len(self.logData))):
            if len(self.logData[i]) > 0:
                self.logData[i] = self.logData[i].split(",")
                self.logDataTime = datetime.datetime.strptime(self.logData[i][0], self.DateFmt)
                if (time - self.logDataTime).seconds <= 10:
                    self.logData[i] = {'time': self.logDataTime, "name": self.logData[i][1], "levelname": self.logData[i][2], "message": self.logData[i][3]}
                else:
                    del self.logData[i]
        return self.logData

mylogger = mylog()