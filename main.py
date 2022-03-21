import random
from turtle import Turtle, Screen

colours = ['lime', 'cyan', 'black', 'blue', 'red', 'yellow', 'indigo', 'orange red']

donny = Turtle()
donny.color("cyan")


def draw(n):
    angle = (360 / n)
    for _ in range(n):
        donny.fd(100)
        donny.rt(angle)


donny.lt(90)
donny.pu()
donny.fd(100)
donny.rt(90)
donny.pd()

for i in range(3, 11):
    donny.pencolor(random.choice(colours))
    draw(i)

screen = Screen()
screen.exitonclick()
