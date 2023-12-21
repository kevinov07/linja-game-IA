from Model.Square import Square
from Constants.Global import SCORES
import random

class Game:
    def __init__(self, init_state, current_player, current_type_movement):
        self.squares = []
        self.current_player = current_player
        self.postions_current_player = []
        self.possible_movements = []
        self.type_movement = current_type_movement
        self.create_board(init_state)


    def create_board(self,initial_state):

        cols = len(initial_state[0])

        for col in range(cols):
            max_pieces = 6
            type = "Normal"

            red_pieces, black_pieces, distribution_pieces = self.obtain_info_square(initial_state, col)

            if col == 0 or col == 7:
                max_pieces = float('inf')
                type = "Final"

            square = Square(col,type, SCORES[col], max_pieces, red_pieces, black_pieces, distribution_pieces)
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
            elif piece == "2":
                count_black_pieces += 1

            distribution_pieces.append(piece)
        
        return count_red_pieces, count_black_pieces, distribution_pieces



    def update_current_player(self,player):
        self.current_player = player

    def check_final_state(self):
        
        is_final_state = True

        for square in self.squares:
            if square.red_pieces != 6 or square.black_pieces !=6:
                is_final_state = False
                break
        return is_final_state
    

    def get_possible_movements(self):
        self.obtain_positions_current_player()
        print("Jugador que realiza los siguientes posibles movimientos:", self.current_player)
        if self.type_movement == "1":    
            print(self.postions_current_player)
            return self.get_first_moves()


    
    def get_first_moves(self):
        first_moves = []
        if self.current_player == "1":
            return self.get_first_moves_red()
        
        return self.get_first_moves_black()

    def get_first_moves_red(self):
        first_moves = []
        for col in range(len(self.postions_current_player) - 1):

            current_col = self.postions_current_player[col]

            if len(current_col['positions']) == 0: continue

            next_col = self.squares[current_col['col'] + 1] if current_col['col'] < 7 else self.squares[current_col['col']]
            if next_col.is_full(): continue

            next_col_availables_pos = next_col.get_empty_pos()
            row_index = next_col.pos + 1

            if len(next_col_availables_pos) != 0:
                row_index = random.choice(next_col_availables_pos)

            movement = self.get_movement_info(current_col['col'], random.choice(current_col['positions']), current_col['col'] + 1, row_index, next_col.get_total_pieces())
            first_moves.append(movement)

        return first_moves
    
    def get_first_moves_black(self):
        first_moves = []
        for col in range(len(self.postions_current_player) - 1, 0, -1):

            current_col = self.postions_current_player[col]

            if len(current_col['positions']) == 0: continue

            next_col = self.squares[current_col['col'] - 1] if current_col['col'] > 1 else self.squares[current_col['col']]
            if next_col.is_full(): continue

            next_col_availables_pos = next_col.get_empty_pos()
            row_index = next_col.pos - 1

            if len(next_col_availables_pos) != 0:
                row_index = random.choice(next_col_availables_pos)

            movement = self.get_movement_info(current_col['col'], random.choice(current_col['positions']), current_col['col'] - 1, row_index,  next_col.get_total_pieces())
            first_moves.append(movement)

        return first_moves

    def get_movement_info(self, col_origin, row_index, col_arrival, row_arrival, movements):
        movement = {
                "col_origin": col_origin,
                "row_origin": row_index,
                "col_arrival": col_arrival,
                "row_arrival": row_arrival,
                "movements": movements
            }
        
        return movement
    
    def obtain_positions_current_player(self):
        for square in self.squares:
            position = {
                "col": square.pos,
                "positions": square.get_pos_pieces(self.current_player)
            }
            self.postions_current_player.append(position)

    def move_piece(self, movement):
        #Remove piece from where it will be move
        square_index = movement['col_origin']
        square = self.squares[square_index]
        square.remove_piece(self.current_player, movement['row_origin'])

        #Add piece to the new square
        square_index = movement['col_arrival']
        square = self.squares[square_index]
        square.add_piece(self.current_player, movement['row_arrival'])


    def get_heuristic(self):
        return self.get_AI_score() - self.get_human_score()
        
    #The AI is represented as 2 -> the black pieces
    def get_AI_score(self):
        score_AI = 0
        for square_index in range(5):
            score_AI += self.squares[square_index].get_score('2')
            print("Score de la IA: ", score_AI)
        
        return score_AI
    
    def get_human_score(self):
        score_human = 0
        for square_index in range(4, len(self.squares)):
            score_human += self.squares[square_index].get_score('1')
        
        return score_human

