from PyQt5 import QtWidgets, QtCore
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
"""
plt plt.rcParams['font.sans-serif'] 相關文章
https://jnturtle.blogspot.com/2020/02/python-matplotlib.html
"""
plt.rcParams['font.sans-serif'] = ["DFKai-SB"] # 標楷體
plt.rcParams['axes.unicode_minus'] = False  # 正常顯示負號
"""
Unary quadratic equation
"""
class MW_UQE(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(MW_UQE, self).__init__(parent)
        self.initUi()
    def initUi(self):
        self.layout = QtWidgets.QVBoxLayout(self)
        self.FC = MW_UQE_Canvas(self, width=1, height=0.5, dpi=100)
        self.layout.addWidget(self.FC)
 
class MW_UQE_Canvas(FigureCanvas):
    def __init__(self, parent=None, width=3.5, height=2, dpi=100):
        #
        self.fig = plt.Figure(figsize=(width,height), dpi=dpi)
        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)
        # 
        self.showStatusBar = None
        self.showLegend = None
        self.legend = None
        self.fig.canvas.mpl_connect('motion_notify_event', self.on_plot_hover)  
        self.fig.suptitle('一元二次方程')       
        # 添加軸
        self.axes = [self.fig.add_subplot(111, autoscale_on=True)] 
        self.axes[0].set_xlabel("x")
        self.axes[0].set_ylabel("y")
        self.axes[0].set_xlim(-2,2)
        #
        self.hiddenLines = []
    def addLine(self, a, b, c, itemNo):
        lineName = "{:}x**2 + {:}x**1 + {:}".format(a, b, c)
        x = np.arange(-4.5,4.5,0.01)
        y = a*x**2 + b*x**1 + c
        self.axes[0].plot(x, y, lineWidth=1, gid = itemNo, label = lineName)    
        self.legendChange()
        self.axes[0].relim()        
        self.axes[0].autoscale(axis = "y")
        self.draw()
        pass
    def legendChange(self):
         # 刪除舊圖利
        if self.legend is not None: 
            self.legend.remove()
            del self.legend
            self.legend = None
        # 產生圖例
        if self.showLegend() == 2 and len(self.axes[0].get_lines()) > 0:
            self.legend = self.fig.legend(loc = 3) # loc: 3 圖片下左 
        pass
    def showLine(self, itemNo):     
        for line in self.hiddenLines:
            if line.get_gid() == itemNo:
                self.axes[0].add_line(line)
                self.hiddenLines.remove(line)
                self.legendChange()
                self.draw()
                break
        pass
    def hiddenLine(self, itemNo):
        for line in self.axes[0].get_lines():
            if line.get_gid() == itemNo:
                line.remove()
                self.hiddenLines.append(line)
                self.legendChange()
                self.draw()
                break
        pass
    def removeLine(self, itemNo):
        tem_gid = -1
        for line in self.axes[0].get_lines():
            if line.get_gid() == itemNo:
                tem_gid = itemNo
                line.remove()                
                del line
                break
        for line in self.hiddenLines:
            if line.get_gid() == itemNo:
                tem_gid = itemNo
                self.hiddenLines.remove(line)             
                del line
                break
        # 線以清單的位置為gid，如果刪除清單的item，位置也會變動，所以也要改變線的gid
        if tem_gid != -1:
            for lines in [self.axes[0].get_lines(), self.hiddenLines]:
                for line in lines:
                    if line.get_gid() > tem_gid:
                        line.set_gid(line.get_gid()-1)
            self.legendChange()
            self.axes[0].relim()
            self.axes[0].autoscale(axis = "y")
            self.draw()
        pass
    def setWidth(self, width, xDatum = None):
        if xDatum is None: self.axes_xDatum = self.axes[0].get_xlim()[0]                  
        else: self.axes_xDatum = xDatum
        self.axes[0].set_xlim(self.axes_xDatum, self.axes_xDatum+width)
        self.draw()
        pass
    def on_plot_hover(self, event):
        if event.ydata is not None:
            # 依序遞迴軸與其軸上的線，尋找有包含事件座標的線。
            for line in self.axes[0].get_lines():
                if line.contains(event)[0]:
                    msg = "label:「{:<20}」, x:{:>6.2f}, y:{:>6.2f}".format(line.get_label(),  event.xdata, event.ydata)
                    if self.showStatusBar is not None: self.showStatusBar(msg)
        pass

