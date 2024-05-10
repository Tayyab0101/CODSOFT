from turtle import *
import random

getscreen()
speed(10)
shape("classic")
color("red", "yellow")
begin_fill()
while True:
    forward(200)
    left(175)
    if heading()==0:
        break
    
end_fill()
hideturtle()
exitonclick()
