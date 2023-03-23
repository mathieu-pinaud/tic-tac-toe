def my_refactor(board):
    r = []
    for i in board:
        if i == 2:
            r.append(-1)
        else:
            r.append(i)
    return(r)

def wining_condition(board):
    l = [0, 0, 0, 0, 0, 0, 0, 0]
    r_board = my_refactor(board)
    test_egalité = 0
    l[0] = r_board[0] + r_board[1] + r_board[2]
    l[1] = r_board[3] + r_board[4] + r_board[5]
    l[2] = r_board[6] + r_board[7] + r_board[8]
    l[3] = r_board[0] + r_board[3] + r_board[6]
    l[4] = r_board[1] + r_board[4] + r_board[7]
    l[5] = r_board[2] + r_board[5] + r_board[8]
    l[6] = r_board[0] + r_board[4] + r_board[8]
    l[7] = r_board[2] + r_board[4] + r_board[6]

    for i in l:
        if i == 3:
            return(0)
        elif i == -3:
            return(1)
    for j in r_board:
        if j != 0:
            test_egalité += 1
    if test_egalité == 9:
        return(2)
    return(-1)

def ia(board, signe):
    if (signe == 'X'):
        tmp = 1
        nw_sign = 'O'
        best_prob = 10
    elif(signe == 'O'):
        tmp = 2
        nw_sign = 'X'
        best_prob = -10
   
    for i in range(len(board)):
        if (board[i] == 0):
            board[i] = tmp
            prob = my_minimax(board, nw_sign)
            board[i] = 0
            if (signe == 'X' and prob <  best_prob):
                best_i = i
                best_prob = prob
            elif (signe == 'O' and prob > best_prob):
                best_i = i
                best_prob = prob
    return(best_i)

def my_minimax(board, signe):

    v = wining_condition(board)
    if (v == 0):
        return(-1)
    elif (v == 1):
        return(1)
    elif (v == 2):
        return(0) 
    
    if (signe == 'X'):
        tmp = 1
        nw_sign = 'O'
        best_prob = 10
    elif(signe == 'O'):
        tmp = 2
        nw_sign = 'X'
        best_prob = -10
   
    for i in range(len(board)):
        if (board[i] == 0):
            board[i] = tmp
            prob = my_minimax(board, nw_sign)
            board[i] = 0
            if (signe == 'X' and prob <  best_prob):
                best_prob = prob
            elif (signe == 'O' and prob > best_prob):
                best_prob = prob
    return(best_prob)