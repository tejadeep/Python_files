import logging
logging.basicConfig(filename='log.txt',level=logging.ERROR)
print("********* DEMO ***********")
logging.debug("********** Debug *******")
logging.warning("***** warning ********")
logging.error("******** Error ******")
logging.critical("****** Critical ******")
