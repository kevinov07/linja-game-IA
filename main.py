import tkinter as tk

from Constants.Global import PIECES_IMAGES, GAME_BOARD
from View.board import GameBoardApp
from Model.Game import Game



def load_initial_game_board(filename="board1.txt"):
  with open(filename, "r") as file:
    lines = file.readlines()
    initial_state = [list(line.strip().split()) for line in lines]
  return initial_state
    
initial_state = load_initial_game_board()

print(initial_state)

game = Game(initial_state , "1", "1")

print(game.obtain_state_matrix())
for square in game.squares:
  print(square)

game.get_possible_movements()
#first_moves = game.get_first_moves()
#print(first_moves)
print(game.get_AI_score())
print(game.get_human_score())
print(game.get_heuristic())
#game.move_piece(first_moves[0])
for square in game.squares:
  print(square)

print(game.check_final_state())
root = tk.Tk()
root.title("Linja Game")


app = GameBoardApp(root, initial_state, PIECES_IMAGES)

root.mainloop()