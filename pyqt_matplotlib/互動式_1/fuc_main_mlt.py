"""功能區編寫"""
from PyQt5 import QtCore, QtGui, QtWidgets
import ui_mlt # 載入轉譯後 .py 檔

# 功能區
class MYMAINWINDOW(QtWidgets.QMainWindow, ui_mlt.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MYMAINWINDOW, self).__init__(parent)
        self.setupUi(self)
        self.btn_f1plus.clicked.connect(self.btn_f1plus_clicked)
        self.btn_f1sub.clicked.connect(self.btn_f1sub_clicked)
        self.btn_timerStart.clicked.connect(self.btn_timerStart_clicked)
        self.btn_timerStop.clicked.connect(self.btn_timerStop_clicked)
        self.btn_show.clicked.connect(self.btn_show_clicked)
        self.hsb_f1.valueChanged.connect(self.hsb_f1_valueChanged)
        self.followF1.stateChanged.connect(self.followF1_stateChanged)
        self.xWidth = [1, 2, 3, 5, 7, 10, 12, 15, 30]
        self.xWidthIndex = 2    
    def hsb_f1_valueChanged(self, value):
        # scrollbar單位是整數，設定1單位對應x軸0.1。
        self.f1.FC.setWidth(self.xWidth[self.xWidthIndex], value/10)
        pass
    def btn_f1plus_clicked(self):
        if self.xWidthIndex  < len(self.xWidth)-1:
            self.xWidthIndex += 1
            self.lal_f1Width.setText("Width: {:}".format(self.xWidth[self.xWidthIndex]))
        self.f1.FC.setWidth(self.xWidth[self.xWidthIndex])
        pass
    def btn_f1sub_clicked(self):
        if self.xWidthIndex  > 0:
            self.xWidthIndex -= 1
            self.lal_f1Width.setText("Width: {:}".format(self.xWidth[self.xWidthIndex]))
        self.f1.FC.setWidth(self.xWidth[self.xWidthIndex])
    def btn_timerStart_clicked(self):
        if not self.f1.FC.timer.isActive():
            self.f1.FC.timer.start(33)
        pass
    def btn_timerStop_clicked(self):
        if self.f1.FC.timer.isActive():
            self.f1.FC.timer.stop()
        pass
    def followF1_stateChanged(self):
        if self.followF1.checkState() == 2: # 2 為 checkbox 勾選時的狀態
            self.f1.FC.axes_xFollow = True
            self.hsb_f1.setEnabled(0)
        else: 
            self.f1.FC.axes_xFollow = False
            xloc = int(self.f1.FC.axes[0].get_xlim()[0]*10)
            if xloc > self.hsb_f1.maximum(): self.hsb_f1.setMaximum(xloc)
            self.hsb_f1.setValue(xloc)
            self.hsb_f1.setEnabled(1)
        pass
    def btn_show_clicked(self):
        if self.f1.FC.axlineShow: 
            self.f1.FC.axlineShow = False
            # 如果軸1有輔助線，則移除
            if len(self.f1.FC.axes[1].get_lines()) == 1:
                self.f1.FC.hline_mouse.remove()
                self.f1.FC.draw()
        else: self.f1.FC.axlineShow = True        
        # showHLine
        print("顯示輔助線:", self.f1.FC.axlineShow)
        pass


