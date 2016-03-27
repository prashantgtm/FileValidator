from dbconnection import DbConnection
import re


class Queries:
    def __init__(self):
        self.connection = DbConnection()
        self.schema = 'shared_etl'

    def getRawTableName(self, clientName, fileName):
        cursor = self.connection.getDbConnection
        query = "Select `reqexp` from %s.raw_control where client_name ='%s';" % (
            self.schema, clientName)
        try:
            cursor.execute(query)
        except Exception as error:
            exit(error)
        regList = cursor.fetchall()
        for regExp in regList:
            if re.match(regExp[0], fileName):
                query = "Select `table_name` from %s.raw_control where client_name = '%s' and `regexp` = '%s'" % (
                    self.schema, clientName, regExp[0])
        try:
            cursor.execute(query)
        except Exception as error:
            exit(error)
        tableName = cursor.fetchone()
        self.connection.closeConnection()
        return tableName

    def getDatabaseColumns(self, columnName, clientName, rawTable):
        cursor = self.connection.getDbConnection
        query = "Select `%s` from %s.metadata_control where client_name = '%s' and raw_table_name = '%s' and raw_file_columns <> 'null';" % (
            columnName, self.schema, clientName, rawTable)
        try:
            cursor.execute(query)
        except Exception as error:
            exit(error)
        columns = cursor.fetchall()
        dbColumns = []
        for eachColumn in columns:
            eachColumn = [x.strip(',') for x in eachColumn]
            dbColumns.append(eachColumn[0])
        self.connection.closeConnection()
        return dbColumns
