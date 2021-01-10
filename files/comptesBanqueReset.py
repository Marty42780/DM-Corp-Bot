import pickle

comptesBanque = {}

pickle.dump(comptesBanque, open('comptesBanqueFile', 'wb'))

print ('Fichier comptesBanqueFile reset')

import logging
def logging ():
    fileObject = open(r"File_Name","Access_Mode")
logging.basicConfig(format='%(asctime)s - %(levelname)-10s %(message)s',
    datefmt='%Y-%m-%d:%H:%M:%S',
    level=logging.DEBUG)

logger = logging.getLogger(__name__)
logger.debug("This is a debug log")
logger.info("This is an info log")
logger.critical("This is critical")
logger.error("An error occurred")