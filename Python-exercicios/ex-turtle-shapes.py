import turtle as t
import random

colors = ['black','orange','green','purple','red','blue','yellow','violet','magenta','navy']
turtle = t.Turtle()

turtle.shape('turtle')
turtle.penup()
turtle.setpos((0,250))
turtle.pendown()


def shapes(sides):
    angulo = 360 / sides
    turtle.color(random.choice(colors))
    for side in range(sides):
        turtle.forward(200)
        turtle.right(angulo)
        
for lados in range(3,11):
    shapes(lados)

screen = t.Screen()
screen.exitonclick()