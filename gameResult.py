import tkinter as tk

class GameResult:
  def __init__(self):
      self.red_score = 0
      self.black_score = 0
      self.red_columns = set()
      self.black_columns = set()
  
  def check_winner(self, game_board):
      
      for i in range(len(game_board)):
          for j in range(len(game_board[i])):
              if game_board[i][j] == 1:
                  self.red_columns.add(j)
              elif game_board[i][j] == 2:
                  self.black_columns.add(j)

      if not self.red_columns.intersection(self.black_columns):
          print("Game Over!")
          self.score(game_board)
          self.show_winner(True)
          return True
      else:
          self.red_columns.clear()
          self.black_columns.clear()
          
  def score(self, game_board):

      for j in self.red_columns:
          count = sum(1 for i in range(len(game_board)) if game_board[i][j] == 1)
          if j == 4:
              self.red_score += 1 * count
          elif j == 5:
              self.red_score += 2 * count
          elif j == 6:
              self.red_score += 3 * count
          elif j == 7:
              self.red_score += 5 * count

      for j in self.black_columns:
          count = sum(1 for i in range(len(game_board)) if game_board[i][j] == 2)
          if j == 3:
              self.black_score += 1 * count
          elif j == 2:
              self.black_score += 2 * count
          elif j == 1:
              self.black_score += 3 * count
          elif j == 0:
              self.black_score += 5 * count

      print(f"Red Score: {self.red_score}")
      print(f"Black Score: {self.black_score}")
  
  def show_winner(self, winner):
      if winner:
          if self.red_score > self.black_score:
              print("Red Wins!")
          elif self.red_score < self.black_score:
              print("Black Wins!")
          else:
              print("Draw!")
    
  
  def reset_game(self):
      self.red_score = 0
      self.black_score = 0
