"""從這裡執行才能正常啟用"""
from PyQt5 import QtWidgets

if __name__ == '__main__':
    import sys
    import ui2py
    import fuc_main_mlt2
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = fuc_main_mlt2.MYMAINWINDOW()
    MainWindow.show()
    app.exec()