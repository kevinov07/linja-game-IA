import tkinter as tk

from Constants.Global import PIECES_IMAGES, GAME_BOARD
from View.board import GameBoardApp


root = tk.Tk()
root.title("Linja Game")


app = GameBoardApp(root, GAME_BOARD, PIECES_IMAGES)

root.mainloop()