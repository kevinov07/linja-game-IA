import tkinter as tk
from PIL import ImageTk, Image

class GameBoardApp:
    def __init__(self, root, game_board, info_entities_images):
        self.root = root
        self.game_board = game_board
        self.info_entities_images = info_entities_images
        self.cells = []
        self.turn_step = 0
        self.turn_max_movement = 1
        self.x_pos = 0
        self.y_pos = 0
        self.is_clicked = False

        self.create_game_board()

    def create_game_board(self):
        for i in range(len(self.game_board)):
            row = []
            for j in range(len(self.game_board[i])):
                cell_value = self.game_board[i][j]
                original_image = Image.open(self.info_entities_images[cell_value])
                resized_image = original_image.resize((100, 100))
                img = ImageTk.PhotoImage(resized_image)
                cell_label = tk.Button(
                    self.root,
                    borderwidth=1,
                    relief="solid",
                    background="white",
                    image=img,
                    anchor="center",
                    compound="center",
                    command=lambda row=i, col=j: self.on_cell_click(row, col),
                )
                cell_label.image = img
                cell_label.grid(row=i, column=j)
                row.append(cell_label)
            self.cells.append(row)

    def on_cell_click(self, row, col):
        if self.game_board[row][col] == 1 and self.is_clicked == False:
            self.x_pos = row
            self.y_pos = col
            self.is_clicked = True
            self.add_border(row, col)
        elif (self.is_clicked and not(self.has_valid_moves(self.y_pos))):
            self.remove_border(self.x_pos, self.y_pos)
            self.x_pos = 0
            self.y_pos = 0
            self.is_clicked = False
        elif (
            self.is_clicked
            and self.game_board[row][col] == 0
            and self.y_pos < col
            and col <= self.turn_max_movement + self.y_pos
        ):
            prev_values = self.game_board[self.x_pos][self.y_pos]
            self.game_board[self.x_pos][self.y_pos] = self.game_board[row][col]
            self.game_board[row][col] = prev_values
            self.is_clicked = False
            self.update_board(self.game_board)
            self.remove_border(self.x_pos, self.y_pos)
            if self.turn_step == 1:
                self.turn_step = 0
                self.turn_max_movement = 1
            elif self.turn_step == 0:
                self.turn_step = 1
                self.turn_max_movement = self.get_count_total_in_column(col)

    def update_board(self, new_board):
        for i in range(len(new_board)):
            for j in range(len(new_board[i])):
                cell_value = new_board[i][j]
                original_image = Image.open(self.info_entities_images[cell_value])
                resized_image = original_image.resize((100, 100))
                img = ImageTk.PhotoImage(resized_image)

                if self.cells[i][j].image:
                    self.cells[i][j].image = img
                    self.cells[i][j].configure(image=img)
                else:
                    cell_label = tk.Button(
                        self.root,
                        borderwidth=1,
                        relief="solid",
                        background="white",
                        image=img,
                        anchor="center",
                        compound="center",
                        command=lambda row=i, col=j: self.on_cell_click(row, col),
                    )
                    cell_label.image = img
                    cell_label.grid(row=i, column=j)
                    self.cells[i][j] = cell_label

    def add_border(self, row, col):
        self.cells[row][col].config(borderwidth=1, relief="sunken")

    def remove_border(self, row, col):
        self.cells[row][col].config(
            borderwidth=1,
            relief="solid",
        )
        
    def get_count_total_in_column(self,column):
        total_count = 0
        for i in range(len(self.game_board)):
            for j in range(len(self.game_board[i])):
                if column == j and (self.game_board[i][j] == 2 or self.game_board[i][j] == 1):
                    total_count += 1
        return total_count - 1
    
    def has_valid_moves(self,column):
        for i in range(len(self.game_board)):
            for j in range(len(self.game_board[i])):
                if column < j and (self.game_board[i][j] == 0):
                    return True
        return False
