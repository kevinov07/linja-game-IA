from Model.Game import Game

def minimax(init_state, player, current_type_movement, max_depth, current_depth):

    gameBoard = Game(init_state,player, current_type_movement)
    if (gameBoard.check_final_state() or current_depth == max_depth):
        return {
            'best_puntuation': gameBoard.get_heuristic(),
            'best_move': None
        }
    
    else:
        best_move = None
        best_score = float('inf')
        if (player == '1'):
            best_score = -float('inf')
        
        movements = gameBoard.get_possible_movements()

        for move in movements:
            pass



    