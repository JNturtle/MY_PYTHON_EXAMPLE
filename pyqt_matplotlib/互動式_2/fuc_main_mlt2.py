"""功能區編寫
每條線以清單上的位置作為gid，確保其獨一無二
線的label則訂為該線的方程

線的顯示與否，不顯示的線用一個List名為 hiddenLines 存放
從隱藏換成顯示，就從 hiddenLines 中取出該線再添加到軸上
線只會在 軸 上或是 hiddenLines 中，刪除線就從這兩個地方找出來刪
"""

from PyQt5 import QtCore, QtGui, QtWidgets
import ui_mlt2 # 載入轉譯後 .py 檔

# 功能區
class MYMAINWINDOW(QtWidgets.QMainWindow, ui_mlt2.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MYMAINWINDOW, self).__init__(parent)
        self.setupUi(self)
        self.btn_add.clicked.connect(self.btn_add_clicked)
        self.btn_del.clicked.connect(self.btn_del_clicked)
        self.hsb_f1.valueChanged.connect(self.hsb_f1_valueChanged)
        self.lines.itemChanged.connect(self.lines_itemChanged)
        self.legned.stateChanged.connect(self.legned_stateChanged)
        #self.f1.FC.showStatusBar = self.statusBar().showMessage # 兩種寫法都可以
        self.f1.FC.showStatusBar = self.statusbar.showMessage 
        self.f1.FC.showLegend = self.legned.checkState
        # 添加預設的3條線        
        self.inti_line()
    def inti_line(self):
        """產生預設的線，仿按下add按鈕"""
        aVs = [2.0,0.0,0.0]
        bVs = [1.0,1.0,0.0]
        cVs = [-2.0,-2.0,-2.0]
        No = [0,1,2]
        for aV, bV, cV, itemRow in zip(aVs, bVs, cVs, No):
            item_name = "{:}x**2 + {:}x**1 + {:}".format(aV, bV, cV)
            item = QtWidgets.QListWidgetItem()
            item.setText(item_name)
            item.setCheckState(2)
            self.lines.addItem(item)
            self.f1.FC.addLine(aV, bV, cV, itemRow)
        pass
    def lines_itemChanged(self, item):
        if item.checkState() == 2:
            self.f1.FC.showLine(self.lines.row(item))
        else:
            self.f1.FC.hiddenLine(self.lines.row(item))
        pass
    def hsb_f1_valueChanged(self, value):
        # value 25 對齊 xlim[0] -2， value 1 unit → xlim 0.1
        self.f1.FC.setWidth(4, (value-45)/10)
        pass
    def btn_add_clicked(self):        
        aV = self.aV.value()
        bV = self.bV.value()
        cV = self.cV.value()
        item_name = "{:}x**2 + {:}x**1 + {:}".format(aV, bV, cV)
        item = QtWidgets.QListWidgetItem()
        item.setText(item_name)
        item.setCheckState(2)
        self.lines.addItem(item)
        self.f1.FC.addLine(aV, bV, cV, self.lines.row(item)) 
        pass
    def btn_del_clicked(self):
        item = self.lines.currentItem()
        if item is not None:           
            self.f1.FC.removeLine(self.lines.row(item))
            self.lines.takeItem(self.lines.row(item))
            del item
        pass
    def legned_stateChanged(self):
        self.f1.FC.legendChange()
        self.f1.FC.draw()
        pass


