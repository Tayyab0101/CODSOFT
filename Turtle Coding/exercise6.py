import random
from turtle import *

getscreen()
speed(0)
title("Dot Painting")
screensize(600, 600)
colors = ["red", "green", "purple", "black", "yellow", "blue", "brown", "cyan", "chocolate1"]

for i in range(100):
    penup()
    # setheading(random.randint(25, 375))
    goto(random.randint(-300,300), random.randint(-300,300))
    # forward(50)
    pencolor(random.choice(colors))
    dot(20)
    pendown()
    

exitonclick()