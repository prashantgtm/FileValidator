from configreader import ConfigReader
import MySQLdb
import sys


class DbConnection:
    def __init__(self):
        configreader = ConfigReader()
        self.config = configreader.readConfig()

    def getDbConnection(self):
        host = self.config.get('database', 'host')
        username = self.config.get('database', 'username')
        password = self.config.get('database', 'password')
        schema = self.config.get('database', 'schema')

        try:
            connection = MySQLdb.connect(host, username, password, schema)
        except Exception as error:
            sys.exit(error)
        return connection


if __name__ == '__main__':
    conn =DbConnection()
    conn.getDbConnection()



