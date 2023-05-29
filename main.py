from random import choice
from math import inf

board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

def printBoard(board):
    chars = {1: 'X', -1: 'O', 0: ' '}
    for row in board:
        for cell in row:
            ch = chars[cell]
            print(f'| {ch} |', end='')
        print('\n' + '---------------')
    print('===============')

def clearBoard(board):
    for row in board:
        for i in range(len(row)):
            row[i] = 0

def hasPlayerWon(board, player):
    winning_conditions = [[board[0][0], board[0][1], board[0][2]],
                          [board[1][0], board[1][1], board[1][2]],
                          [board[2][0], board[2][1], board[2][2]],
                          [board[0][0], board[1][0], board[2][0]],
                          [board[0][1], board[1][1], board[2][1]],
                          [board[0][2], board[1][2], board[2][2]],
                          [board[0][0], board[1][1], board[2][2]],
                          [board[0][2], board[1][1], board[2][0]]]

    return [player, player, player] in winning_conditions

def isGameWon(board):
    return hasPlayerWon(board, 1) or hasPlayerWon(board, -1)

def printResult(board):
    if hasPlayerWon(board, 1):
        print('X has won!')

    elif hasPlayerWon(board, -1):
        print('O has won!')

    else:
        print('It\'s a draw!')

def getBlanks(board):
    blank_cells = []
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == 0:
                blank_cells.append([row, col])

    return blank_cells

def isBoardFull(board):
    return len(getBlanks(board)) == 0

def makeMove(board, x, y, player):
    board[x][y] = player

def playerMove(board):
    moves = {1: [0, 0], 2: [0, 1], 3: [0, 2],
             4: [1, 0], 5: [1, 1], 6: [1, 2],
             7: [2, 0], 8: [2, 1], 9: [2, 2]}

    while True:
        try:
            move = int(input('Enter a number between 1-9: '))
            if move < 1 or move > 9:
                print('Invalid move! Try again!')
            elif moves[move] not in getBlanks(board):
                print('Invalid move! Try again!')
            else:
                x, y = moves[move]
                makeMove(board, x, y, 1)
                printBoard(board)
                break
        except (KeyError, ValueError):
            print('Enter a number!')

def getScore(board):
    if hasPlayerWon(board, 1):
        return 10

    elif hasPlayerWon(board, -1):
        return -10

    else:
        return 0

def alphaBetaMinimax(board, depth, alpha, beta, player):
    row = -1
    col = -1

    if depth == 0 or isGameWon(board):
        return [row, col, getScore(board)]

    else:
        for cell in getBlanks(board):
            x, y = cell
            makeMove(board, x, y, player)
            score = alphaBetaMinimax(board, depth - 1, alpha, beta, -player)

            if player == 1:
                if score[2] > alpha:
                    alpha = score[2]
                    row, col = x, y

            else:
                if score[2] < beta:
                    beta = score[2]
                    row, col = x, y

            makeMove(board, x, y, 0)

            if alpha >= beta:
                break

        if player == 1:
            return [row, col, alpha]

        else:
            return [row, col, beta]

def computerMove(board, player):
    if len(getBlanks(board)) == 9:
        x = choice([0, 1, 2])
        y = choice([0, 1, 2])
        makeMove(board, x, y, player)
        printBoard(board)

    else:
        result = alphaBetaMinimax(board, len(getBlanks(board)), -inf, inf, player)
        makeMove(board, result[0], result[1], player)
        printBoard(board)

def playVsComputer():
    while True:
        try:
            order = int(input('Enter to play first (1) or second (2): '))
            if order not in [1, 2]:
                print('Please pick 1 or 2')
            else:
                break
        except (KeyError, ValueError):
            print('Enter a number')

    clearBoard(board)

    if order == 2:
        currentPlayer = -1
    else:
        currentPlayer = 1

    while not (isBoardFull(board) or isGameWon(board)):
        if currentPlayer == 1:
            playerMove(board)
        else:
            computerMove(board, -1)

        currentPlayer *= -1

    printResult(board)

# Driver Code
print("=================================================")
print("TIC-TAC-TOE using MINIMAX with ALPHA-BETA Pruning")
print("=================================================")
playVsComputer()
