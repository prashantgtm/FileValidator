import ConfigParser


class ConfigReader:
    def __init__(self):
        pass

    def readConfig(self):
        config = ConfigParser.RawConfigParser()
        config.read('config.ini')
        return config


