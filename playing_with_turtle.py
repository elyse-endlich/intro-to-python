from turtle import Turtle, Screen

dir(turtle)

wn = Screen()
wn.bgcolor("lightgreen")
ryan = Turtle()
ryan.speed(10)
ryan.color('gray')
for _ in range(3):
    ryan.forward(50)
    ryan.right(120)
ryan.color("red")
for _ in range(4):
    ryan.forward(50)
    ryan.right(90)
ryan.color("yellow")
for _ in range(5):
    ryan.forward(50)
    ryan.right(72)
ryan.color("blue")
for _ in range(6):
    ryan.forward(50)
    ryan.right(60)
ryan.color('orange')
for _ in range(7):
    ryan.forward(50)
    ryan.right(51.4285714)
ryan.color('green')
for _ in range(8):
    ryan.forward(50)
    ryan.right(45)
ryan.color('pink')
for _ in range(9):
    ryan.forward(50)
    ryan.right(40)
ryan.color('white')
for _ in range(10):
    ryan.forward(50)
    ryan.right(36)
ryan.up()
ryan.forward(25)
ryan.down()
ryan.color('black')
for _ in range(360):
    ryan.forward(1.45)
    ryan.right(1)
