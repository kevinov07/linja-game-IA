import tkinter as tk
from Minimax.minimax import minimax
from Constants.Global import PIECES_IMAGES, GAME_BOARD
from View.board import GameBoardApp
from Model.Game import Game



def load_initial_game_board(filename="board1.txt"):
  with open(filename, "r") as file:
    lines = file.readlines()
    initial_state = [list(line.strip().split()) for line in lines]
  return initial_state
    
initial_state = load_initial_game_board()

#print(initial_state)

#game = Game(initial_state , "2", 1, 1)
#best_score, best_move = minimax(initial_state, "2", 1, 1, 4, 0)

"""
print(game.obtain_state_matrix())
for square in game.squares:
  print(square)


first_moves = game.get_possible_movements()
print("primeros movimientos", first_moves)
game.move_piece(first_moves[0])
new_state = game.obtain_state_matrix()
game.create_board(new_state)

print("Después del primer movimiento queda así el tablero")
for square in game.squares:
  print(square)

game.type_movement = 2
game.turn_max_movements = first_moves[0]['movements']

seconds_moves = game.get_possible_movements()
print("segundos movimientos", seconds_moves)

print("Después del segundo movimiento queda así el tablero")
for square in game.squares:
  print(square)
"""


#print(game.check_final_state())
root = tk.Tk()
root.title("Linja Game")


app = GameBoardApp(root, initial_state, PIECES_IMAGES)

root.mainloop()