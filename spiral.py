import turtle 

turtle.setup(700, 700, 200, 200)
basic_length = 5
for i in range(99):
    turtle.left(90)
    turtle.fd(basic_length)
    basic_length = basic_length + 5
input()
