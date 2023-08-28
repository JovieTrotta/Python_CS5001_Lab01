'''
Jovienne Trotta
CS 5001 | Fall 2022
Lab 1 : Making Shapes with Turtle

This is our first lab where we practice some basic python by making shapes.
This file includes my first and second shape.
'''

from turtle import *

#this will make the background color blue
bgcolor("blue")

#this is the start of shape one, which will draw a cat face
#this will draw the cat's face
up()
backward(150)
down()
fillcolor("orange")
begin_fill()
left(70)
forward(100)
right(140)
forward(100)
right(275)
right(15)
forward(200)
left(70)
forward(100)
right(140)
forward(100)
right(20)
forward(200)
right(90)
forward(337)
right(90)
forward(200)
end_fill()

#this will make the left eye
up()
right(90)
forward(75)
right(90)
forward(40)
down()
fillcolor("green")
begin_fill()
forward(30)
left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
end_fill()

#this will make the nose
up()
right(180)
forward(75)
right(90)
forward(40)
down()
fillcolor("pink")
begin_fill()
left(50)
forward(30)
left(80)
forward(30)
left(140)
forward(45)
end_fill()

#this will make the right eye
up()
right(180)
forward(75)
left(90)
forward(40)
down()
fillcolor("green")
begin_fill()
right(90)
forward(30)
right(90)
forward(30)
right(90)
forward(30)
right(90)
forward(30)
end_fill()

#this will draw the right whiskers
up()
left(90)
forward(30)
left(90)
forward(40)
down()
color("black")
left(45)
forward(50)
left(180)
forward(50)
right(150)
forward(50)

#this will draw the left whiskers
up()
left(180)
forward(50)
left(15)
forward(45)
down()
color("black")
left(45)
forward(50)
right(180)
forward(50)
left(150)
forward(50)
#this is the end of shape one

#this is the start of shape two, which will be a sun
up()
right(30)
forward(200)
right(90)
forward(200)
down()
fillcolor("red")
begin_fill()
circle(80)
end_fill()
fillcolor("orange")
begin_fill()
circle(60)
end_fill()
fillcolor("yellow")
begin_fill()
circle(40)
end_fill()
#this is the end of shape two

#this will draw the picture
mainloop()