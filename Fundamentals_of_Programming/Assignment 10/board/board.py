from domain.domain import Cell

class Grid:
    def __init__(self):
        self.__grid=[]
        self.initialise_board()

    def initialise_board(self):
        for i in range(8):
            line=[]
            for i in range(8):
                line.append(0)
            self.__grid.append(line)

    def get_game_board(self):
        return self.__grid

    def set_value_to_board(self,line,column,value):
        print('line=',line)
        print('column=',column)
        
        
        self.__grid[line][column]=value
        print(self.__grid[line][column])