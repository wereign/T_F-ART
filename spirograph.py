import random
import turtle
from turtle import Turtle, Screen
turtle.colormode(255)
turtle.speed('fastest')

donny = Turtle()


def random_color():
    r = random.choice(range(0, 255))
    g = random.choice(range(0, 255))
    b = random.choice(range(0, 255))
    return r, g, b


for i in range(1, 360, 20):
    donny.seth(i)
    donny.pencolor(random_color())
    donny.circle(100)


screen = Screen()
screen.exitonclick()




