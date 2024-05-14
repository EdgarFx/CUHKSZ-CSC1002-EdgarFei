import random

n = int(input('Enter the desired dimension of the puzzle:'))

directions = input('Enter the four letters used for left, right, up and down directions:').split()
left = directions[0]
right = directions[1]
up = directions[2]
down = directions[3]

# 获得初始二维数组的函数
def InitialArray(n):
    # 生成顺序数组
    blocks = []
    numbers = list(range(1,n**2))
    numbers.append(0)

    # 将数字添加到二维数组
    for row in range(n):
        blocks.append([])
        for column in range(n):
            element = numbers[row*n + column]
            if element == 0:
                zero_row = row
                zero_column = column
            blocks[row].append(element)
    
    # TODO 随机移动打乱数组

# 方块移动算法
