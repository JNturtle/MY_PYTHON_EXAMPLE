"""
programD 跑我一個，卡你一核
將其中一個檔名改成這個，觀察是否會跟主程式擠在同一核。
>>>用cmd執行別的程式不會擠在同一核。
"""

import time
from myLogger import mylogger 
logger = mylogger.getLogger("ProgramD", fileName="PD.log")
logger.warning('將來會無限循環造成一核雍塞，關掉cmd就能夠解決')

i = 1
while 1:
    i = i + 1
