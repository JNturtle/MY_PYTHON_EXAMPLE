"""JN BLOG: https://jnturtle.blogspot.com/"""

import logging

if 1:
    import logging

    loggerName = "test"
    fileName = "hello.log"

    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger(loggerName) 
    FileHandler = logging.FileHandler(fileName)
    FileHandler.setLevel("ERROR")
    logger.addHandler(FileHandler)

    logger.info("哈囉")
    logger.debug("這個不會顯示出來 INFO > DEBUG")
    logger.warning("注意下一個訊息")
    logger.error("只有這個會被保存在log")


if 0:
    import logging
    
    loggerName = "test"
    loggerName2 = "test2"
    fmt = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
    logger = logging.getLogger(loggerName) 
    logger2 = logging.getLogger(loggerName2) 
    logger.setLevel("DEBUG")
    logger2.setLevel("DEBUG")
    StreamHandler = logging.StreamHandler()
    StreamHandler.setLevel("INFO")
    StreamHandler.setFormatter(fmt)
    StreamHandler2 = logging.StreamHandler()
    StreamHandler2.setLevel("ERROR")
    StreamHandler2.setFormatter(fmt)
    logger.addHandler(StreamHandler)
    logger2.addHandler(StreamHandler2)

    for lg in [logger, logger2]:
        print(lg.getEffectiveLevel())
        lg.info("哈囉")
        lg.debug("這個如何")
        lg.warning("那這個呢")
        lg.error("最後一個")

if 0:
    import logging
    from logging import config
    
    configName = "logging.conf"
    loggerName = "test"
    loggerName2 = "test2"

    config.fileConfig(configName)
    logger = logging.getLogger(loggerName) 
    logger2 = logging.getLogger(loggerName2) 

    for lg in [logger, logger2]:
        print(lg.getEffectiveLevel())
        lg.info("哈囉")
        lg.debug("這個如何")
        lg.warning("那這個呢")
        lg.error("最後一個")


if 0:
    import logging
    from logging import config
    
    configName = "logging.conf"
    loggerName = "test"
    loggerName2 = "test2"

    config.fileConfig(configName)
    logger = logging.getLogger(loggerName) 
    logger2 = logging.getLogger(loggerName2) 

    fmt = logging.Formatter("%(name)s - %(levelname)s - %(message)s - root SH 20")
    StreamHandler = logging.StreamHandler()
    StreamHandler.setFormatter(fmt)
    StreamHandler.setLevel(20)
    fmt2 = logging.Formatter("%(name)s - %(levelname)s - %(message)s - root SH2 40")
    StreamHandler2 = logging.StreamHandler()
    StreamHandler2.setFormatter(fmt2)
    StreamHandler2.setLevel(40)
    logging.root.addHandler(StreamHandler)
    logging.root.addHandler(StreamHandler2)

    logger.setLevel(10)
    logger2.setLevel(30)
    logging.root.setLevel(20)

    for lg in [logger, logger2]:
        lg.info("20")
        lg.debug("10")
        lg.warning("30")
        lg.error("40")
