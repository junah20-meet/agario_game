import turtle
import time
import random
import math
from ball import Ball

turtle.colormode(1)
turtle.tracer(0)
turtle.hideturtle()
running = True
screen_width = turtle.getcanvas().winfo_width()/2
screen_height = turtle.getcanvas().winfo_height()/2

my_ball = Ball(0, 0, 10, 10, 50, "black")
writer = turtle.clone()
writer.pu()
writer.goto(200, 300)
number_of_balls = 6
minimum_ball_radius = 10
maximum_ball_radius = 70
minimum_ball_dx = -2
maximum_ball_dx = 2
minimum_ball_dy = 2
maximum_ball_dy = 2
BALLS = []

for i in range(number_of_balls):
    x = random.randint(-screen_width + maximum_ball_radius,screen_width - maximum_ball_radius)
    y = random.randint(-screen_height + maximum_ball_radius , screen_height - maximum_ball_radius)
    dx = random.randint(minimum_ball_dx , maximum_ball_dx)
    dy = random.randint(minimum_ball_dy , maximum_ball_dy)
    while dx == 0:
        dx = random.randint(minimum_ball_dx , maximum_ball_dx)
    while dy == 0:
        dy = random.randint(minimum_ball_dy , maximum_ball_dy)
    r = random.randint(minimum_ball_radius , maximum_ball_radius)
    color = (random.random(), random.random(), random.random())

    new_ball = Ball(x, y, dx, dy, r, color)
    BALLS.append(new_ball)

def move_all_balls():
    for ball in BALLS:
        ball.move(screen_width , screen_height)

def same_ball(Ball_a , Ball_b):
    if Ball_a == Ball_b:
        return True
    else:
         return False

def collide(Ball_a , Ball_b):
    if Ball_a == Ball_b:
        return False
    distance = math.sqrt((Ball_a.xcor()-Ball_b.xcor())**2 + (Ball_a.ycor()-Ball_b.ycor())**2)
    sum_of_r = Ball_a.r + Ball_b.r
    if distance <= sum_of_r:
        return True
    else:
        return False

def check_all_balls_collisions():
    global running
    all_balls=[]
    all_balls.append(my_ball)
    for ball in BALLS:
        all_balls.append(ball)
    for ball_a in all_balls:
        for ball_b in all_balls:
            if (collide(ball_a,ball_b)):
                r1=ball_a.r
                r2=ball_b.r
                x=random.randint(-screen_width + maximum_ball_radius,screen_width - maximum_ball_radius)
                y=random.randint(-screen_height + maximum_ball_radius,screen_height - maximum_ball_radius)
                dx=random.randint(minimum_ball_dx,maximum_ball_dx)
                dy=random.randint(minimum_ball_dy,maximum_ball_dy)
                radius=random.randint(minimum_ball_radius,maximum_ball_radius)
                color=(random.random(), random.random(), random.random())
                while(dx==0):
                     dx=random.randint(minimum_ball_dx,maximum_ball_dx)

                while(dy==0):
                    dy=random.randint(minimum_ball_dy,maximum_ball_dy)

                if (r1>r2):
                    print("ball b smaller")
                    ball_b.new_ball(x,y,dx,dy,radius,color)
                    ball_a.r=ball_a.r+5
                    ball_a.shapesize(ball_a.r/10)
                    if (ball_b==my_ball):
                        print("my ball eaten")
                        running=False
                else:
                    print("ball a smaller")
                    ball_a.new_ball(x,y,dx,dy,radius,color)
                    ball_b.r=ball_b.r+10
                    ball_b.shapesize(ball_b.r/10)
                    if (ball_a==my_ball):
                        print("my ball eaten")

                        running=False

def movearound():
    my_ball.goto( turtle.getcanvas().winfo_pointerx() - screen_width*2,screen_height - turtle.getcanvas().winfo_pointery())

score = 0
while(running==True):
    score += 1
    print("running",running)
    screen_width=turtle.getcanvas().winfo_width()/2
    screen_height=turtle.getcanvas().winfo_height()/2
    movearound()
    move_all_balls()
    check_all_balls_collisions()
    turtle.update()
    time.sleep(1/60)
    if score % 10 == 0:
        writer.clear()
        writer.write(score / 10,  font=("Arial", 40, "normal"))
    if (my_ball.r >= 500):
        running = False
        turtle.write('Win', move=False, align="center", font=("Arial", 40, "normal"))
        print("byee")

turtle.write('GAME OVER', move=False, align="center", font=("Arial", 40, "normal"))

turtle.mainloop()
