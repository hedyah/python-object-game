
import gameboard
import player 


played = [
    player.Player(3,2)
]
board = [
    gameboard.GameBoard
]

printBoard = gameboard.GameBoard.printBoard
checkWin = gameboard.GameBoard.checkWin
rowPosition = player.Player.moveLeft
columnPosition = player.Player.moveUp


print("Welcome to the game!")
print("Instructions: ")
print("To move up: w")
print("To move down: s")
print("To move left: a")
print("To move right: d")

print("Try to get to the end! Good Luck!")
print("-----------------------------")

# TODO
# Create a new GameBoard called board
# Create a new Player called played starting at position 3,2

while True:
    board(printBoard(player.rowPosition, player.columnPosition))
    selection = input("Make a move: ")
    # TODO
    # Move the player through the board
    # Check if the player has won, if so print a message and break the loop!
    
    
    if selection == 'w' :
        print(player.Player.moveUp)
    elif selection == 's':
        print(player.Player.moveDown)
    elif selection == 'a':
        print(player.Player.moveLeft)
    elif selection == 'd':
        print(player.Player.moveRight)
    
    player_win = gameboard.GameBoard.checkMove
    
    if player_win != (gameboard.GameBoard.checkWin):
        print("you lost!")
        break
    elif player_win == (gameboard.GameBoard.checkWin):
        print("you won the game !!")
    
    player_win = input("play again? (y/n): ")
    if player_win == 'n':
        break
