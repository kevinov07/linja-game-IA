import tkinter as tk

from Constants.Global import PIECES_IMAGES, GAME_BOARD
from View.board import GameBoardApp



def load_initial_game_board(filename="board1.txt"):
  with open(filename, "r") as file:
    lines = file.readlines()
    initial_state = [list(line.strip().split()) for line in lines]
  return initial_state
    
initial_state = load_initial_game_board()

root = tk.Tk()
root.title("Linja Game")


app = GameBoardApp(root, initial_state, PIECES_IMAGES)

root.mainloop()