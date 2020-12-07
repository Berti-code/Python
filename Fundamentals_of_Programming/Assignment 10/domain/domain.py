class Cell:
    def __init__(self,value,line,column):
        self.__value=value
        self.__line=line
        self.__column=column

    def get_value(self):
        return self.__value

    def get_line(self):
        return self.__line
    
    def get_column(self):
        return self.__column

    def set_value(self,value):
        self.__value=value

    def set_line(self,line):
        self.__line=line

    def set_column(self,column):
        self.__column=column