# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Names: 	Emily Murphy
# 	 		Ryan Oakes
# 	 		Kelsey Wright
#			Mason Fields
# Section:		102-522
# Assignment:	Lab 7
# Date:		10/10/2018

Row1 = ["R", "N", "B", "Q", "K", "B", "N", "R"]
Row2 = ["P", "P", "P", "P", "P", "P", "P", "P"]
Row3 = [".", ".", ".", ".", ".", ".", ".", "."]
Row4 = [".", ".", ".", ".", ".", ".", ".", "."]
Row5 = [".", ".", ".", ".", ".", ".", ".", "."]
Row6 = [".", ".", ".", ".", ".", ".", ".", "."]
Row7 = ["p", "p", "p", "p", "p", "p", "p", "p"]
Row8 = ["r", "n", "b", "q", "k", "b", "n", "r"]

chessBoard = [Row1, Row2, Row3, Row4, Row5, Row6, Row7, Row8]  # creating a chessboard variable to call later

stopped = False  # always will have at least one move
while not stopped:  # going for an unknown number of moves
    for row in chessBoard:  # loops through each row of the chess board
        for item in row:  # loops through each square of the row
            print(item, end="")  # prints whatever is in the square without going to the next line
        print()  # new line created
    # asks user for the starting position of the piece
    startRow = int(input("Enter the row (1-8 left to right) of the piece you would like to move :"))
    startRow -= 1  # usable value
    # asks user for the starting position of the piece
    startCol = int(input("Enter the column (1-8 top to bottom) of the piece you would like to move: "))
    startCol -= 1  # usable value
    # asks user for the starting position of the piece
    finishRow = int(input("Enter the row (1-8 left to right) you would like to move the piece to: "))
    finishRow -= 1  # usable value
    # asks user for the starting position of the piece
    finishCol = int(input("Enter the column (1-8 top to bottom) you would like to move the piece to: "))
    finishCol -= 1  # usable value
    # checks if the numbers are usable in the lists they exist in
    if startRow < 0 or startCol < 0 or finishRow < 0 or finishCol < 0 or startRow > 7 or startCol > 7 or finishRow > 7 or finishCol > 7:
        print("You did not give a proper value")  # error statement
        stopped = True  # stops the loop from going
    elif chessBoard[startRow][startCol] == "R":  # user has selected a square with the Rook
        chessBoard[startRow][startCol] = "."  # nothing will exist where the Rook was
        chessBoard[finishRow][finishCol] = "R"  # user is moving the Rook to this square
    elif chessBoard[startRow][startCol] == "N":  # user has selected a square with the Knight
        chessBoard[startRow][startCol] = "."  # nothing will exist where the Knight was
        chessBoard[finishRow][finishCol] = "N"  # user is moving the Knight to this square
    elif chessBoard[startRow][startCol] == "B":  # user has selected a square with the Bishop
        chessBoard[startRow][startCol] = "."  # nothing will exist where the Bishop was
        chessBoard[finishRow][finishCol] = "B"  # user is moving the Bishop to this square
    elif chessBoard[startRow][startCol] == "Q":  # user has selected a square with the Queen
        chessBoard[startRow][startCol] = "."  # nothing will exist where the Queen was
        chessBoard[finishRow][finishCol] = "Q"  # user is moving the Queen to this square
    elif chessBoard[startRow][startCol] == "K":  # user has selected a square with the King
        chessBoard[startRow][startCol] = "."  # nothing will exist where the King was
        chessBoard[finishRow][finishCol] = "K"  # user is moving the King to this square
    elif chessBoard[startRow][startCol] == "P":  # user has selected a square with the Pawn
        chessBoard[startRow][startCol] = "."  # nothing will exist where the Pawn was
        chessBoard[finishRow][finishCol] = "P"  # user is moving the Pawn to this square
    elif chessBoard[startRow][startCol] == "r":  # user has selected a square with the rook
        chessBoard[startRow][startCol] = "."  # nothing will exist where the rook was
        chessBoard[finishRow][finishCol] = "r"  # user is moving the rook to this square
    elif chessBoard[startRow][startCol] == "n":  # user has selected a square with the knight
        chessBoard[startRow][startCol] = "."  # nothing will exist where the knight was
        chessBoard[finishRow][finishCol] = "n"  # user is moving the knight to this square
    elif chessBoard[startRow][startCol] == "b":  # user has selected a square with the bishop
        chessBoard[startRow][startCol] = "."  # nothing will exist where the bishop was
        chessBoard[finishRow][finishCol] = "b"  # user is moving the bishop to this square
    elif chessBoard[startRow][startCol] == "q":  # user has selected a square with the queen
        chessBoard[startRow][startCol] = "."  # nothing will exist where the queen was
        chessBoard[finishRow][finishCol] = "q"  # user is moving the queen to this square
    elif chessBoard[startRow][startCol] == "k":  # user has selected a square with the king
        chessBoard[startRow][startCol] = "."  # nothing will exist where the king was
        chessBoard[finishRow][finishCol] = "k"  # user is moving the king to this square
    elif chessBoard[startRow][startCol] == "p":  # user has selected a square with the pawn
        chessBoard[startRow][startCol] = "."  # nothing will exist where the pawn was
        chessBoard[finishRow][finishCol] = "p"  # user is moving the pawn to this square
    else:  # user tried to move an empty square
        stopped = True  # stop the game
        print("The move you made was invalid")  # error message

