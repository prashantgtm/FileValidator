from dbconnection import DbConnection
import sys


class Validator:
    def __init__(self, clientName, fileName):
        self.clientName = clientName
        self.fileName = fileName

    def validateFile(self):
        pass


if __name__ == '__main__':
    validator = Validator()
    validator.validateFile()
