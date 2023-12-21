from Model.Square import Square
from Constants.Global import SCORES
class Game:
    def __init__(self, current_player):
        self.squares = []
        self.current_player = current_player
        self.count_turns = 0


    def create_board(self,initial_state):

        cols = len(initial_state[0])
        max_pieces = 6

        for col in range(cols):

            red_pieces, black_pieces, distribution_pieces = self.obtain_info_square(initial_state, col)

            if col == 0 or col == 7:
                max_pieces = float('inf')

            square = Square(col,"Final", SCORES[col], max_pieces, red_pieces, black_pieces, distribution_pieces)
            self.squares.append(square)

    def obtain_info_square(self, state, col):

        rows = len(state)
        count_red_pieces = 0
        count_black_pieces = 0
        distribution_pieces = []

        for row in range(rows):
            piece = state[row][col]
            if piece == "1":
                count_red_pieces += 1
            else:
                count_black_pieces += 1

            distribution_pieces.append(piece)
        
        return count_red_pieces, count_black_pieces, distribution_pieces



    def update_current_player(self,player):
        self.current_player = player