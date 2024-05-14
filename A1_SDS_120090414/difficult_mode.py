#CSC_1002 Assignment_1

import heapq
import random

n=0; N=0
#以序列的形式储存华容道，左移位置-1，上移位置-n
a = []; c = []
flag = 1 #游戏状态标志，0表示一局游戏结束，1表示进行中，2表示操作非法
step = 0
row = 0; column = 0;
l = 0; b_Position = 0;
U = 'u'; R = 'r'; D = 'd'; L = 'l'
limit = 0
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
	global row, column
	global a, c
	c = [0]*N
	F = 0 #当前华容道的状态量
	for i in range(0,N):
		if a[i] == 0:
			column = i//n+1; row = i%n
			continue
		update(a[i])
		F += a[i]-query(a[i]) 
	#先求出逆序对数再将逆序对数转换成状态量
	#print(F, column)
	if n%2==1: F%=2
	else: F=(F%2)^( (n-column)%2 )
	return F
#---------------------------------------------------------

def new_game():
	global a, c
	global n, N
	global l, b_Position
	global U, R, D, L
	global limit
	limit = 0
	
	n = input('\nSelect the level you want(1~3) :\n')
	while True:
		try:
			n = int(n)
		except:
			n = input('\nSelect the level you want(1~3) :\n')
		else:
			if n <=3: break
			else:
				n = input('\nSelect the level you want(1~3) :\n') 
				continue
	
	if n == 1 or n == 2:
		n += 2
	else:
		limit = 1
	
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
		next_Step = input('\nEnter the two letters used for up and left directions > {} {}\nOr enter q to end the game!\n'.format(U,L))
	elif b_Position == n-1:#右上角
		next_Step = input('\nEnter the two letters used for up and right directions > {} {}\nOr enter q to end the game!\n'.format(U,R))
	elif b_Position == N-1:#右下角
		next_Step = input('\nEnter the two letters used for right, down directions > {} {}\nOr enter q to end the game!\n'.format(R,D))
	elif b_Position == N-n:#左下角
		next_Step = input('\nEnter the two letters used for down and left directions > {} {}\nOr enter q to end the game!\n'.format(D,L))
	elif b_Position < n:#第一行
		next_Step = input('\nEnter the three letters used for up, right and left directions > {} {} {}\nOr enter q to end the game!\n'.format(U,R,L))
	elif b_Position >= N-n:#第n行
		next_Step = input('\nEnter the three letters used for right, down and left directions > {} {} {}\nOr enter q to end the game!\n'.format(R,D,L))
	elif (b_Position+1) % n == 1:#第一列
		next_Step = input('\nEnter the three letters used for up, down and left directions > {} {} {}\nOr enter q to end the game!\n'.format(U,D,L))
	elif (b_Position+1) % n == 0:#第n列
		next_Step = input('\nEnter the three letters used for up, right and down directions > {} {} {}\nOr enter q to end the game!\n'.format(U,R,D))
	else: next_Step = input('\nEnter the four letters used for up, right, down and left directions > {} {} {} {}\nOr enter q to end the game!\n'.format(U,R,D,L))
	
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
		print('\nAfter {} steps, you win!'.format(step))
		flag = 0
		return
#---------------------------------------------------------
#A*求可行解
origin = []
ans = []
_col = [-1, 0, 1, 0]
_row = [0, 1, 0, -1]

openTable = []

class State():
	def __init__(self, state=None, hashNum=None, g=0, h=0, father=None):
		self.state = state
		self.hashNum = hashNum
		self.g = g
		self.h = h
		self.f = g + h
		self.father = father
		self.kids = []
		
	def __lt__(self, other): return self.f < other.f
	
	def __eq__(self, other): 
		return self.hashNum == other.hashNum

def illegal(x, y, n):
	return x < 0 or x >= n or y < 0 or y >= n

def copy(state):
	s = []; l = len(state)
	for i in range(l):
		s.append([])
		s[i] = state[i][:]
	return s

def get_dis(a, b): #manhattan dis as the estimated value
	sA = a.state
	sB = b.state
	dis = 0; l = len(sA)
	for i in range(l):
		for j in range(l):
			if sA[i][j] == sB[i][j]:
				continue
			if sA[i][j] == 0:
				col, row = l-1, l-1
			else:
				col = sA[i][j]//l
				row = sA[i][j] - l*col - 1
			dis += abs(col - i) + abs(row - j)
	return dis

def get_kids(now, end, hashTable, openTable): #bfs
	if now == end:
		heapq.heappush(openTable, end)
		return
	l = len(now.state)
	for i in range(l):
		for j in range(l):
			if now.state[i][j] != 0:
				continue
			for d in range(4):
				col = i + _col[d]
				row = j + _row[d]
				if illegal(col, row, n):
					continue
				global nodeSum
				s = copy(now.state)
				s[i][j], s[col][row] = s[col][row], s[i][j]
				has = hash(str(s))
				if has in hashTable: continue
				hashTable.add(has)
				node = State(s, has, now.g+1, get_dis(now, end), now)
				now.kids.append(node)
				heapq.heappush(openTable, node)

path = []
def printNode(state):
	n = len(state)
	l = len(str(n*n))
	for i in range(n):
		for j in range(n):
			if state[i][j] == 0:
				print(' '*l, end=' ')
			else:
				ll = len(str(state[i][j])) 
				print(state[i][j], ' '*(l-ll), sep='', end=' ')
		print()
	print()

def get_path(son):
	global path
	path = []
	steps = son.g	
	while son.father:
		path.append(son.state)
		son = son.father
	path.append(son.state)
	return steps
		
def aStar(st, end):
	root = State(st, hash(str(st)), 0, 0, None)
	leaf = State(end, hash(str(end)), 0, 0, None)
	if root == leaf: 
		return 0
	
	openTable = []
	openTable.append(root)
	heapq.heapify(openTable)
	
	hashTable = set()
	hashTable.add(root.hashNum)
	
	while len(openTable):
		node = heapq.heappop(openTable)
		if node == leaf:
			return get_path(node)
		get_kids(node, leaf, hashTable, openTable)


def be_harder():
	global n
	global a
	p = 0
	origin = []
	ans = []
	for i in range(n):
		origin.append([])
		ans.append([])
		for j in range(n):
			origin[i].append(a[p])
			if p == n*n - 1: 
				p = -1
			ans[i].append(p + 1)
			p += 1
	#print(origin)
	#print(ans)
	
	return aStar(origin, ans) 
#---------------------------------------------------------

print("Welcome to the sliding puzzle game!")
print("We have 3 levels for you:")
print("1. 3*3 easy")
print("2. 4*4 easy")
print("3. 3*3 hard")

#main function
while flag == 1:
	
	if flag == 1 and limit and step > limit:
		print("\nYou lose!")
		
		S = input('\nWant to see the solution?(y/n)\n')
		while S != 'y' and S != 'Y' and S != 'n' and S != 'N':
			S = input('\nWant to see the solution?(y/n)\n')
		if S == 'y' or S == 'Y':
			r = 0
			while len(path):
				if r:
					print("Step {}:".format(r))
				else: print("Origin:")
				printNode(path.pop())
				r += 1
			pass
		elif S == 'n' or S == 'N':
			pass
		flag = 0
		
	if flag:
		if step == 0: new_game()
		else: move()
		while flag == 2: #若出现非法状态，将重复输入环节，直到操作合法
			flag = 1
			move()
		
		if limit and step == 0:
			limit = be_harder()
			print("\nYou have to finish this game in {} steps!".format(limit))
	
	if flag == 0:
		S = input('\nStart new?(y/n)\n')
		while S != 'y' and S != 'Y' and S != 'n' and S != 'N':
			S = input('\nStart new?(y/n)\n')
		if S == 'y' or S == 'Y':
			flag = 1
			step = 0
			continue
		elif S == 'n' or S == 'N':
			print('\nSee you!')
			break
	
	print()		
	for i in range(0,N):
		l_Now = len(str(a[i]))
		if i == b_Position: print(' '*l,end=' ')
		else: print(a[i],' '*(l-l_Now),sep='',end=' ')
		if (i+1) % n ==0: print()
	
	print("You have moved {} steps".format(step))
	step += 1
