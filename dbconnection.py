import MySQLdb
import sys


class DbConnection:
    def __init__(self):
        self.host = ''
        self.username = ''
        self.password = ''
        self.defaultSchema = ''

    def getDbConnection(self):
        try:
            connection = MySQLdb.connect(self.host, self.username, self.password, self.defaultSchema)
        except Exception as error:
            sys.exit(error)
        cursor = connection.cursor()
        return cursor

if __name__ == '__main__':
    conn = DbConnection()
    conn.getDbConnection()
