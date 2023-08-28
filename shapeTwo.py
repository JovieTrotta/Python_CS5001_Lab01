'''
Jovienne Trotta
CS 5001 | Fall 2022
Lab 1 : Making Shapes with Turtle

This is our first lab where we practice some basic python by making shapes.
This file includes my scaled second shape.
'''

from turtle import *

scale = 5.0

#this will make the background color blue
bgcolor("blue")

#this is the start of shape two, which will be a sun
fillcolor("red")
begin_fill()
circle(80*scale)
end_fill()
fillcolor("orange")
begin_fill()
circle(60*scale)
end_fill()
fillcolor("yellow")
begin_fill()
circle(40*scale)
end_fill()
#this is the end of shape two

#this will draw the picture
mainloop()