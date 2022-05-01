import logging

logging.basicConfig(level = logging.DEBUG, filename= "test.log", filemode = "w", format="%(asctime)s - %(message)s")
logging.debug("Redirected logs")

