from Model.Game import Game

def minimax(init_state, player, current_type_movement, max_depth, current_depth):

    gameBoard = Game(init_state,player, current_type_movement)

    if current_type_movement == '1':
        current_type_movement = '2'
    else:
        current_type_movement = '1'

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
            player == '2'
        else:
            player == '1'
        
        movements = gameBoard.get_possible_movements()

        for movement in movements:
            gameBoard.move_piece(movement)
            new_state = gameBoard.obtain_state_matrix()

            actual_score, _ = minimax(new_state, player, current_type_movement, max_depth, current_depth + 1)

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



    