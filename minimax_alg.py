def checkWinner(game_board, i, turn):
    #horizontal wins 
    if game_board[i] == game_board[i + 1] and game_board[i] == game_board[i + 2] and game_board[i] == turn:
        return True
    elif game_board[i + 3] == game_board[i + 4] and  game_board[i + 3] == game_board[i + 5]and game_board[i + 3] == turn:
        return True 
    elif game_board[i + 6] == game_board[i + 7] and game_board[i + 6] == game_board[i + 8] and game_board[i + 6] == turn:
        return True 
    #vertical wins
    elif game_board[i] == game_board[i + 3] and game_board[i] == game_board[i + 6] and game_board[i] == turn:
        return True 
    elif game_board[i + 1] == game_board[i + 4] and game_board[i + 1] == game_board[i + 7] and game_board[i + 1] == turn:
        return True 
    elif game_board[i + 2] == game_board[i + 5] and game_board[i + 2] == game_board[i + 8] and game_board[i + 2] == turn:
        return True 
    #diagonal wins 
    elif game_board[i] == game_board[i + 4] and game_board[i] == game_board[i + 8] and game_board[i] == turn:
        return True 
    elif game_board[i + 2] == game_board[i + 4] and game_board[i + 2] == game_board[i + 6] and game_board[i + 2] == turn:
        return True 
    else:
        return False 


def tie(game_board):
    for i in range(len(game_board)):
        if game_board[i] != "X" and game_board[i] != "O":
            return False
    return True 




def minimax(board, isMaximizing, alpha, beta):
    #if board state is at terminal condition/end state, then just return the score
    if checkWinner(board, 0, "X"):
        return 1
    elif checkWinner(board, 0, "O"):
        return -1
    elif tie(board):
        return 0
    #if it is not end state, then check all the possible next moves 
    if isMaximizing:
        bestScore = -10
        for i in range(len(board)):
            #if the spot is available
            if board[i] != 'X'and board[i] != 'O':
                board[i] = 'X'
                score = minimax(board, False, alpha, beta)
                board[i] = str(i + 1)[0]
                bestScore = max(score, bestScore)
                alpha = max(alpha, score)
                #we are tyring to maximize and so if we happen to find a value that is less than what we have, we don't need to go any further 
                if beta <= alpha:
                    break
        #finding the best score for all the possible next turns by the ai player 
        return bestScore 
    else:
        #now the player needs to find the best position for it, which is the lowest score 
        bestScore = 10
        for i in range(len(board)):
            if board[i] != 'X' and board[i] != 'O':
                board[i] = 'O'
                score = minimax(board,True, alpha, beta)
                board[i] = str(i + 1)[0]
                bestScore = min(bestScore, score)
                beta = min(beta, score)
                #this means that white had a better option avaiable earlier on in the tree
                if beta <= alpha:
                    break
        return bestScore 






