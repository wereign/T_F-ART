import random
import turtle
# import colorgram
# colors = colorgram.extract("dots.jpg", 10)
#
# rgb_colors = []
# for color in colors:
#     rgb_colors.append((color.rgb[0], color.rgb[1], color.rgb[2]))
#
# print(rgb_colors)
# for each new image. Does not need to run every time.

donny = turtle.Turtle()
turtle.colormode(255)

rgb_colors = [ (1, 12, 31),
              (53, 25, 17), (218, 127, 106), (10, 104, 159), (242, 213, 68), (149, 83, 39), (116, 255, 253),
               (116, 126, 253), (213, 131, 187)]
donny.pu()
for y in range(-250, 201, 50):
    for x in range(-250, 201, 50):
        donny.goto(x, y)
        donny.dot(20, random.choice(rgb_colors))
screen = turtle.Screen()
screen.exitonclick()

