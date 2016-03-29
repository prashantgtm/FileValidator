import csv
from configreader import ConfigReader


class ReadFile(object):
    def __init__(self, file, clientName, fileType):
        configreader = ConfigReader()
        config = configreader.readConfig()
        fileDelimiter = config.get(clientName, fileType + '.delimiter')
        self.fileTopOffset = int(config.get(clientName, fileType + '.topOffset'))
        self.fileLeftOffset = int(config.get(clientName, fileType + '.leftOffset'))

        try:
            with open(file, 'rb') as csvfile:
                file = csv.reader(csvfile.read().decode('utf-8-sig').encode('utf-8').splitlines(),
                                  delimiter=fileDelimiter, quotechar='"')
                self.data = []
                for line in file:
                    self.data.append(line)
        except Exception as error:
            exit(error)

    def getFileHeader(self):
        header = self.data[self.fileTopOffset]
        for i in range(self.fileLeftOffset):
            header.pop(0)
        return header

    def getFileContent(self):
        content = self.data[(self.fileTopOffset+1):]
        for line in content:
            for i in range(self.fileLeftOffset):
                line.pop(0)
        return content


if __name__ == '__main__':
    readfile = ReadFile('D:\Leapfrog\\newmodel\\files\candidates.03.22.2016.08.45.csv',
                        'correctcare', 'candidate')
    print readfile.getFileHeader()
    for eachrow in readfile.getFileContent():
        print eachrow

