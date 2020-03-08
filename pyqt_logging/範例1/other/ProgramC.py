"""
programC 跑到第5秒時會報錯，而且沒有設置例外
"""

import time
from myLogger import mylogger 
logger = mylogger.getLogger("ProgramC", fileName="PC.log")
logger.error('壽命只剩下4秒 第5秒就會死~~')
logger.info('START')
for i in range(5):
    if i == 4: 
        logger.warning("即將出錯...") 
        i = 4 + "dead"
        logger.critical("來不及說遺言...") 
    logger.info("progress:{:}/5".format(i+1)) 
    time.sleep(1)
logger.info('DONE')    
