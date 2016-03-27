from configreader import ConfigReader
import MySQLdb
import sys


class DbConnection:
    def __init__(self):
        configreader = ConfigReader()
        config = configreader.readConfig()
        host = config.get('database', 'host')
        username = config.get('database', 'username')
        password = config.get('database', 'password')
        schema = config.get('database', 'schema')
        try:
            self.conn = MySQLdb.connect(host, username, password, schema)
        except Exception as error:
            sys.exit(error)

    def getDbConnection(self):
        cursor = self.conn.cursor()
        return cursor

    def closeConnection(self):
        self.conn.close()


