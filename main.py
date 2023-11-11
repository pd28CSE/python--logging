from main_logger import logger


logger.warning("warning message")
logger.debug("this is debug mode")
logger.info("this is info")
logger.warning("this is warning")
logger.error("this is error")
logger.critical("this is critical")


try:
    a = 1 / 0
    print(a)

except Exception as e:
    logger.critical(str(e))
