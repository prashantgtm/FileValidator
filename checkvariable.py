import re


class CheckVariable:
    def __init__(self):
        pass

    @staticmethod
    def isVarchar(value):
        if re.match('^[0-9a-zA-Z]+$', value):
            return True
        else:
            return False

    @staticmethod
    def isInteger(value):
        if re.match('^[0-9]+$', value):
            return True
        else:
            return False

    @staticmethod
    def isDatetime(value):

        if re.match('(?:(20[0-9]{2})|([0-3][0-9]))[-/][0-1][0-9][-/](?:(20[0-9]{2})|([0-3][0-9]))', value):
            return True
        else:
            return False

    @staticmethod
    def isTimestamp(value):
        pass

if __name__ == '__main__':
    print CheckVariable.isDatetime('2015-12-29')
