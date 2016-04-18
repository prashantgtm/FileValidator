import re


class CheckVariable:
    def __init__(self):
        pass

    @staticmethod
    def isVarchar(value):
        if str(value):
            return True
        elif value == '':
            return True
        else:
            print value
            return False

    @staticmethod
    def isInteger(value):
        if re.match('^[0-9].$', value):
            return True
        else:
            return False

    @staticmethod
    def isDatetime(value):
        if re.match('(?:(?:(20[0-9]{2})'
                    '[-/.](?:([0][1-9])|([1][0-2]))'
                    '[-/.](?:([0][1-9])|([1-2][0-9])'
                    '|([3][0-2])))|(?:(?:([0][1-9])|'
                    '([1-2][0-9])|([3][0-2]))[-/.]'
                    '(?:([0][1-9])|([1][0-2]))[-/.](20[0-9]{2})))', value):
            return True
        else:
            return False

    @staticmethod
    def isEmail(value):
        if re.match('^.+@.+[com|net]', value.lower()):
            return True
        else:
            return False

    @staticmethod
    def isTimestamp(value):
        pass





