from turtle import *
import random
import time

win=Screen()
win.bgcolor("#952323")
win.setup(600,600)
win.tracer(0)

#snake head
head=Turtle("square")
head.color("#F2E8C6")
head.speed(0)
head.penup()
head.goto(0,0)
head.dir = "stop"

delay = 0.1

#food
food=Turtle("circle")
food.color("black")
food.speed(0)
food.penup()
food.goto(random.randint(-250, 250), random.randint(-250, 250) or head.distance(head.position()))

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
    onkeypress(go_down,"Down")
    onkeypress(go_left,"Left")
    onkeypress(go_right,"Right")

#keyboard
def go_up():
    if head.dir != "down":
	    head.dir = "up"
def go_down():
    if head.dir != "up":
	    head.dir = "down"
def go_left():
    if head.dir != "right":
	    head.dir = "left"
def go_right():
    if head.dir != "left":
	    head.dir = "right"

def move (): 
    x = head.xcor()
    y =  head.ycor()
    if head.dir =="up":
        head.sety(y+20)
    elif head.dir =="down":
        head.sety(y-20)
    elif head.dir =="left":
        head.setx(x-20)
    elif head.dir =="right":
        head.setx(x+20)

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
    head.goto(0,0)
    head.dir = "stop"
    food.goto(random.randint(-250, 250), random.randint(-250, 250) or head.distance(head.position()))
    global delay
    delay = 0.09
    for segment in segments:
        segment.hideturtle()
    segments.clear()
    global score
    score = 0
    text.clear()
    text.write("Score : {} High Score : {} " .format( score , high_score), align="center" ,font=("Arial",18,'bold'))

segments=[]
while True:
    win.update()
    if head.xcor()>=300 or head.xcor()<=-300 or head.ycor()>=300 or head.ycor()<=-300 :
        crash()
    if head.distance(food)<20:
        food.goto(random.randint(-250, 250), random.randint(-250, 250) or head.distance(head.position()))
        new_segment=Turtle("square")
        new_segment.color("#BCA37F")
        new_segment.penup()
        segments.append(new_segment)
        # delay -= 0.001
        if score >= 5 :
             delay -= 0.001
        score += 1
        if score > high_score:
             high_score = score           
        text.clear()
        text.write("Score : {} High Score : {} " .format( score , high_score), align="center" ,font=("Arial",18,'bold'))

    for i in range(len(segments)-1,0,-1):
        x = segments[i-1].xcor()
        y = segments[i-1].ycor()
        segments[i].goto(x,y)
    if len(segments)>0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)
    move()
    for s in segments :
        if s.distance(head) < 20:
            crash()

    time.sleep(0.1)

done()