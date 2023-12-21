from Model.Game import Game

def minimax(init_state, player, current_type_movement, turn_max_movements, max_depth, current_depth):

    gameBoard = Game(init_state,player, current_type_movement, turn_max_movements)
    for square in gameBoard.squares:
         print(square.__str__())
    if (gameBoard.check_final_state() or current_depth == max_depth):
        return {
            'best_puntuation': gameBoard.get_heuristic(),
            'best_move': None
        }
    
    else:
        best_move = None
        best_score = -float('inf')
        if (player == '1'):
            best_score = float('inf')
        
        movements = gameBoard.get_possible_movements()

        for movement in movements:

            #To check second movement for current player
            if (current_type_movement == 1 and movement['movements'] == 0):
                player = "2" if player == "1" else "1"
            
            else: 
                if current_type_movement == 1:
                    current_type_movement = 2
                else:
                    current_type_movement = 1
                    player = "2" if player == "1" else "1"


            gameBoard.move_piece(movement)
            new_state = gameBoard.obtain_state_matrix()
            
            result = minimax(new_state, player, current_type_movement, movement['movements'], max_depth, current_depth + 1)
            actual_score = result['best_puntuation']
            if(player == "1"):
                if (actual_score > best_score):
                    best_score = actual_score
                    best_move = movement

            else:
                if (actual_score < best_score):
                    best_score = actual_score
                    best_move = movement
                    
            gameBoard.undo_movement()

    return best_score, best_move



    