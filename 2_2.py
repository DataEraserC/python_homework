import turtle
for r in [10,20,40,80]:
    turtle.penup()
    turtle.goto(0,-r)
    turtle.pendown()
    turtle.circle(r)
input()
