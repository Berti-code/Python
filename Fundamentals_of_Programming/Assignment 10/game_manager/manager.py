class Manager:
    def __init__(self,board):
        self.__board=board

    def get_board(self):
        return self.__board

    def get_game_board(self):
        return self.get_board().get_game_board()

    def set_board(self,line,column,value):
        self.__board.set_value_to_board(line,column,value)

    def validate_orientation_input(self,orientation_input):
        if orientation_input not in ['N','S','W','E']:
            raise ValueError('Invalid orientation!')

    def get_ship_end_position(self,line,column,orientation,ship_lenght):
        end_line=line
        end_column=column
        if orientation=='N':
            if line>=ship_lenght-1:
                end_line=line-ship_lenght+1
            else:
                raise ValueError('Ship impossible to place!')
        if orientation=='S':
            if line<=7-ship_lenght+1:
                end_line=line+ship_lenght-1
            else:
                raise ValueError('Ship impossible to place!')
        if orientation=='W':
            if column>=ship_lenght-1:
                end_column=column-ship_lenght+1
            else:
                raise ValueError('Ship impossible to place!')
        if orientation=='E':
            if column<=7-ship_lenght+1:
                end_column=column+ship_lenght-1
            else:
                raise ValueError('Ship impossible to place!')
        return end_line,end_column
            
    def record_on_the_board(self,start_line,start_column,end_line,end_column,value):
        delta_Y=start_line-end_line
        delta_X=start_column-end_column
        print('dY=',delta_Y)
        print('dX=',delta_X)
        ship_lenght=max([abs(delta_X),abs(delta_Y)])+1

        line=start_line
        column=start_column
        for i in range(ship_lenght):
            #print(line,column)
            #self.get_board().set_value_to_board(line,column,value)
            #self.__board.set_value_to_board(line,column,value)
            self.set_board(line,column,value)
            if delta_Y > 0:
                line-=1
            if delta_Y < 0:
                line+=1#
            if delta_X > 0:
                column-=1
            if delta_X < 0:
                column+=1#

    def place_ship(self,ship_line,ship_column,ship_orientation,ship_lenght,value):
        self.validate_orientation_input(ship_orientation)
        end_line,end_column=self.get_ship_end_position(ship_line,ship_column,ship_orientation,ship_lenght)
        print('start:',ship_line,ship_column)
        print('end:',end_line,end_column)
        self.record_on_the_board(ship_line,ship_column,end_line,end_column,value)

    def place_battleship(self,battleship_line,battleship_column,battleship_orientation):
        value=1#player's ships fill in the grid with ones
        ship_lenght=4#battleship's lenght is 4
        self.place_ship(battleship_line,battleship_column,battleship_orientation,ship_lenght,value)


    def register_move(self,line,column):
        #TODO: check validity
        pass

    def player_move(self):
        pass

    def computer_move(self):
        pass