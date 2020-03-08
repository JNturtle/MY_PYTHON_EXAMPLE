"""將當前資料夾的 .ui 檔，轉成 .py 檔"""

def trans_ui2py():    
    import os
    dir = os.path.split(os.path.realpath(__file__))[0]
    cmd = "cd " + dir
    os.system(cmd) # 進到當前資料夾
    for file_name in [each for each in os.listdir(dir) if each.split(".")[-1] == "ui"]:   
        cmd = "python -m PyQt5.uic.pyuic -o " + dir + "\\ui_" + file_name.split(".")[0] + ".py " + dir + "\\" + file_name
        os.system(cmd) # 將 .ui 檔轉譯
trans_ui2py()