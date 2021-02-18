from random import uniform, gauss
from turtle import Turtle, Screen
from statistics import mean, stdev
from altair import Data, Chart, Axis

# calculate pi

alex = Turtle()
wn = Screen()
wn.setworldcoordinates(-1, -1, 1, 1)
alex.tracer(12, 25)
alex.penup()
alex.setpos(0, -1)
alex.pendown()
alex.circle(1)
alex.penup()
alex.setpos(0, 0)

darts = 2000
red = 0

for _ in range(darts):
    x = uniform(-1, 1)
    y = uniform(-1, 1)
    alex.setpos(x, y)
    if alex.distance(0, 0) <= 1:
        red += 1
        alex.color("red")
        alex.dot()
    else:
        alex.color("blue")
        alex.dot()

ratio = red / darts
pie = ratio * 4
print(pie)

# predicting stock prices (Apple)
file = open("AAPL_train.csv", 'r')
lines = file.readlines()
header = lines[0]
field_names = header.strip().split(',')
lines2 = []
for row in lines[1:1001]:
    vals = row.strip().split(',')
    lines2.append(vals)
print(lines2[2][3])


x_vals = range(0, 1000)
y_vals = []
for line in lines2:
    y_vals.append(line[4])

data = Data(X=x_vals, Y=y_vals)
chart = Chart(data)
mark = chart.mark_point()
enc = mark.encode(x='X', y='Y')
enc.display()

file = open("AAPL_train.csv", 'r')
lines = file.readlines()
header = lines[0]
field_names = header.strip().split(',')
lines2 = []
for row in lines[1:1001]:
    vals = row.strip().split(',')
    lines2.append(vals)
print(lines2[2][3])

day_change = []
start_price = lines2[1][4]

for line in lines2:
    current_price = line[4]
    change = float(current_price) - float(start_price)
    day_change.append(change)
    start_price = line[4]

x_vals = range(0, 1000)
y_vals = []
for price in day_change:
    y_vals.append(price)

data = Data(X=x_vals, Y=y_vals)
chart = Chart(data)
mark = chart.mark_point()
enc = mark.encode(x='X', y='Y')
enc.display()

data = Data(change=day_change)
chart = Chart(data)
mark = chart.mark_bar()
X = Axis('change:Q', bin=True)
Y = Axis('count()')
enc = mark.encode(x=X, y=Y)
enc.display()

print(mean(day_change))
print(stdev(day_change))

# predictions
# print(lines2[999][4])
# 306.730011

change = 0
change_guess = []
start_price = 306.730011
worst = 0
best = 0
final_price_list = []

for _ in range(10000):
    for _ in range(250):
        change = gauss(0.215610008, 3.841395571073448)
        current_price = start_price + change
        change_guess.append(current_price)
        current_price = start_price
    final_price = change_guess[249]
    if final_price > best:
        best = final_price
    if final_price < worst:
        worst = final_price
    final_price_list.append(final_price)
print(best)
print(worst)

average = 0
average = mean(final_price_list)
print(average)
