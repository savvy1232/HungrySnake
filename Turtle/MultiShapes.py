import turtle as t
import random

colours = ["green", "black", "pink" , "red" , "blue" , "gold" ]
tim = t.Turtle()

def draw_shape(num_sides):
    angle = 360/num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)



for shape_side in range(3,10):
    tim.color(random.choice(colours))
    draw_shape(shape_side)