"""
programB 具有長達30秒的任務時間
"""

import time
from myLogger import mylogger 
logger = mylogger.getLogger("ProgramB", fileName="PB.log")
logger.debug('執行中，預期跑個30秒')
try:
    logger.info('START')
    for i in range(30):
        logger.info("progress:{:}/30".format(i+1)) 
        time.sleep(1)
    logger.info('DONE')    
except TypeError:
    logger.error("ERROR")