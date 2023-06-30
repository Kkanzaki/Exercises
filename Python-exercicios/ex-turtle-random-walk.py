import turtle as t
import random

colors = ['black', 'orange', 'green', 'purple', 'red', 'blue', 'yellow', 'violet', 'magenta', 'navy']
turtle = t.Turtle()
turtle.shape("classic")
turtle.shapesize(2, 2, 6)
turtle.pen(pensize=10, speed=5)
headings = [0, 90, 180, 270]
key = True

while key:
    turtle.color(random.choice(colors))
    turtle.forward(50)
    turtle.setheading(random.choice(headings))

screen = t.Screen()
screen.exitonclick()