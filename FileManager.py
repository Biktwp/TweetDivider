class FileManager:

    def __init__(self, path, separator):
        self.__path = path
        self.__separator = separator
        self.__file = open(path, "r+")
        self.__data = self.__file.read()

    def getAllData(self):
        return [i.split(self.__separator) for i in self.__data.split("\n")]

    def getAllLines(self):
        return [i for i in self.__data.split("\n")]

    # def __setSeparator(self, separator):
    #     if separator is None: return ""
    #     return separator

