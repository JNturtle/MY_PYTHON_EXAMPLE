"""功能區編寫
能預期線程執行的程式會四散在各地，所以引用特定的myLogger，避免使用多個同名檔案造成混淆。
有 ProgramA ProgramB ProgramC ProgramD 四個按鈕，分別對應 ./other 的 .py檔
ProgramA 是有針對對應錯誤的做應對的，而且有錯誤發生
ProgramB 是有針對對應錯誤的做應對的，但是沒有錯誤
ProgramC 沒有做任何錯誤處理
ProgramD 無限循環

如果獨立程式也不想顯示cmd，請把指令換成下行，並將對應檔案的檔名改成 .pyw 。但是這樣就不會有任何非預期錯誤輸出。
cmd = 'start ""pythonw ' + folderPath + '\\other\\Program[X].pyw >{:} 2>&1"'.format(temErrorLog)
cmd = 'start ""pythonw ' + folderPath + '\\other\\Program[X].pyw '
"""

from PyQt5 import QtCore, QtGui, QtWidgets
import datetime

import os
folderPath = os.path.split(os.path.realpath(__file__))[0]   
os.makedirs(folderPath+"\\other\\error\\", exist_ok = True)

import sys
LOGGERPATH = os.path.split(os.path.realpath(__file__))[0]
sys.path.append(LOGGERPATH + r"\other") # 在系統添加指定路徑，引入 myLogger。

from myLogger import mylogger # 這邊引入的是 ./other/myLogger.py
import ui_work # 載入轉譯後 .py 檔

# 功能區
class MYMAINWINDOW(QtWidgets.QMainWindow, ui_work.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MYMAINWINDOW, self).__init__(parent)
        self.setupUi(self)
        # 系統時間
        self.sysTime = datetime.datetime.now()
        self.sysTimeLastSec = self.sysTime
        self.sysTimeLastMin = self.sysTime
        self.setLocalTimeLabel()
        self.sysTimer = QtCore.QTimer()
        self.sysTimer.timeout.connect(self.sysTimer_timeout)
        self.sysTimer.start(333) 
        # 線程
        self.threads = []
        self.PA.clicked.connect(self.PA_clicked)
        self.PB.clicked.connect(self.PB_clicked)
        self.PC.clicked.connect(self.PC_clicked)
        self.PD.clicked.connect(self.PD_clicked)
        # logging
        mylogger.clearLog()
        self.logger = mylogger.getLogger("Main")
        self.loggingFilter = "INFO"
        self.notWarnRecord = []
        self.CRITICAL.toggled.connect(lambda: self.loggingRadioBtnState(self.CRITICAL))
        self.ERROR.toggled.connect(lambda: self.loggingRadioBtnState(self.ERROR))
        self.WARNING.toggled.connect(lambda: self.loggingRadioBtnState(self.WARNING))
        self.INFO.toggled.connect(lambda: self.loggingRadioBtnState(self.INFO))
        self.DEBUG.toggled.connect(lambda: self.loggingRadioBtnState(self.DEBUG))
    def loggingRadioBtnState(self, btn):
        if btn.isChecked() == True:
            self.loggingFilter = btn.text()
            self.logger.info("清單只顯示 {:} 以上的紀錄".format(btn.text()))
            self.showLogMsg()
        pass
    def PA_clicked(self):       
        temErrorLog = folderPath + "\\other\\error\\ProgramA_{:}.log".format(self.sysTime.strftime("%Y%m%d%H%M%S"))
        cmd = 'python ' + folderPath + '\\other\\ProgramA.py >{:} 2>&1'.format(temErrorLog)
        self.logger.info("按下 programA 按鈕")
        self.addThread(os.system, [cmd], "ProgramA", temErrorLog)
    def PB_clicked(self):
        temErrorLog = folderPath + "\\other\\error\\ProgramB_{:}.log".format(self.sysTime.strftime("%Y%m%d%H%M%S"))
        cmd = 'python ' + folderPath + '\\other\\ProgramB.py >{:} 2>&1'.format(temErrorLog)
        self.logger.info("按下 programB 按鈕")
        self.addThread(os.system, [cmd], "ProgramB", temErrorLog)
    def PC_clicked(self):     
        temErrorLog = folderPath + "\\other\\error\\ProgramC_{:}.log".format(self.sysTime.strftime("%Y%m%d%H%M%S"))
        cmd = 'python ' + folderPath + '\\other\\ProgramC.py >{:} 2>&1'.format(temErrorLog)
        self.logger.info("按下 programC 按鈕")
        self.addThread(os.system, [cmd], "ProgramC", temErrorLog)
    def PD_clicked(self):     
        temErrorLog = folderPath + "\\other\\error\\ProgramD_{:}.log".format(self.sysTime.strftime("%Y%m%d%H%M%S"))
        cmd = 'python ' + folderPath + '\\other\\ProgramD.py >{:} 2>&1'.format(temErrorLog)
        self.logger.info("按下 programD 按鈕")
        self.addThread(os.system, [cmd], "ProgramD", temErrorLog)
    def addThread(self, func, params, programName, temLogPath):
        self.threads.append(WorkThread())
        self.threads[-1].setFuncParams(func, params, programName, temLogPath)
        self.threads[-1].start()

    def sysTimer_timeout(self):
        self.sysTime = datetime.datetime.now()
        if (self.sysTime - self.sysTimeLastSec).seconds >= 1:
            self.sysTimeLastSec = self.sysTime
            self.setLocalTimeLabel()
            self.showLogMsg()
            self.checkThread()
        pass
    def setLocalTimeLabel(self):
        msg = "現在時間: {:}".format(self.sysTime.strftime("%m-%d %H:%M:%S"))
        self.localTime.setText(msg)
    def showLogMsg(self):
        logs = mylogger.queryLastestLog(self.sysTime, seconds = 10)
        self.loglist.clear()
        if self.ERRORWARN.checkState() == 2:
            for log in self.notWarnRecord: 
                if log not in logs: del log
        FL = []
        for level in ["CRITICAL", "ERROR", "WARNING", "INFO", "DEBUG"]:
            if self.loggingFilter not in FL: FL.append(level)
            else: break                      
        for log in logs:
            if log['levelname'] in FL:
                self.loglist.addItem("{:}, {:}, {:}, {:}".format(str(log['time']), log['levelname'], log['name'], log['message']))
                if self.ERRORWARN.checkState() == 2 and (log['levelname'] == "CRITICAL" or log['levelname'] == "ERROR" ) and log not in self.notWarnRecord:
                    self.notWarnRecord.append(log)
                    QtWidgets.QMessageBox.warning(self, log['name'], log['levelname'] + "！\n" + log['message'], QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.Yes)
        pass
    def checkThread(self):
        for thread in self.threads:
            if thread.isFinished() == True:
                if os.path.getsize(thread.temLogPath) == 0:
                    os.remove(thread.temLogPath)
                else:
                    with open(thread.temLogPath, "r") as f:
                        msg = f.read()
                        f.close()
                    if self.ERRORWARN.checkState() == 2: QtWidgets.QMessageBox.warning(None, thread.programName, msg, QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.Yes)
                self.threads.remove(thread)
                del thread
        pass
       
class WorkThread(QtCore.QThread):    
    def __int__(self, func = None, params = None):
        super(WorkThread, self).__init__()
        self.func = func
        self.params = params
        self.temLogPath = ""

    def setFuncParams(self, func = None, params = None, programName="ERROR", temLogPath = ""):
        self.func = func
        self.params = params
        self.programName = programName
        self.temLogPath = temLogPath

    def run(self):
        self.func(*self.params)

