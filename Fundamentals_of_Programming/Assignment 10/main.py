from board.board import Grid
from game_manager.manager import Manager
from UI.ui import UI

grid=Grid()
game_manager=Manager(grid)
ui=UI(game_manager)

ui.run_game()