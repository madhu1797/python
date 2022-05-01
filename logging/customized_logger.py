import logging

#Method - 1
logging.basicConfig(level = logging.DEBUG, filename= "test.log", filemode = "w", format="%(asctime)s - %(message)s")
logger = logging.getLogger(__name__)

logging.debug("Redirected customized logs - in method1")

#Method - 2

handler = logging.FileHandler("test.log")
formatter = logging.Formatter("%(asctime)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

logging.debug("Redirected customized logs via file handler")
