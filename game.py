# Tic Tac Toe game

board = [' ' for x in range(10)]

def insertMove(letter, pos):
    global board
    board[pos] = letter

def isSpaceFree(pos):
    return board[pos] == ' '

def isWinner(bo, le):
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or # across the top
    (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle
    (bo[1] == le and bo[2] == le and bo[3] == le) or # across the bottom
    (bo[7] == le and bo[4] == le and bo[1] == le) or # down the left side
    (bo[8] == le and bo[5] == le and bo[2] == le) or # down the middle
    (bo[9] == le and bo[6] == le and bo[3] == le) or # down the right side
    (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal
    (bo[9] == le and bo[5] == le and bo[1] == le)) # diagonal

def playerMove():
    run = True
    while run:
        move = input('Please select a position for next move (1-9): ')
        try:
            move = int(move)
            if move > 0 and move < 10:
                if isSpaceFree(move):
                    run = False
                    insertMove('X', move)
                else:
                    print('This position is already occupied')
            else:
                print('Please type a number withing the range')
        except:
            print('Please type a number')
            

def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]

def compMove():
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    # Check for a winning move or block winning move
    for let in ['O', 'X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if isWinner(boardCopy, let):
                move = i
                return move

    # Take a corner
    cornersOpen = []
    for i in possibleMoves:
        if i in [2, 4, 6, 8]:
            cornersOpen.append(i)
    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    # Take the center
    if 5 in possibleMoves:
        move = 5
        return move

    # Take an edge
    edgesOpen = []
    for i in possibleMoves:
        if i in [2, 4, 6, 8]:
            edgesOpen.append(i)

    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
        return move

def isBoardFull():
    if board.count(' ') > 1:
        return False
    else:
        return True

def printBoard():
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')

def main():
    # Main game loop
    print('Welcome to Tic Tac Toe game. The borad has postions 1-9 startinga t top left')

    printBoard()

    while not(isBoardFull()):
        if not(isWinner(board, 'O')):
            playerMove()
            printBoard()
        else:
            print('O wins this game')
            break

        if not(isWinner(board, 'X')):
            move = compMove()
            if move == 0:
                print('Game is a tie!')
            else:
                insertMove('O', move)
                printBoard()
        else:
            print('X wins, good job')
            break

    if isBoardFull():
        print('Game is a time! No more spaces left to move.')

main()

while True:
    answer = input('Do you want to play again? (Y/N)')
    if answer == 'y' or answer == 'Y':
        board = [' ' for x in range(10)]
        print('-----------')
        main()
    else:
        break