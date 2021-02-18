from turtle import Turtle, Screen
from math import pi

# triangle
n = float(input("Please enter a side length for the triangle."))

wn = Screen()
alex = Turtle()
for _ in range(3):
    alex.forward(n)
    alex.right(120)

# square
n = float(input("Please enter a side length for the triangle."))

wn = Screen()
alex = Turtle()
for _ in range(4):
    alex.forward(n)
    alex.right(90)

# octagon
n = float(input("Please enter a side length for the triangle."))

wn = Screen()
alex = Turtle()
for _ in range(8):
    alex.forward(n)
    alex.right(45)

# circle
n = input("Please enter a radius length for the circle.")
n = int(n)

wn = Screen()
alex = Turtle()
alex.penup()
alex.forward(n)
alex.right(90)
c = float(2) * pi * float(n)
d = int(c) / 360
alex.pendown()
for _ in range(360):
    alex.forward(d)
    alex.right(1)

# rainbow

n = input("Please enter a radius length for the rainbow.")
n = int(n)

wn = Screen()
alex = Turtle()
alex.speed(10)
alex.pensize(5)
# alex.stamp()
# alex.forward(-1*n)
# alex.forward(2*n)
alex.penup()
alex.forward(n)
alex.left(90)
c = float(2) * 3.14 * float(n)
d = int(c) / 360
alex.pendown()

alex.color("red")
for _ in range(180):
    alex.forward(d)
    alex.left(1)
alex.penup()
alex.left(90)
alex.forward(5)
alex.pendown()
n = n - 5
c = float(2) * 3.14 * float(n)
d = int(c) / 360
alex.left(90)

alex.color("orange")
for _ in range(180):
    alex.forward(d)
    alex.right(1)
alex.penup()
alex.right(90)
alex.forward(5)
alex.pendown()
n = n - 5
c = float(2) * 3.14 * float(n)
d = int(c) / 360
alex.right(90)

alex.color("yellow")
for _ in range(180):
    alex.forward(d)
    alex.left(1)
alex.penup()
alex.left(90)
alex.forward(5)
alex.pendown()
n = n - 5
c = float(2) * 3.14 * float(n)
d = int(c) / 360
alex.left(90)

alex.color("green")
for _ in range(180):
    alex.forward(d)
    alex.right(1)
alex.penup()
alex.right(90)
alex.forward(5)
alex.pendown()
n = n - 5
c = float(2) * 3.14 * float(n)
d = int(c) / 360
alex.right(90)

alex.color("blue")
for _ in range(180):
    alex.forward(d)
    alex.left(1)
alex.penup()
alex.left(90)
alex.forward(5)
alex.pendown()
n = n - 5
c = float(2) * 3.14 * float(n)
d = int(c) / 360
alex.left(90)

alex.color("purple")
for _ in range(180):
    alex.forward(d)
    alex.right(1)
alex.penup()
alex.right(90)
alex.forward(5)
alex.pendown()
n = n - 5
c = float(2) * 3.14 * float(n)
d = int(c) / 360
alex.right(90)
