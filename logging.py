import logging
import datetime


class Logging:
    def __init__(self):
        self.logPath = ''

    def initiateLog(self, clientName):
        logfile = clientName + "-Log-" + datetime.now().strftime("%d-%b-%Y")
        logging.basicConfig(filename=self.logPath + logfile,
                            format='%(asctime)s %(levelname)s %(message)s',
                            level=logging.INFO,
                            datefmt='%m/%d/%Y %I:%M:%S %p')
        logging.INFO('---------------START OF THE EXECUTION-----------------')
