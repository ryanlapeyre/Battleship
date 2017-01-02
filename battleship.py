from random import randint


def makeBoard(board , boardSize): 
    for x in range(boardSize):
        board.append(["O"] * boardSize)
    return
def print_board(board):
    for row in board:
        print " ".join(row)
    return
def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board) - 1)
    

def main():
    boardSize = 5
    maxTurns = 5
    board = []
    makeBoard(board , boardSize)
    print "Let's play Battleship!"
    turn = int(1) 
    print "Turn" , turn
    print_board(board)
    ship_row = random_row(board)
    ship_col = random_col(board)
    counter = int(0)
    while (turn !=  maxTurns):
        guess_row = int(raw_input("Guess Row:"))
        guess_col = int(raw_input("Guess Col:"))
        if (guess_row == ship_row and guess_col == ship_col):
            print "Congratulations! You sunk my battleship!"
            return
            break
        if (guess_row < 0 or guess_row >= boardSize or guess_col < 0 or guess_col >= boardSize):
            print "Oops, that's not even in the ocean."

        elif(board[guess_col][guess_row] == "X"):
            print "You guessed that one already."

        else:
            print "You missed my battleship!"
            board[guess_row][guess_col] = "X"
        
        turn += 1
        if(turn != maxTurns):
            print "Turn" , turn
            print_board(board)

    if (turn == maxTurns):
        print "Game Over"
        return




main()
