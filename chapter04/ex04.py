import turtle
import math

def arc(t: turtle.Turtle, radius: float, angle: float):
  """рисует дугу черепашкой t,радиусом radius и углом angle"""
    arc_length = 2 * math.pi * radius * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n
    
    for i in range(n):
        t.forward(step_length)
        t.left(step_angle)

def petal(t, radius, angle):
  """рисует лепесток черепашкой t, радиусом radius и углом angle"""
    arc(t, radius, angle)
    t.left(180 - angle)
    arc(t, radius, angle)
    t.left(180 - angle)

def flower(t, radius, angle, n):
  """рисует цветок черепашкой t, радиусом radius и углом angle лепестков, количество которых равно n"""
    for i in range(n):
        petal(t, radius, angle)
        t.left(360 / n)

bob = turtle.Turtle()
bob.speed(0)  #ускоряем

#7-лепетковый цветок
bob.penup()    
bob.left(180)          
bob.forward(300)
bob.pendown()
flower(bob, 150, 50, 7)

#10-лепестковый цветок
bob.setheading(0)
bob.penup()     
bob.forward(300)
bob.pendown()
flower(bob, 100, 70, 5)
bob.left(180)
flower(bob, 100, 70, 5)

#20- лепестковый цветок
bob.setheading(0)
bob.penup()     
bob.forward(300)
bob.pendown()
flower(bob, 600, 10, 20)


turtle.mainloop()
