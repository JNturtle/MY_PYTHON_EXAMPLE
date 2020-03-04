"""從這裡執行才能正常啟用"""
from PyQt5 import QtWidgets

if __name__ == '__main__':
    import sys
    print(sys.getdefaultencoding())
    import ui2py
    import fuc_main_mlt
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = fuc_main_mlt.MYMAINWINDOW()
    MainWindow.show()
    app.exec()