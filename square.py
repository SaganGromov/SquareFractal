from turtle import Turtle, Screen
from math import *
import turtle
import random
import random
import time
win_width, win_height, bg_color = 1000, 550, 'white'
SPEED = 5000000
screen = Screen()
colors = ['yellow', 'gold', 'orange', 'red', 'maroon', 'violet', 'magenta', 'purple', 'navy', 'blue', 'skyblue', 'cyan',
 'turquoise', 'lightgreen', 'green', 'darkgreen', 'chocolate', 'brown', 'black', 'gray']

screen.setup(width = 1.0, height = 1.0)
screen.title("Fractal")


angle = 90
sides = 4
#size_of_side = 200
#diagonal = size_of_side*(2**(1/2))

class RectangleData():
    def __init__(self, start_position, size_of_side1, size_of_side2):
        self.mydata = {}
        self.start_position = start_position
        self.size_of_side1 = size_of_side1
        self.size_of_side2 = size_of_side2
        self.mydata['Rectangle'] = {}
        self.mydata['Rectangle']['Starting position'] = start_position
        self.mydata['Rectangle']['First side'] = size_of_side1
        self.mydata['Rectangle']['Second side'] = size_of_side2



class RectangleDrawn(Turtle):
    def __init__(self, start_position, size_of_side1, size_of_side2):
        super().__init__()
        self.hideturtle()
        self.recs = []
        a = start_position[0]
        b = start_position[1]
        self.speed(SPEED)
        self.next_positions = [(a,b), (a, b+size_of_side2/2), (a+size_of_side1/2, b), (a+size_of_side1/2, b+size_of_side2/2)]
        self.next_sides = [size_of_side1/2, size_of_side2/2]
        self.mycolor = random.choice(colors)
        self.color(self.mycolor)
        self.start_position = start_position
        self.size_of_side1 = size_of_side1
        self.size_of_side2 = size_of_side2
        self.diagonal = sqrt(size_of_side1** 2 + size_of_side2 ** 2)
        self.dangle = asin(size_of_side2 / self.diagonal)
        self.dangle*= 180/pi
        #self.hideturtle()
        self.penup()
        self.goto(start_position)
        self.pendown()
        for i in range(4):
            if i % 2 == 0:
                #time.sleep(1)
                self.forward(size_of_side1)
                self.left(90)
            else:
                #time.sleep(1)
                self.forward(size_of_side2)
                self.left(90)
    def drawsthelines(self):
        #time.sleep(1)
        self.hideturtle()
        x = self.start_position[0]
        y = self.start_position[1]
        self.goto(self.start_position)
        self.left(self.dangle)
        self.forward(self.diagonal)
        self.setheading(-self.dangle)
        self.penup()
        self.goto((x,y+self.size_of_side2))
        self.pendown()
        self.forward(self.diagonal)
        self.penup()
        self.goto((x,y+self.size_of_side2/2))
        self.setheading(0)
        self.pendown()
        self.forward(self.size_of_side1)
        self.penup()
        self.goto((x+self.size_of_side1/2, y+self.size_of_side2))
        self.pendown()
        self.setheading(270)
        self.forward(self.size_of_side2)
def draws_from_data(data):
    start = data['Rectangle']['Starting position']
    side_1 = data['Rectangle']['First side']
    side_2 = data['Rectangle']['Second side']
    sq = RectangleDrawn(start_position=start, size_of_side1=side_1, size_of_side2=side_2)
    sq.drawsthelines()
def turn_to_list(singledict):
    a = []
    counter = 0
    for i in singledict:
        a.append({f"{i}"[0:9]: singledict[i]})
    return a
def next_4(rectangle_data):
    recs = {}
    rectangle = rectangle_data['Rectangle']
    x_1 = rectangle['Starting position'][0]
    y_1 = rectangle['Starting position'][1]
    side_1 = rectangle['First side']
    side_2 = rectangle['Second side']
    f_1 = rectangle['Starting position']
    f_2 = (x_1 + side_1/2, y_1)
    f_3  =(x_1 + side_1/2, y_1 + side_2/2)
    f_4 = (x_1, y_1 + side_2/2)
    positions = [f_1, f_2, f_3, f_4]
    for i in positions:
        n = positions.index(i)+1
        recs[f"Rectangle {n}"] = {}
        recs[f"Rectangle {n}"]["Starting position"] = positions[n-1]
        recs[f"Rectangle {n}"]["First side"] = side_1/2
        recs[f"Rectangle {n}"]["Second side"] = side_2 / 2
    return turn_to_list(recs)
def allnext(work):
    a = []
    for i in work:
        a+=next_4(i)
    #print(len(a))
    return a
first_position = (-950,-450)
first_size1 = 1900
first_size2 = 900
rec1 = RectangleData(start_position=first_position, size_of_side1=first_size1, size_of_side2=first_size2)
data = rec1.mydata
print(data)
work = next_4(data)
print(f"Work: {work}")

def iterate(function, times, element):
    for i in range(times):
        element = function(element)
    return element
"""
myrecswillbe = iterate(allnext, 1, work)
for i in myrecswillbe:
    draws_from_data(i)
print(len(myrecswillbe))
"""
def iterations(number):
    #turtle.tracer(0, 0)
    work = next_4(data)
    if number == 0:
        draws_from_data(data)
    elif number == 1:
        draws_from_data(data)
        for i in work:
            draws_from_data(i)
    else:
        myrecswillbe = iterate(allnext, number-1, work)
        for i in myrecswillbe:
            draws_from_data(i)
    #turtle.update()
while True:
    a = 0
    while a < 24:
        iterations(a)
        time.sleep(0.0000000000000000005)
        #turtle.clearscreen()
        a+=1
"""
work = next_4(data)
print(work)
work = turn_to_list(work)
print(work)
print(next_4(work[0]))
draws_from_data(data)
"""
#sq = Rectangle(start_position=first_position, size_of_side1=first_size1, size_of_side2=first_size2)
"""
print(data)
new_recs = next_4(data)
L = []
for key, value in new_recs.items():
    print(key, value)
    L.append((key, value))
print(new_recs)
testing = turn_to_data(L[0])
print(next_4(testing))
c = 0
"""
"""
def next_ones(dict_of_rectangles):
    a = 0
    new_recs = {}
    for i in dict_of_rectangles:
        new_recs[f"Rectangle {a}"] = {}
        
print(next_4(sq))"""
#sq.draws()
"""
first_position = (-650,-350)
first_size1 = 1300
first_size2 = 700
sq = Rectangle(start_position=first_position, size_of_side1=first_size1, size_of_side2=first_size2)
sq.draws()
positions = tuple(sq.next_positions)
next_sides = tuple(sq.next_sides)
for i in positions:
    sq = Rectangle(start_position=i, size_of_side1=next_sides[0], size_of_side2=next_sides[1])
    sq.draws()
"""


"""
for i in positions:
    sq_j = Rectangle(start_position=i, size_of_side1=sq.next_sides[0], size_of_side2=sq.next_sides[1])
    print(sq_j.next_positions)
    sq_j.draws()
print(positions)
"""
#sq2 = Rectangle(start_position=(-650, 0), size_of_side1=650, size_of_side2=350)
#sq2.draws()
#sq3 = Rectangle(start_position=(-650,-350), size_of_side1=650, size_of_side2=)


turtle.mainloop()
