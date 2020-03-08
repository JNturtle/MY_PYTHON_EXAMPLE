"""
programA 故意設計來測試錯誤情形下反應
"""

import time
from myLogger import mylogger 
logger = mylogger.getLogger("ProgramA", fileName="PA.log")
logger.debug('就是故意來出錯的 ya')
try:
    logger.info('START')
    print("2"+1) # 型態不合，一定出錯。
    time.sleep(2)
    logger.info('DONE')    
except TypeError:
    logger.error("類型錯誤")


