import random
import sys


def drawBoard(board):
    # this function prints out the board that it was passed. Returns None.

    HLINE = '  +---+---+---+---+---+---+---+---+'
    VLINE = '  |   |   |   |   |   |   |   |   |'

    print ' 1   2   3   4   5   6   7   8'
    print HLINE
    for y in range(8):
        print (VLINE)
        print(y+1)
        for x in range(8):
            print('| %s' % (board[x][y]))
        print '|'
        print VLINE
        print HLINE

def resetBoard(board):
    # blanks out the board it is passed, except for the original starting position.
    for x in range(8):
        for y in range(8):
            board[x][y] = ' '

    # starting pieces:
    board[3][3] = 'X'
    board[3][4] = 'O'
    board[4][3] = 'O'
    board[4][4] = 'X'

def getNewBoard():
    #  Creates a branc new, blank board data structure.
    board = []
    for i in range(8):
        board.append([' '] * 8)

    return board

def isValidMove(board, tile, xstart, ystart):
    # returns False if the player's move on space xstart, ystart is invalid
    # if it is a valid move, returns a list of spaces that would become the player's if they made a move here.

    if board[xstart][ystart] != ' ' or not  isOnBoard(xstart, ystart):
        return False

    board[xstart][ystart] = tile # temporarily set the tile on the baord.

    if tile == 'X':
        otherTile = 'O'
    else:
        otherTile = 'X'

    tilesToFlip = []
    for xdirection, ydirection in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
        x, y = xstart, ystart
        x += xdirection # first step in the direction x
        y += ydirection # first step in the direction y
        if isOnBoard(x, y) and board[x][y] == otherTile:
            # there is a piece belonging to the other player next to our piece
            x += xdirection
            y += ydirection
            if not isOnBoard(x, y):
                continue
            while board[x][y] == otherTile:
                x += xdirection
                y += ydirection
                if not isOnBoard(x, y): # break out of the while loop, then continue in for loop
                    while True:
                        x -= xdirection
                        y -= ydirection
                        if x == xstart and y == ystart:
                            break
                        tilesToFlip.append([x, y])

    board[xstart][ystart] = ' ' # restore the empty space

    if len(tilesToFlip) == 0: # If no tiles were flipped, this is not a valid move
        return False
    return tilesToFlip

def isOnBoard(x, y):
    # returns True if coordinates are located on the board
    return x >= 0 and x <= 7 and y >= 0 and y <= 7

def getBoardWithValidMoves(board, tile):
    # returns a new board with . marking the valid moves the given player can make
    dupeBoard = getBoardCopy(board)

    for x, y in getValidMoves(dupeBOard, tile);
        dupeBoard[x][y] = '.'
    return dupeBoard

def getValidMoves(board, tile):
    # returns a list of [x, y] lists of valid moves for the given player on the given board
    validMoves = []

    for x in range(8):
        for y in range(8):
            if isValidMove(baord, tile, x, y) != False:
                validMoves.append([x, y])

    return validMoves

def getScoreOfBoard(board):
    # determine the score by counting the tiles.
    # returns a dictionary with keys 'X' and 'O'
    xscore = 0
    oscore = 0
    for x in range(8):
        for y in range(8):
            if board[x][y] == 'X':
                xscore += 1
            if board[x][y] == 'O':
                oscore += 1

    return { 'X': xscore, 'O': oscore }

def enterPlayerTile():
    # Let's the player type which tile they want to be
    # returns a list with the player's tile as the first item, and the computer's tile as the second
    tile = ''
    while not (tile == 'X' or tile == 'O'):
        print 'Do you want to be X or O?'
        tile = raw_input().upper()

    # the first element in the tuple is the player's tile, the second is the computer's tile.

    if tile == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

