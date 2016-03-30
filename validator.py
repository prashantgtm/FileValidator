from queries import Queries
from readfile import ReadFile
from checkvariable import CheckVariable


class Validator(object):
    def __init__(self, clientName, fileName, fileType):
        self.clientName = clientName
        self.fileName = fileName
        self.fileType = fileType
        self.queries = Queries()
        self.rawTableName = self.queries.getRawTableName(self.clientName, self.fileName)
        self.readfile = ReadFile(self.fileName, self.clientName, self.fileType)
        if self.validateHeader() is False:
            exit('Header mismatch')
        if self.validateContent() is True:
            exit(0)
        else:
            exit('Content mismatch')

    def validateHeader(self):
        databaseHeader = self.queries.getDatabaseColumns('raw_file_columns', self.clientName, self.rawTableName)
        fileHeader = self.readfile.getFileHeader()
        for i in range(len(databaseHeader)):
            if databaseHeader[i] != fileHeader[i]:
                return False
        return True

    def validateContent(self):
        dataType = self.queries.getDatabaseColumns('data_type', self.clientName, self.rawTableName)
        fileContent = self.readfile.getFileContent()
        for line in fileContent:
            for i in range(len(dataType)):
                if dataType[i] == 'int':
                    if CheckVariable.isInteger(line[i]) is False:
                        return False
                elif dataType[i] == 'varchar':
                    if CheckVariable.isVarchar(line[i])is False:
                        return False
                elif dataType[i] == 'datetime':
                    if CheckVariable.isDatetime(line[i])is False:
                        return False
                elif dataType[i] == 'email':
                    if CheckVariable.isEmail(line[i]) is False:
                        return False
                else:
                    return False
        return True


if __name__ == '__main__':
    validator = Validator('', '', '')

