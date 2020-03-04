from PyQt5 import QtWidgets, QtCore
import numpy as np
from matplotlib import pyplot as plt

# 使用 matplotlib中的FigureCanvas (在使用 Qt5 Backends中 FigureCanvas继承自QtWidgets.QWidget)
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

"""
plt plt.rcParams['font.sans-serif'] 相關文章
https://jnturtle.blogspot.com/2020/02/python-matplotlib.html
"""
plt.rcParams['font.sans-serif'] = ["DFKai-SB"] # 標楷體
plt.rcParams['axes.unicode_minus'] = False  # 正常顯示負號


"""
將 QtWidget 提升類別至 MW_SIN
此例 f1 原是 QWidget 類別 提升至 MW_SIN
則生成這個類別的物件時，會自動從 標題檔 引入 類別
此例價等 from MatplotlibWidget import MW_SIN
"""
class MW_SIN(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(MW_SIN, self).__init__(parent)
        self.initUi()

    def initUi(self):
        self.layout = QtWidgets.QVBoxLayout(self)
        self.FC = MW_SIN_Canvas(self, width=1, height=0.5, dpi=100)
        self.layout.addWidget(self.FC)
 
class MW_SIN_Canvas(FigureCanvas):
    def __init__(self, parent=None, width=3.5, height=2, dpi=100):
        #
        self.fig = plt.Figure(figsize=(width,height), dpi=dpi)
        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)
        # 
        self.axlineShow = True
        self.axes_xFollow = False
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_figure)
        self.fig.canvas.mpl_connect('motion_notify_event', self.on_plot_hover)  
        self.fig.canvas.mpl_connect('button_press_event', self.__onclick__)
        self.fig.suptitle('Sin圖')       
        # 添加軸
        self.axes = [self.fig.add_subplot(111, autoscale_on=True)] # sin軸
        self.axes[0].set_gid("sin軸")
        self.axes[0].set_ylabel("sin")
        self.axes[0].grid(True)
        self.axes.append(self.axes[0].twinx()) # 輔助線軸
        self.axes[1].set_gid("輔助線軸")
        self.axes[1].get_yaxis().set_visible(False) # 輔助線軸不顯示y軸
        self.axes.append(self.axes[0].twinx()) # sin2軸
        self.axes[2].set_gid("sin2軸")
        self.axes[2].set_ylabel("sin2")
        # 添加線
        self.x = np.arange(0.0,3.0,0.01)
        self.y = np.sin(2 * np.pi * self.x)*2      
        self.y2 = np.sin(2 * np.pi * self.x)*-1   
        self.line_sin, = self.axes[0].plot(self.x, self.y, lineWidth=1, gid = "sin", label = "sin")        
        self.hline_mouse = self.axes[1].axhline(lineWidth=0.5, color = "#000000", ls = "--", gid = "axline", label = "輔助線")   
        self.line_sin2, = self.axes[2].plot(self.x, self.y2, lineWidth=1, gid = "sin2", color = "orange", label = "sin2")    
        self.axes_xDatum = self.axes[0].get_xlim()[0]
        self.axes_xWidth = 3
        # 產生圖例
        self.fig.legend(loc = 3) # loc: 3 圖片下左


    def update_figure(self):
        self.x = np.append(self.x, self.x[-1]+0.01)
        self.y = np.append(self.y, np.sin(2 * np.pi * self.x[-1])*2)
        self.y2 = np.append(self.y2, np.sin(2 * np.pi * self.x[-1])*-1)
        self.line_sin.set_data(self.x, self.y)
        self.line_sin2.set_data(self.x, self.y2)
        if self.axes_xFollow:
            self.axes_xDatum = self.x[-1]
            self.axes[0].set_xlim(self.axes_xDatum - self.axes_xWidth, self.axes_xDatum)
        self.draw()

    def setWidth(self, width, xDatum = None):
        self.axes_xWidth = width
        #
        if xDatum is None:
            if self.axes_xFollow: self.axes_xDatum = self.x[-1]                
            else: self.axes_xDatum = self.axes[0].get_xlim()[0]   
        else:
            self.axes_xDatum = xDatum
        # 
        if self.axes_xFollow:
            self.axes[0].set_xlim(self.axes_xDatum - self.axes_xWidth, self.axes_xDatum)
        else:
            self.axes[0].set_xlim(self.axes_xDatum, self.axes_xDatum+self.axes_xWidth)
        self.draw()

    def valueConvert(self, value, axesNo1, axesNo2=-1):
        xmin1, xmax1 = self.axes[axesNo1].get_ylim()
        xmin2, xmax2 = self.axes[axesNo2].get_ylim()
        value = value - (xmax2 + xmin2)/2 
        value = value * (xmax1 - xmin1)/(xmax2 - xmin2) 
        value = value + (xmax1 + xmin1)/2
        return value

    def on_plot_hover(self, event):
        if event.ydata is not None:
            if self.axlineShow : 
                if len(self.axes[1].get_lines()) == 0:
                    self.axes[1].add_line(self.hline_mouse)
                # event.ydata 是 最後一個雙生軸的y值，如果想得到前面雙生軸的y值，需要經過換算
                # 因為共用x軸，所以不用計算x值
                value = self.valueConvert(event.ydata, axesNo1=1, axesNo2=-1)
                self.hline_mouse.set_ydata(value)
                self.draw()           
            # 依序遞迴軸與其軸上的線，尋找有包含事件座標的線。
            for i in range(len(self.axes)):
                if i == 1: continue #輔助線不顯示
                for line in self.axes[i].get_lines():
                    if line.contains(event)[0]:
                        value = self.valueConvert(event.ydata, axesNo1=i, axesNo2=-1)
                        print("line_gid: {:<5}, axes_gid: {:<5}, x:{:>6.2f}, y:{:>6.2f}".format(line.get_gid(), line.axes.get_gid(), event.xdata, value))
        pass


    def __onclick__(self,click):
        self.point = (click.xdata,click.ydata)
        print(self.point)
        return self.point