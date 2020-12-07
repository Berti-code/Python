class UI:
    def __init__(self,game_manager):
        self.__game_manager=game_manager

    def print_board(self):
        board=self.__game_manager.get_game_board()
        for i in range(8):
            for j in range(8):
                print(board[i][j],end=' ')
            print()

    def player_move(self):
        line=int(input('line='))
        column=int(input('column='))
        self.__game_manager.player_move(line,column)

    def player_place_ships(self):
        print('Battleship(4 squares) position:')
        battleship_line=int(input('Battleship line(Y axis)='))
        battleship_column=int(input('Battleship column(Y axis)='))
        battleship_orientation=input('Select battleship orientation from [N,S,W,E]:')
        self.__game_manager.place_battleship(battleship_line,battleship_column,battleship_orientation)
        '''
        print('Cruiser(3 squares) position:')
        cruiser_line=int(input('Cruiser line(Y axis)='))
        cruiser_column=int(input('Cruiser column(Y axis)='))
        cruiser_orientation=input('Select cruiser orientation from [N,S,W,E]:')
        self.__game_manager.place_cruiser(cruiser_line,cruiser_column,cruiser_orientation)

        print('Destroyer(2 squares) position:')
        destroyer_line=int(input('Destroyer line(Y axis)='))
        destroyer_column=int(input('Destroyer column(Y axis)='))
        destroyer_orientation=input('Select destroyer orientation from [N,S,W,E]:')
        self.__game_manager.place_destroyer(destroyer_line,destroyer_column,destroyer_orientation)
        '''
    def run_game(self):
        self.print_board()
        self.player_place_ships()
        self.print_board()
        #place battleships
        '''
        whie True:
            get player move
            make the computer move
            print outcome and targetting grid
        '''