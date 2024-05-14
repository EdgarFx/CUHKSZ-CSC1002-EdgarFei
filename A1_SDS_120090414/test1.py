import random


def findZero(g_puzzle):    # find the position of 0 in the list
    for r in range(0, g_n):
        for c in range(0, g_n):
            if g_puzzle[r][c] == 0:
                return[r, c]


def generatePuzzle(g_puzzle):     # to generate the puzzle
    global g_puzzleInOrder
    g_puzzleInOrder = [i for i in range(0, g_n**2)]
    random.shuffle(g_puzzleInOrder)
    # g_puzzleInOrder: a list contain random numbers from 0 to g_num
    for i in range(0, len(g_puzzleInOrder), g_n):
        row_i = g_puzzleInOrder[i:i+g_n]
        g_puzzle.append(row_i)    # row_i: small lists, each have n elements


def printSquare(g_puzzle):             # print a nested list in square
    for r in range(0, g_n):       # there're n lines in total
        c = 0
        while c < g_n:             # each row contains n numbers
            if g_puzzle[r][c] == 0:
                print(" ", end="\t")
            else:
                print(g_puzzle[r][c], end="\t")
            c += 1
            if c == g_n:
                print("\n")


def checkSolvability(g_puzzle):   # check solvability
    s = 0   # s: the number of inversions(not sure about its English name)
    for i in range(0, g_num+1):
        for j in range(i, g_num+1):
            if g_puzzleInOrder[i] > g_puzzleInOrder[j] and g_puzzleInOrder[i] != 0 and g_puzzleInOrder[j] != 0:
                s += 1
    if g_n == 3 and s % 2 == 0:
        return True
    elif g_n == 4 and s % 2 == 0 and (3-findZero(g_puzzle)[0]) % 2 == 0:
        return True
    elif g_n == 4 and s % 2 != 0 and (3-findZero(g_puzzle)[0]) % 2 != 0:
        return True
    else:
        return False


def moveUp(g_puzzle):       # move up
    try:
        g_puzzle[g_zero[0]][g_zero[1]] = g_puzzle[g_zero[0]+1][g_zero[1]]
        g_puzzle[g_zero[0]+1][g_zero[1]] = 0
    except IndexError:
        print("out or range! please enter again")


def moveDown(g_puzzle):        # move down
    if g_zero[0] > 0:
        g_puzzle[g_zero[0]][g_zero[1]] = g_puzzle[g_zero[0]-1][g_zero[1]]
        g_puzzle[g_zero[0]-1][g_zero[1]] = 0
    else:
        print("out or range! please enter again")


def moveLeft(g_puzzle):         # move left
    try:
        g_puzzle[g_zero[0]][g_zero[1]] = g_puzzle[g_zero[0]][g_zero[1]+1]
        g_puzzle[g_zero[0]][g_zero[1]+1] = 0
    except IndexError:
        print("out or range! please enter again")


def moveRight(g_puzzle):          # move right
    if g_zero[1] > 0:
        g_puzzle[g_zero[0]][g_zero[1]] = g_puzzle[g_zero[0]][g_zero[1]-1]
        g_puzzle[g_zero[0]][g_zero[1]-1] = 0
    else:
        print("out or range! please enter again")


def testVictory(g_puzzle):      # compare g_puzzle with the answer
    if g_n == 4 and g_puzzle == [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]:
        return True
    elif g_n == 3 and g_puzzle == [[1, 2, 3], [4, 5, 6], [7, 8, 0]]:
        return True
    else:
        return False


print("""welcome to Yifan's sliding puzzle program!)
You will choose either the 8 or 15-puzzle to play with!
And you move the tiles with the keyboard using any 4 LETTERS you like""")

while 1 > 0:    # loop until the user stop it
    try:
        g_num = int(input("choose 8-puzzle(enter 8) or 15-puzzle(enter 15) here:"))
        # num:the type of puzzle
        g_n = int((g_num+1)**0.5)
        # n: a variable for the convenience of calculation, n^2 = num-1
        if g_num != 8 and g_num != 15:
            print("please choose 8 or 15!")
            continue
    except ValueError:
        print("sorry, please enter a number! (8 or 15) ")
        continue

    while 1 > 0:    # loop until win
        g_up = str(input("enter a letter to define up here:"))
        g_down = str(input("enter a letter to define down here:"))
        g_left = str(input("enter a letter to define left here:"))
        g_right = str(input("enter a letter to define right here:"))
        if len(g_up) > 1 or len(g_down) > 1 or len(g_left) > 1 or len(g_right) > 1:
            print("please enter only 1 letter for one direction!")
            continue
        # up: a letter the user defined which means move up
        # down: a letter the user defined which means move down
        # left: a letter the user defined which means move left
        # right: a letter the user defined which means move right

        if g_up != g_down and g_up != g_left and g_up != g_right and g_down != g_left and g_down != g_right and g_left != g_right:
            break
        else:
            print("please input different letters!")
            # make sure these 4 letters are different

    while 1 > 0:
        g_puzzle = []     # puzzle: a list which is the main body of the puzzle
        generatePuzzle(g_puzzle)
        if checkSolvability(g_puzzle) is True:
            break
        else:
            continue

    g_times = 0   # the times of move
    while 1 != 0:
        printSquare(g_puzzle)

        g_zero = findZero(g_puzzle)
        print("input sliding direction:", end="")
        if g_zero[0] < g_n-1:       # a Hint of where you can move
            print("(up->", g_up, " ", end="")
        if g_zero[0] > 0:
            print("down->", g_down, " ", end="")
        if g_zero[1] < g_n-1:
            print("left->", g_left, " ", end="")
        if g_zero[1] > 0:
            print("right->", g_right, "", end="")

        g_choice = str(input("):"))    # the player's choice of where to move
        if g_choice == g_up:
            moveUp(g_puzzle)
        elif g_choice == g_down:
            moveDown(g_puzzle)
        elif g_choice == g_left:
            moveLeft(g_puzzle)
        elif g_choice == g_right:
            moveRight(g_puzzle)
        else:
            print("invalid input! please enter again!")
        g_times += 1

        if testVictory(g_puzzle) is True:
            break

    printSquare(g_puzzle)
    print("You win!!!!!!It takes", g_times, "steps in total")
    g_tryAgain = str(input("if you want to try again, enter anything you like, else, enter 0:"))
    if g_tryAgain == "0":    # if player don't play again, stop looping
        break
