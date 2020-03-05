#imporintg modules
import turtle
import time
import random
import os

delay = 0.1

#score

score = 0
high_score = 0

#set up the game screen

wn=turtle.Screen()
wn.title("Snake Game in Python")
wn.setup(width=600, height=600)
#remives the animation
wn.tracer(0)
wn.bgcolor("green")

#Creating a Snake head
head = turtle.Turtle()
head.shape("circle")
head.speed(0)
head.color("grey")
head.penup()
head.goto(0,0)
head.direction = "stop"

#Creating the snake food
food = turtle.Turtle()
food.shape("square")
food.speed(0)
food.color("red")
food.penup()
food.goto(0,100)

segments = []

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score: 0  High Score 0", align="center", font=("Courier", 24, "normal"))

#Functions

def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"


#moving the head of the snake

def move():
    if head.direction == "up":
        y = head.ycor()
        #moving 20 pixels each time
        head.sety(y + 20)
        
    if head.direction == "down":
        y = head.ycor()
        #moving 20 pixels each time
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        #moving 20 pixels each time
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        #moving 20 pixels each time
        head.setx(x + 20)

#Keyboard bindings

wn.listen()
wn.onkeypress(go_up,"Up")
wn.onkeypress(go_down,"Down")
wn.onkeypress(go_left,"Left")
wn.onkeypress(go_right,"Right")


#main game loop

while True:
    wn.update()
    
    #checking for a collision with the boader
    if head.xcor()> 290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        #hide segments
        for segment in segments:
            segment.goto(1000,1000)

        #clear the segment
        segments.clear()

    #reset score
        score = 0
        pen.clear()
        pen.write("Score: {}  High Score {}".format(score,high_score), align="center", font=("Courier", 24, "normal"))
        
    
    #check to see if the head has collided with the food
    if head.distance(food) < 20:
        #Move the food on a random spot on the screen
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        food.goto(x,y)

    #adding a segemnt
        new_segment = turtle.Turtle()
        new_segment.speed()
        new_segment.shape("square")
        new_segment.color("blue")
        new_segment.penup()
        segments.append(new_segment)

    #increasing the score
        score= score + 10


        #check for the high score
        if score > high_score:
            high_score = score
            
        pen.clear()
        pen.write("Score: {}  High Score {}".format(score,high_score), align="center", font=("Courier", 24, "normal"))
        

    #Move the end segment first in reverse order
    for index in range(len(segments)-1,0,-1):
        x = segments[index-1].xcor()
        y = segments[index -1].ycor()
        segments[index].goto(x,y)

    #move segment 0 to where the head is
    if len(segments) >0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)
      
    
    move()

    #check for collison with the body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
              #hide segments
            for segment in segments:
                segment.goto(1000,1000)

            #clear the segment
            segments.clear()
            #clears the score
            score = 0

        pen.clear()
        pen.write("Score: {}  High Score {}".format(score,high_score), align="center", font=("Courier", 24, "normal"))
        
    
    time.sleep(delay)


#this keeps the window game always open
wn.mainloop()
