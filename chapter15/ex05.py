from chapter15.ex04 import *
import turtle
import math


def draw_rect(t: turtle.Turtle, rectangle: Rectangle) -> None:
    """Рисует прямоугольник rectangle: Rectangle черепашкой t: turtle.Turtle."""
    t.penup()
    t.forward(rectangle.corner.x)
    t.left(90)
    t.forward(rectangle.corner.y)
    t.pendown()

    t.forward(rectangle.height)
    t.right(90)
    t.forward(rectangle.width)
    t.right(90)
    t.forward(rectangle.height)
    t.right(90)
    t.forward(rectangle.width)


def draw_circle(t: turtle.Turtle, circle: Circle) -> None:
    """Рисует круг circle: Circle черепашкой t: turtle.Turtle."""
    t.penup()
    t.forward(circle.center.x + circle.radius)
    t.left(90)
    t.forward(circle.center.y)
    t.pendown()

    circle_length = 2 * math.pi * circle.radius
    n = int(circle_length / 3) + 1
    step_length = circle_length / n
    step_angle = 360 / n

    for i in range(n):
        t.forward(step_length)
        t.right(step_angle)


bob = turtle.Turtle()
bob.speed(0)
rect = create_rectangle(100, 100, 300, 250)
circ = create_circle(100, 100, 100)

draw_rect(bob, rect)
draw_circle(bob,circ)

turtle.mainloop()
