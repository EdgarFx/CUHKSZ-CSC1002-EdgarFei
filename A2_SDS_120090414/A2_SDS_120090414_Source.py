import turtle
import random

#-------------------------------------------------------------------
# part 1: Set the initial interface

def set_screen():
    # Set the size and position of the main screen
    s = turtle.Screen()
    s.setup(660,740)
    s.tracer(0)

    # Set the title of the main screen
    s.title("Snake by Edgar")

    # Set subtitles at the start of the game
    subtitles = turtle.Turtle()
    subtitles.up()
    subtitles.ht()
    subtitles.goto(-230,60)
    subtitles.write(
        '''
        Welcome to Edgar's version of snake...
        
        You are going to use the 4 arrow keys to move the snake
        around the screen, trying to consume all the food items
        before the monster catches you...

        Click anywhere on the screen to start the game, have fun!
        ''',
        font = ("Times New Roman", 11, "normal")
    )

    set_board() # draw the gaming board
    set_contact() # write the initial contact (0)
    set_time() # write the initial time (0s)
    set_motion() # write the initial motion (Paused)

    s.update()

    return s, subtitles

contact = 0
contact_pen = turtle.Turtle()
def set_contact(): # write the contact value
    contact_pen.up()
    contact_pen.ht()
    contact_pen.goto(-200,240)
    contact_pen.write("Contact: %d"%contact, font=("Times New Roman", 14, "bold"))


time = 0
time_pen = turtle.Turtle()
def set_time(): # write the time value
    time_pen.up()
    time_pen.ht()
    time_pen.goto(-60,240)
    time_pen.write("Time: %ds"%time, font=("Times New Roman", 14, "bold"))


motion = "Paused"
motion_pen = turtle.Turtle()
def set_motion(): # write the motion status
    motion_pen.up()
    motion_pen.ht()
    motion_pen.goto(80,240)
    motion_pen.write("Motion: %s"%motion, font=("Times New Roman", 14, "bold"))
    
def set_board(): # draw the gaming board
    board = turtle.Turtle()
    board.speed(0)
    board.up()
    board.ht()
    board.goto(-250,290)
    board.down()
    for i in range(2):
        board.forward(500)
        board.right(90)
        board.forward(580)
        board.right(90)
    board.up()
    board.goto(-250,210)
    board.down()
    board.forward(500)  
    return board

def snake(): # draw the head of the snake (red)
    snake = turtle.Turtle()
    snake.up()
    snake.goto(0,-40)
    snake.shape("square")
    snake.color("red","red")
    return snake

def monster(): # draw the monster which is purple
    monster = turtle.Turtle()
    monster.up()
    x = random.randint(-48,48)
    while abs(x) <= 16:
        x = random.randint(-48,48)
    y = random.randint(-48,10)
    while abs(y+5) <= 16:
        y = random.randint(-48,10)
    monster.goto(x*5,y*5)
    monster.shape("square")
    monster.color("purple","purple")
    return monster

#-----------------------------------------------------------------------------
# part 2: run the game

# use numbers to represent the flag of the game
# 0 means need to click
# 1 means the game starts, but the snake and the monster are not moving
# 2 means normally playing
# 3 means game over
# 4 means win

game_status = 0
def start_game(x,y): # the core function to play the game
    global game_status
    if game_status != 0:
        return
    game_status = 1
    subtitles.clear()
    food()
    set_key()

    fx_screen.update()
    run_time()
    run_motion()

    snake_move()
    monster_move()


#check whether any food near (x,y). This can keep food from getting too close
def check_food(x,y):
    for food in food_items:
        if abs(food.xcor()-x) <= 20 and abs(food.ycor()-y) <= 20:
            return False
    return True

food_items = []
def food(): # generate the food items randomly
    for i in range(1,10):
        food = turtle.Turtle()
        food.speed(0)
        food.up()
        food.ht()
        x = random.randint(-11,11)
        y = random.randint(-13,9)
        while not check_food(x*20,y*20): 
            x = random.randint(-11,11)
            y = random.randint(-13,9)       # *20 is to make the food items and the center of the snake are in the same line
        food.goto(x*20, y*20-5)             # y*20-5 is to have a better visual feeling
        food.write(i, font=("Times New Roman", 10, "normal"))
        food_items.append(food)

def run_time(): # let the time runs
    global time
    if game_status == 1:
        fx_screen.ontimer(run_time, 0)
    elif game_status == 3 or game_status == 4:
        return
    else:
        time_pen.clear()
        set_time()
        time += 1
        fx_screen.ontimer(run_time, 1000)
        fx_screen.update()

def run_motion(): # change the motion value according to the motion of the snake
    global motion
    if game_status == 1:
        fx_screen.ontimer(run_motion, 0)
    else:
        motion = now_direction.capitalize()
        if now_direction == 'stop':
            motion = 'Paused'
        motion_pen.clear()
        set_motion()
        if game_status == 3 or game_status == 4:
            return
        else:   
            fx_screen.ontimer(run_motion, speed//2)
            fx_screen.update()

def set_key(): # set the four directions
    fx_screen.onkey(stop, "space")
    fx_screen.onkey(right, "Right")
    fx_screen.onkey(left, "Left")
    fx_screen.onkey(up, "Up")
    fx_screen.onkey(down, "Down")
    fx_screen.listen()

#----------------------------------------------------------------------
# part 3: check the game status

def is_win(): # check whether we win or not
    global game_status
    if game_status == 3 or generated_tails:
        return
    
    is_win = True
    for i in range(9):
        if eaten[i] == False:
            is_win = False
    
    if is_win:
        win = turtle.Turtle()
        win.up()
        win.ht()
        win.goto(snake.xcor(), snake.ycor())
        win.color("red")
        win.write("winner!!", font=("Times New Roman", 14, "normal"))
        game_status = 4

def is_lose():  # check whether we lose or not
    global game_status
    if abs(snake.xcor() - monster.xcor()) < 20 and abs(snake.ycor() - monster.ycor()) < 20:
        lose = turtle.Turtle()
        lose.up()
        lose.ht()
        lose.goto(snake.xcor(), snake.ycor())
        lose.color("purple")
        lose.write("Game Over!!", font=("Times New Roman", 14, "normal"))
        game_status = 3


#----------------------------------------------------------------------
# part 4: running snake

now_direction = 'stop'  
last_direction = 'null'
angle = {'right':0,'left':180,'up':90,'down':270,'stop':0} # store the relationship between the direction strings and the angle
distance = {'right':20,'left':20,'up':20,'down':20,'stop':0} # store the relationship between the direction strings and the distance

def stop():
    global now_direction
    global last_direction
    global game_status
    if now_direction == 'stop' and last_direction != 'null':
        now_direction = last_direction
        last_direction = 'null'
    else:
        last_direction = now_direction
        now_direction = 'stop'
        
def right():
    global now_direction
    global game_status
    now_direction = 'right'
    game_status = 2

def left():
    global now_direction
    global game_status
    now_direction = 'left'
    game_status = 2

def up():
    global now_direction
    global game_status
    now_direction = 'up'
    game_status = 2

def down():
    global now_direction
    global game_status
    now_direction = 'down'
    game_status = 2

def is_edge(): # check whether the snake go directly to the edge of the board and touch the edge, then stop the snake
    global now_direction
    if snake.xcor() >= 239 and now_direction == 'right':
        now_direction = 'stop'
    elif snake.xcor() <= -239 and now_direction == 'left':
        now_direction = 'stop'
    elif snake.ycor() >= 199 and now_direction == 'up':
        now_direction = 'stop'
    elif snake.ycor() <= -279 and now_direction == 'down':
        now_direction = 'stop'
    fx_screen.ontimer(is_edge, speed)

generated_tails = 5
speed = 300
snake_x = [0]
snake_y = [0]
eaten = [False]*9

def has_eaten(): # check whether a food item has been eaten
    global eaten
    global game_status
    global generated_tails
    if game_status == 3:
        return
    for i in range(9):
        if eaten[i] == True:
            continue
        elif abs(snake.xcor()-food_items[i].xcor()) <= 10 and abs(snake.ycor()-food_items[i].ycor()) <= 10:
            food_items[i].clear()
            generated_tails += i+1
            eaten[i] = True


def extend():
    global generated_tails
    speed = 450
    snake.stamp()
    snake.setheading(angle[now_direction])
    snake.forward(distance[now_direction])
    snake_x.append(snake.xcor())
    snake_y.append(snake.ycor())
    generated_tails -= 1

def normal_move():
    global generated_tails
    speed = 300
    snake.stamp()
    snake.setheading(angle[now_direction])
    snake.forward(distance[now_direction])
    snake_x.append(snake.xcor())
    snake_y.append(snake.ycor())
    snake.clearstamps(1)
    snake_x.pop(0)
    snake_y.pop(0)

def snake_move():
    global game_status
    global speed
    global generated_tails
    fx_screen.update()
    is_win()
    is_lose()
    is_edge()
    has_eaten()
    if game_status == 3:
        return
    if game_status == 4:
        return
    if game_status == 1 or now_direction == 'stop':
        fx_screen.ontimer(snake_move,speed)
        return
    snake.color("blue","black")
    if generated_tails:
        extend()
    else:
        normal_move()
    snake.color("red","red")
    fx_screen.update()
    fx_screen.ontimer(snake_move,speed)



#------------------------------------------------------------------------
# part 5: running monster
m_speed = 300
m_direction = 'stop'


def is_x_longer():
    return abs(monster.xcor() - snake.xcor()) >= abs(monster.ycor() - snake.ycor())

def change_m_direction():
    global m_direction
    if game_status == 1:
        m_direction = 'stop'
        return
    
    if monster.xcor() < snake.xcor() and monster.ycor() < snake.ycor():
        if is_x_longer():
            if m_speed <= speed:
                m_direction = 'right'
            else:
                m_direction = 'up'
        else:
            if m_speed <= speed:
                m_direction = 'up'
            else:
                m_direction = 'right'
    
    elif monster.xcor() < snake.xcor() and monster.ycor() > snake.ycor():
        if is_x_longer():
            if m_speed <= speed:
                m_direction = 'right'
            else:
                m_direction = 'down'
        else:
            if m_speed <= speed:
                m_direction = 'down'
            else:
                m_direction = 'right'

    elif monster.xcor() > snake.xcor() and monster.ycor() < snake.ycor():
        if is_x_longer():
            if m_speed <= speed:
                m_direction = 'left'
            else:
                m_direction = 'up'
        else:
            if m_speed <= speed:
                m_direction = 'up'
            else:
                m_direction = 'left'

    elif monster.xcor() > snake.xcor() and monster.ycor() > snake.ycor():
        if is_x_longer():
            if m_speed <= speed:
                m_direction = 'left'
            else:
                m_direction = 'down'
        else:
            if m_speed <= speed:
                m_direction = 'down'
            else:
                m_direction = 'left'

    elif monster.xcor() == snake.xcor():
        if monster.ycor() < snake.ycor():
            m_direction = 'up'
        else:
            m_direction = 'down'

    elif monster.ycor() == snake.ycor():
        if monster.xcor() < snake.xcor():
            m_direction = 'right'
        else:
            m_direction = 'left'


def check_if_contact(): # check whether the monster contact with the body of the snake and change the contact value
    global contact
    x = monster.xcor()
    y = monster.ycor()
    is_contact = False
    for i in range(len(snake_x)):
        if abs(x - snake_x[i]) <= 20 and abs(y - snake_y[i]) <= 20:
            is_contact = True
            break
    if is_contact:
        contact += 1
    
    contact_pen.clear()
    set_contact()

def monster_move():
    global game_status
    is_win()
    is_lose()

    if game_status == 3:
        return
    if game_status == 4:
        return

    change_m_direction()
    m_speed = random.randint(260,550)
    monster.stamp()
    monster.setheading(angle[m_direction])
    monster.forward(distance[m_direction])
    monster.clearstamps(1)

    check_if_contact()

    fx_screen.update()
    fx_screen.ontimer(monster_move, m_speed)


#----------------------------------------------------------------------

if __name__ == "__main__":
    fx_screen, subtitles = set_screen()
    snake = snake()
    monster = monster()
    fx_screen.update()
    fx_screen.onclick(start_game)     
    fx_screen.mainloop()








