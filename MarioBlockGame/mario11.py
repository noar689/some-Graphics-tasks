from turtle import *
import random
import time

win=Screen()
win.bgcolor("#56b5e3")
win.setup(600,600)
win.tracer(0)

delay = 0.1

#player circle
p_circle=Turtle("circle")
p_circle.color("#ffffff")
p_circle.speed(0)
p_circle.penup()
# p_circle.pen({"pensize":7 , "resizemode":"auto"})
p_circle.goto(-280,-280)
p_circle.dir = "stop"

#walls
wall1 = Turtle("square")
wall1.color("#aa5835")
wall1.speed(0)
x1 = -100
y1 = -280
wall1.penup()
# wall1.pen({"pensize":7 , "resizemode":"auto"})
wall1.goto(x1, y1)

wall2 = Turtle("square")
wall2.color("#aa5835")
wall2.speed(0)
x2 = -100
y2 = -260
wall2.penup()
# wall1.pen({"pensize":7 , "resizemode":"auto"})
wall2.goto(x2, y2)

wall3 = Turtle("square")
wall3.color("#aa5835")
wall3.speed(0)
x3 = -100
y3 = -240
wall3.penup()
# wall1.pen({"pensize":7 , "resizemode":"auto"})
wall3.goto(x3, y3)


#score
score = 0
high_score = 0
text =Turtle("circle")
text.speed(0)
text.color('#F2E8C6')
text.hideturtle()
text.penup()
text.goto(0,270)
text.write("Score : 0 High Score : 0 ", align="center" ,font=("Arial",18,'bold'))

def keyboard():
    listen()
    onkeypress(go_up,"Up")
    # onkeypress(go_down,"Down")
    onkeypress(go_left,"Left")
    onkeypress(go_right,"Right")
#keyboard
def go_up():
    if p_circle.dir != "down":
	    p_circle.dir = "up"
# def go_down():
#     if p_circle.dir != "up":
# 	    p_circle.dir = "down"
def go_left():
    if p_circle.dir != "right":
	    p_circle.dir = "left"
def go_right():
    if p_circle.dir != "left":
	    p_circle.dir = "right"

def move (): 
    x = p_circle.xcor()
    y =  p_circle.ycor()
    if p_circle.dir =="up":
        p_circle.goto(x,-210)
        


        
    elif p_circle.dir =="down":
        p_circle.sety(y-20)
    elif p_circle.dir =="left":
        p_circle.setx(x-20)
    elif p_circle.dir =="right":
        p_circle.setx(x+20)

keyboard()

#game loop and conditions
def crash():
    time.sleep(1)
    text2 = Turtle()
    text2.speed(0)
    text2.color('#F2E8C6')
    text2.hideturtle()
    text2.penup()
    text2.goto(0,0)
    text2.write("Try Again" , align= 'center',font=("Arial",36,'bold'))
    time.sleep(0.5)
    text2.clear()
    p_circle.goto(-280,-280)
    p_circle.dir = "stop"
    wall1.goto(x1, y1)
    wall2.goto(x2, y2)
    wall3.goto(x3, y3)
    global delay
    delay = 0.09
    global score
    score = 0
    text.clear()
    text.write("Score : {} High Score : {} " .format( score , high_score), align="center" ,font=("Arial",18,'bold'))

while True:
    win.update()
    if p_circle.xcor()>=300 or p_circle.xcor()<=-300 or p_circle.ycor()>=300 or p_circle.ycor()<=-300 :
        crash()
    if p_circle.distance(wall1) < 25 or p_circle.distance(wall2) < 25 or p_circle.distance(wall3) < 25:
        crash()
    if p_circle.xcor() > wall1.xcor() :
        wall1.stamp()
        wall1.fd(150)
        wall2.stamp()
        wall2.fd(150)
        wall3.stamp()
        wall3.fd(150)
        wall1.clear()
        wall2.clear()
        wall3.clear()
        delay -= 0.001
        score+=1
        if score > high_score:
             high_score = score           
        text.clear()
        text.write("Score : {} High Score : {} " .format( score , high_score), align="center" ,font=("Arial",18,'bold'))
    move()

    time.sleep(0.1)


done()
