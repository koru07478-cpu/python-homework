#3.
import turtle
import math


bob = turtle.Turtle()
print(bob)

def triangle(t: turtle.Turtle, side: float, apex_angle: float):
    """рисует треугольник данной черепашкой t, с данной боковой стороной side, и углом между боковыми сторонами apex_angle"""
    apex_angle_radians = math.radians(apex_angle)
    base = 2 * side * math.sin(apex_angle_radians / 2)
    base_angle = (180 - apex_angle) / 2
    
    t.forward(side)
    t.left(180-base_angle)
    t.forward(base)
    t.right(base_angle)
    t.forward(-side)
    t.left(180-apex_angle)
    
    
    

def NPiecePie(t: turtle.Turtle, side: float, n: int):
    """Рисует многоугольный пирог черепашкой t, со боковой стороной куска side, количеством кусков n"""
    t.left(-180+360/n)
    k=n
    while k!=0:
        k-=1
        t.right(-180+360/n)
        triangle(t, side, 360/n)
    
 
#5-угольный пирог
bob.penup()    
bob.left(180)          
bob.forward(200)
bob.pendown()
NPiecePie(bob, 100, 5)

#6-угольный пирог
bob.setheading(0)
bob.penup()     
bob.forward(200)
bob.pendown()
NPiecePie(bob, 100, 6)

#7-угольный пирог
bob.setheading(0)
bob.penup()     
bob.forward(200)
bob.pendown()
NPiecePie(bob, 100, 7)

turtle.mainloop()
