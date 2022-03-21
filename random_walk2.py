import random
import turtle
from turtle import Turtle, Screen
colours = ['lime', 'cyan', 'black', 'blue', 'red', 'yellow', 'indigo', 'orange red']
colours2 = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
donny = Turtle()

turtle.colormode(255)
turtle.speed('fastest')


def right():
    donny.rt(90)
    donny.fd(50)


def left():
    donny.lt(90)
    donny.fd(50)


def straight():
    donny.fd(50)


def back():
    donny.bk(50)


donny.width(10)
movements = [left, right, straight, back]
for i in range(200):
    # donny.pencolor(random.choice(random.choice([colours, colours2])))
    # noinspection PyTypeChecker
    donny.pencolor(tuple(random.randint(0,255) for _ in range(3)))
    random.choice(movements)()


s = Screen()
s.exitonclick()