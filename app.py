from turtle import *

bgcolor('black')
speed(500)
hideturtle()

for i in range(5000):
    color('violet')
    circle(i)
    color('darkblue')
    circle(i*0.8)
    right(119)
    forward(100)
done()