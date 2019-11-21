# Description: This program simulates a two-player tic tac toe game.

import random
# Given a tic, tac, toe board determine if there is a winner
# Function inputs:
#     board_list: an array of 9 strings representing the tic tac toe board
#     move_counter: an integer representing the number of moves that have been made
# Returns a string:
#     'x' if x won
#     'o' if o won
#     'n' if no one wins
#     's' if there is a stalemate
def checkForWinner(board_list, move_counter):
    j = 0
    for i in range(0, 9, 3):
        # Check for 3 in a row
        if board_list[i] == board_list[i+1] == board_list[i+2]:
            return board_list[i]

        # Check for 3 in a column
        elif board_list[j] == board_list[j+3] == board_list[j+6]:
            return board_list[j]

        # Check the diagonal from the top left to the bottom right
        elif board_list[0] == board_list[4] == board_list[8]:
            return board_list[0]

        # Check the diagonal from top right to bottom left
        elif board_list[2] == board_list[4] == board_list[6]:
            return board_list[2]
        j += 1

    # If winner was not found and board is completely filled up, return stalemate
    if move_counter > 8:
        return "s"

    # Otherwise, 3 in a row anywhere on the board
    return "n"


# Print out the tic tac toe board
# Input: list representing the tic tac toe board
# Return value: none
def printBoard(board_list):
    print()
    counter = 0
    for i in range(5):
        if i % 2 == 0:
            for j in range(5):
                if j % 2 == 0:
                    print(board_list[counter], end=" ")
                    counter += 1
                else:
                    print("|", end=" ")
        else:
            print("\n---------")
    return


def isValidMove(board_list, spot): #Checks to see if player input is valid.
    if (spot < 0) or (spot > 8):
        return False
    else:
        return board_list[spot] not in ['o', 'x']

def updateBoard(board_list, spot, player_letter): #Replaces player choice of spot with 'x' or 'o'
    pos = board_list.index(str(spot))
    board_list[pos] = player_letter
    return board_list

def playGame():
    board_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
    print("Welcome to Tic Tac Toe!")
    mode = str(input("Please select a game mode:\n1) Player vs. Player\n2) Player vs. Computer\n>"))
    if (mode != "1") and (mode != "2"):
        print("Invalid input, please try again.")
        mode = input("Please select a game mode:\n1) Player vs. Player\n2) Player vs. Computer\n>")

    count = 0

    playerLet = ["x", "o"]
    chooseLet = input("Please select your letter:\n'x' plays first by default\n'o' plays second\n>").lower()
    if chooseLet not in playerLet:
        print("Invalid input, please try again.")
        chooseLet = input("Please select your letter:\n'x' plays first by default\n'o' plays second\n>").lower()
    while checkForWinner(board_list, count) == "n":
        let = count % 2
        player = playerLet[let]
        printBoard(board_list)
        if (mode == "2") and (chooseLet != player):
            spot = random.choice(range(9))
            while not isValidMove(board_list, spot):
                spot = random.choice(range(9))
            print("\nComputer " + player + ", pick a spot: " + str(spot))
        else:
            spot = int(input("\nPlayer " + player + ", pick a spot: "))
            while not isValidMove(board_list, spot):
                print("Invalid move, please try again.")
                spot = input("PLayer " + player + ", pick a spot: ")
        updateBoard(board_list, spot, player)
        count += 1
    printBoard(board_list)
    print("Game over!")
    winner = checkForWinner(board_list, count)
    if winner == "s":
        print("Stalemate reached.")
    else:
        if mode == "2" and winner != chooseLet:
            print("Computer is the winner!")
        else:
            print("Player " + chooseLet + " is the winner!")

def main():
    playGame()
    while True: #Allows player to decide whether to play another round.
        another = input("Would you like to play another round? (y/n): ").lower()
        if another == "y":
            playGame()
        else:
            print("Goodbye!")
            break
main()