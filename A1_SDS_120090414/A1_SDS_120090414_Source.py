# CSC1002 Assignment_1
# author : FX

import random

state = 1 # Game status flag, 0 means a game is over, 1 means the game is in progress, 2 means the input is illegal
step = 0 # Record the number of steps in the game

# use enumeration to find the number of Count Inversions
def InversionPair(a):
    global n, N
    num = 0
    for i in range(N):
        if a[i]!=0:
            for j in range(i+1,N):
                if a[j]!=0:
                    if a[i] > a[j]:
                        num += 1
    return num

# check if there is a solution
def is_solvable(a):
    for i in range(N):
        if a[i] == 0:
            zero_row = i//n + 1
            break
    F = InversionPair(a)
    # convert the number of Count Inversions into state quantities
    if n%2==1:
        F%=2
    else:
        F=(F%2)^((n-zero_row)%2)
    if F==0:
        return True
    else:
        return False
    
# Implement new game settings
def new_game():
    global a
    global n, N
    global L, R, U, D
    global zero_index
    while True:
        n = input('\nEnter the desired dimension of the puzzle (3~10) > ')
        try:
            n = int(n)
            if n<3 or n>10:
                print('\nPlease select the dimension between 3 and 10.')
                continue
            else:
                break
        except:
            print('\nPlease enter a number between 3 and 10.')
            continue
    N = n**2
    a = list(range(N))
    while True:
        random.shuffle(a)
        if is_solvable(a):
            break
    for i in range(N):
        if a[i]==0:
            zero_index = i
    # choose the direction keys
    while True:
        directions = input('Enter the four letters used for left, right, up and down directions like a d w s > ').split()
        if len(directions)==4 and len(set(directions))==4:
            L = directions[0].lower()
            R = directions[1].lower()
            U = directions[2].lower()
            D = directions[3].lower()
            if L.isalpha() and R.isalpha() and U.isalpha() and D.isalpha() and len(L)==len(R)==len(U)==len(D)==1:
                break
            else:
                print('\nPlease input four different letters!')
                continue
        else:
            print('\nPlease input four different letters!')
            continue
    
# Determine whether the game is successfully completed
def is_win():
    is_win = True
    for i in range(N-1):
        if a[i] != i+1:
            is_win = False
    return is_win

# Implement move algorithms
def move():
    global state
    global zero_index
    global step
    if zero_index == 0: #Upper left corner
        next_step = input('Enter your move (left-%s, up-%s)>'%(L, U)).lower()
    elif zero_index == n-1: #Upper right corner
        next_step = input('Enter your move (right-%s, up-%s)>'%(R, U)).lower()
    elif zero_index == N-1: #Lower right corner
        next_step = input('Enter your move (right-%s, down-%s)>'%(R, D)).lower()
    elif zero_index == N-n: #Lower left corner
        next_step = input('Enter your move (left-%s, down-%s)>'%(L, D)).lower()
    elif zero_index < n: #The first row
        next_step = input('Enter your move (left-%s, right-%s, up-%s)>'%(L, R, U)).lower()
    elif zero_index >= N-n: #The nth row
        next_step = input('Enter your move (left-%s, right-%s, down-%s)>'%(L, R, D)).lower()
    elif (zero_index+1) % n == 1: #The first column
        next_step = input('Enter your move (left-%s, up-%s, down-%s)>'%(L, U, D)).lower()
    elif (zero_index+1) % n == 0: #The nth column
        next_step = input('Enter your move (right-%s, up-%s, down-%s)>'%(R, U, D)).lower()
    else:
        next_step = input('Enter your move (left-%s, right-%s, up-%s, down-%s)>'%(L, R, U, D)).lower()

    # check if the input is valid
    if next_step == U:
        if zero_index >= N-n:
            print('\nYou cannot go UP!')
            state = 2
            return
        a[zero_index+n], a[zero_index] = a[zero_index], a[zero_index+n]
        zero_index += n
    elif next_step == R:
        if (zero_index+1) % n == 1:
            print('\nYou cannot go RIGHT!')
            state = 2
            return
        a[zero_index-1], a[zero_index] = a[zero_index], a[zero_index-1]
        zero_index -=1
    elif next_step == D:
        if zero_index < n:
            print('\nYou cannot go DOWN!')
            state = 2
            return
        a[zero_index-n], a[zero_index] = a[zero_index], a[zero_index-n]
        zero_index -= n
    elif next_step == L:
        if (zero_index+1) % n == 0:
            print('\nYou cannot go LEFT!')
            state = 2
            return
        a[zero_index+1], a[zero_index] = a[zero_index], a[zero_index+1]
        zero_index += 1
    else:
        print('\nPlease input a correct letter!')
        state = 2
        return
    
    if is_win():
        table()
        state = 0
        return

# show game interface
def table():
    global step
    length = len(str(N-1)) # Record the length of the largest number to facilitate formatted output
    print()
    for i in range(N):
        length_now = len(str(a[i]))
        if i == zero_index:
            print(' '*length, end=' ')
        else:
            print(a[i], ' '*(length-length_now), sep='', end=' ')
        if (i+1) % n == 0:
            print()
    print('You have moved %d steps'%step)
    step += 1

# main function
def main():
    global state
    global step
    print('''\nWelcome to Edgar's puzzle game!
You can choose the dimension of the puzzle between 3 and 10!
And you can move the digits with the keyboard using any 4 letters you like!''')
    while state == 1:
        if step == 0:
            new_game()
        else:
            move()
        
        while state == 2:
            state = 1
            move()

        if state == 0:
            print('\nCongratulations! You solved the puzzle in %d moves!'%(step-1))
            option = input("\nEnter 'n' to start a new game or enter 'q' to end the game >")
            while option != 'n' and option != 'N' and option !='q' and option !='Q':
                print('\nPlease input a valid letter.')
                option = input("Enter 'n' to start a new game or enter 'q' to end the game >")
            if option == 'n' or option == 'N':
                state = 1
                step = 0
                continue
            elif option == 'q' or option == 'Q':
                print('\nSee you!')
                break

        table()


main()