import turtle
from math import sqrt

basic_length = 100

t1 = turtle.Pen()
t1.goto(0, 0)
t1.penup()
t1.seth(180)
t1.fd(basic_length / 3 * sqrt(3))
t1.pendown()

t1.seth(30)
for i in range(3):
    t1.fd(basic_length)
    t1.right(120)
t1.hideturtle()

t2 = turtle.Pen()
t2.goto(0, 0)
t2.penup()
t2.seth(0)
t2.fd(basic_length / 3 * sqrt(3))
t2.pendown()

t2.seth(150)
for i in range(3):
    t2.fd(basic_length)
    t2.left(120)
t2.hideturtle()
input()
