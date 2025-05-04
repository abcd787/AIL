# Non AI TicTacToe
def createBoard():
    return [[' ' for _ in range(3)] for _ in range(3)]

def displayBoard(board):
    print()
    for row in board:
        print(" | ".join(row))
        print("- " * 5)

def showGuide():
    print("Tic-Tac-Toe Game")
    print("Pick a cell number like this:")
    print("1 | 2 | 3")
    print("4 | 5 | 6")
    print("7 | 8 | 9")

def moveIsValid(board, move):
    row = (move - 1) // 3
    col = (move - 1) % 3
    return board[row][col] == ' '

def placeMove(board, move, symbol):
    row = (move - 1) // 3
    col = (move - 1) % 3
    board[row][col] = symbol

def checkWinner(board):
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return True
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return True
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return True
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return True
    return False

def boardIsFull(board):
    for row in board:
        if ' ' in row:
            return False
    return True

def playGame():
    board = createBoard()
    showGuide()

    current = 'X'
    while True:
        displayBoard(board)
        try:
            move = int(input(f"Player {current}, choose your move (1-9): "))
            if move < 1 or move > 9 or not moveIsValid(board, move):
                print("Invalid move. Try again.")
                continue
        except ValueError:
            print("Please enter a valid number between 1 and 9.")
            continue

        placeMove(board, move, current)

        if checkWinner(board):
            displayBoard(board)
            print(f"Player {current} wins!")
            break

        if boardIsFull(board):
            displayBoard(board)
            print("It's a draw!")
            break

        # Switch player
        current = 'O' if current == 'X' else 'X'

if __name__ == "__main__":
    playGame()
