from dbconnection import DbConnection
import re


class Queries:
    def __init__(self):
        dbconnection = DbConnection()
        self.schema = 'shared_etl'
        self.conn = dbconnection.getDbConnection()

    def getRawTableName(self, clientName, fileName):

        cursor = self.conn.cursor()
        query = "Select `regexp` from %s.raw_control where client_name ='%s';" % (
            self.schema, clientName)
        try:
            cursor.execute(query)
        except Exception as error:
            exit(error)
        regList = cursor.fetchall()
        for regExp in regList:
            if re.match(regExp[0], fileName):
                query1 = "Select `table_name` from %s.raw_control where client_name = '%s' and `regexp` = '%s'" % (
                    self.schema, clientName, regExp[0])
        try:
            cursor.execute(query1)
        except Exception as error:
            exit(error)
        tableName = cursor.fetchone()
        return tableName[0]

    def getDatabaseColumns(self, columnName, clientName, rawTable):
        cursor = self.conn.cursor()

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
        cursor.close()
        return dbColumns

if __name__ == '__main__':
    queries = Queries()
    tablename = queries.getRawTableName('correctcare', 'candidates.03.22.2016.08.45.csv')
    print queries.getDatabaseColumns('raw_file_columns','correctcare',tablename)


