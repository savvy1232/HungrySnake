import turtle as t
import random

tim = t.turtle()
t.colormode(255)

def color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color=(r,g,b)
    return color

directions = [0,90,180,270]
tim.pensize(50)
tim.speed("fastest")

for _ in range(200)
    tim.colorr(color())
    tim.forward(30)
    tim.setheading(random.choice(directions))