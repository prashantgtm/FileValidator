from dbconnection import DbConnection
import re


class Queries:
    def __init__(self):
        connection = DbConnection()
        self.cursor = connection.getDbConnection
        self.schema = ''

    def getRawTableName(self, clientName, fileName):
        query ="Select `reqexp` from %s.raw_control where client_name ='%s';" % (self.schema, clientName)
        try:
            self.cursor.excute(query)
        except Exception as error:
            exit(error)
        regList = self.cursor.fetchall()
        for regExp in regList:
            if re.match(regExp[0], fileName):
                query = "Select `table_name` from %s.raw_control where client_name = '%s' and `regexp` = '%s'" % (self.schema, clientName, regExp[0])
        try:
            self.cursor.execute(query)
        except Exception as error:
            exit(error)
        tableName = self.cursor.fetchone()
        return tableName

    def getDatabaseHeader(self, clientName, rawTable):
        query = "Select raw_file_columns from %s.metadata_control where client_name = '%s' and raw_table_name = '%s' and raw_file_columns <> 'null';" % (self.schema, clientName, rawTable)
        try:
            self.cursor.execute(query)
        except Exception as error:
            exit(error)
        columns = self.cursor.fetchall()
        dbColumns = []
        for each in columns:
            each =[x.strip(',') for x in each]
            dbColumns.append(each[0])
        return dbColumns




