#CSC_1002 Assignment_1

import random

n=0; N=0
#以序列的形式储存华容道，左移位置-1，上移位置-n
a = []; c = []
flag = 1 #游戏状态标志，0表示一局游戏结束，1表示进行中，2表示操作非法
step = 0
raw = 0; column = 0;
l = 0; b_Position = 0;
U = 'u'; R = 'r'; D = 'd'; L = 'l'
#---------------------------------------------------------
#树状数组求逆序对
def lowbit(x): return x&(-x)

def update(x): 
	while x < N: c[x] += 1; x += lowbit(x)

def query(x): 
	ret = 0 
	while x > 0: ret += c[x]; x -= lowbit(x) 
	return ret
	
def check_if_can_be_solved():#检查是否有解
	global raw, column
	global a, c
	c = [0]*N
	F = 0 #当前华容道的状态量
	for i in range(0,N):
		if a[i] == 0:
			raw = i//n+1; column = i%n
			continue
		update(a[i])
		F += a[i]-query(a[i]) 
	#先求出逆序对数再将逆序对数转换成状态量
	if n%2==1: F%=2
	else: F=(F%2)^( (n-raw)%2 )
	return F
#---------------------------------------------------------

def new_game():
	global a, c
	global n, N
	global l, b_Position
	global U, R, D, L
	n = input('\nSelect the level you want(3~20) :\n')
	while True:
		try:
			n = int(n)
			if n > 20: continue
			if n < 10: break
			S = input('\nThis level could be a little hard!\nSure to start(y/n)?')
			if S == 'y' or S=='Y': break
			elif S == 'n' or S == 'N':
				n = input('\nSelect the level you want(3~20) :\n')
				continue
			while S != 'y' and S != 'Y' and S != 'n' and S !='N':
				S = input('\nSure to start(y/n)?\n')
		except:
			n = input('\nSelect the level you want(3~20) :\n')
	N = n**2
	l = len(str(N-1)) #记录最大数字的长度以方便对齐输出
	a = list(range(0,N))
	c = [0]*(N)
	while True:
		random.shuffle(a)
		if check_if_can_be_solved() == 0: break
	for i in range(0,N):
		if a[i] == 0: b_Position = i 
	#choose the direction keys
	U = input("Please choose a key for UP direction('a'~'z', except 'q') :\n")
	while len(U) == 0 or len(U) > 1 or (ord(U) < 97 or ord(U) > 122 or ord(U) == ord('q')):
		U = input("Please choose a key for UP direction('a'~'z', except 'q') :\n")
	R = input("Please choose a key for RIGHT direction('a'~'z', except 'q') :\n")
	while len(R) == 0 or len(R) > 1 or (ord(R) < 97 or ord(R) > 122 or ord(R) == ord('q')):
		R = input("Please choose a key for RIGHT direction('a'~'z', except 'q') :\n")
	D = input("Please choose a key for DOWN direction('a'~'z', except 'q') :\n")
	while len(D) == 0 or len(D) > 1 or (ord(D) < 97 or ord(D) > 122 or ord(D) == ord('q')):
		D = input("Please choose a key for DOWN direction('a'~'z', except 'q') :\n")
	L = input("Please choose a key for LEFT direction('a'~'z', except 'q') :\n")
	while len(L) == 0 or len(L) > 1 or (ord(L) < 97 or ord(L) > 122 or ord(L) == ord('q')):
		L = input("Please choose a key for LEFT direction('a'~'z', except 'q') :\n")
#---------------------------------------------------------
def win_check():
	global a, N
	if_Win = True
	for i in range(0,N-1):
		if a[i] != i+1: if_Win = False
	return if_Win
	
def move():
	global b_Position, flag
	global a, n, step
	global U, R, D, L
	
	next_Step = U
	if b_Position == 0:#左上角
		next_Step = input('Enter the two letters used for up and left directions > {} {}\nOr enter q to end the game!\n'.format(U,L))
	elif b_Position == n-1:#右上角
		next_Step = input('Enter the two letters used for up and right directions > {} {}\nOr enter q to end the game!\n'.format(U,R))
	elif b_Position == N-1:#右下角
		next_Step = input('Enter the two letters used for right, down directions > {} {}\nOr enter q to end the game!\n'.format(R,D))
	elif b_Position == N-n:#左下角
		next_Step = input('Enter the two letters used for down and left directions > {} {}\nOr enter q to end the game!\n'.format(D,L))
	elif b_Position < n:#第一行
		next_Step = input('Enter the three letters used for up, right and left directions > {} {} {}\nOr enter q to end the game!\n'.format(U,R,L))
	elif b_Position >= N-n:#第n行
		next_Step = input('Enter the three letters used for right, down and left directions > {} {} {}\nOr enter q to end the game!\n'.format(R,D,L))
	elif (b_Position+1) % n == 1:#第一列
		next_Step = input('Enter the three letters used for up, down and left directions > {} {} {}\nOr enter q to end the game!\n'.format(U,D,L))
	elif (b_Position+1) % n == 0:#第n列
		next_Step = input('Enter the three letters used for up, right and down directions > {} {} {}\nOr enter q to end the game!\n'.format(U,R,D))
	else: next_Step = input('Enter the four letters used for up, right, down and left directions > {} {} {} {}\nOr enter q to end the game!\n'.format(U,R,D,L))
	
	#检查操作是否合法或是需要退出
	if next_Step == 'q':
		flag = 0
		return
	elif next_Step == U: 
		if b_Position >= N-n:
			print('\nYou cannot go UP!')
			flag=2
			return
		a[b_Position+n], a[b_Position] = a[b_Position], a[b_Position+n]
		b_Position += n	
	elif next_Step == R: 
		if (b_Position+1) % n ==1:
			print('\nYou cannot go RIGHT!')
			flag=2
			return
		a[b_Position-1], a[b_Position] = a[b_Position], a[b_Position-1]
		b_Position -= 1
	elif next_Step == D: 
		if b_Position < n:
			print('\nYou cannot go DOWN!')
			flag=2
			return
		a[b_Position-n], a[b_Position] = a[b_Position], a[b_Position-n]
		b_Position -= n
	elif next_Step == L: 
		if (b_Position+1) % n ==0:
			print('\nYou cannot go LEFT!')
			flag=2
			return
		a[b_Position+1], a[b_Position] = a[b_Position], a[b_Position+1]
		b_Position += 1
	else:
		print('\nPlease select a direction or end the game!')
		flag = 2
		return
	
	if win_check():
		print('After {} steps, you win!'.format(step))
		flag = 0
		return
#---------------------------------------------------------
#main function
while flag == 1:
	if step == 0: new_game()
	else: move()
	while flag == 2: #若出现非法状态，将重复输入环节，直到操作合法
		flag = 1
		move()
		
	if flag == 0:
		S = input('\nStart new?(y/n)\n')
		if S == 'y' or S == 'Y':
			flag = 1
			step = 0
			continue
		elif S == 'n' or S == 'N':
			print('\nSee you!')
			break
		
		while S != 'y' and S != 'Y' and S != 'n' and S != 'N':
			print('\nStart new?(y/n)\n')
	
	print()		
	for i in range(0,N):
		l_Now = len(str(a[i]))
		if i == b_Position: print(' '*l,end=' ')
		else: print(a[i],' '*(l-l_Now),sep='',end=' ')
		if (i+1) % n ==0: print()
	print("You have moved {} steps".format(step))
	step += 1