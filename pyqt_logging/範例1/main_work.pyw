"""從這裡執行才能正常啟用"""

if __name__ == '__main__':      
    from sys import argv
    from win32gui import FindWindow 
    from PyQt5.QtWidgets import QApplication, QMessageBox   
    app = QApplication(argv)
    # 如果不存在同名的window，就執行。有則提示。
    if FindWindow(None, "qt_work")  == 0:   # MainWindow windowTitle: qt_work   
        import ui2py
        import fuc_main_work        
        MainWindow = fuc_main_work.MYMAINWINDOW()
        MainWindow.show()
        app.exec()
    else:
        QMessageBox.critical(None, "只能運行一個", "本程式只能運行一個！", QMessageBox.Yes, QMessageBox.Yes)


