import turtle
import math

coordinate_list_x = []
coordinate_list_y = []

def Sierpinski(iterations):
    x = coordinate_list_x[-3]
    y = coordinate_list_y[-3]
    x = coordinate_list_x[-3]
    y = coordinate_list_y[-3]
    x = coordinate_list_x[-3]
    y = coordinate_list_y[-3]


def initial(iterations):
    x = 0
    y = 0
    coordinate_list_x.append(x)
    coordinate_list_y.append(y)
    turtle.setposition(x, y)
    x += (25 / 2)*iterations
    coordinate_list_x.append(x)
    y += (25 * math.sqrt(3) / 2) * iterations
    coordinate_list_y.append(y)
    turtle.setposition(x, y)
    x += (25 / 2) * iterations
    coordinate_list_x.append(x)
    y -= (25 * math.sqrt(3) / 2) *iterations
    coordinate_list_y.append(y)
    turtle.setposition(x, y)
    x = coordinate_list_x[-3]
    y = coordinate_list_y[-3]
    coordinate_list_y.append(y)
    coordinate_list_x.append(x)
    turtle.setposition(x, y)
    for z in range(0,1):
        x = coordinate_list_x[-4] +(coordinate_list_x[-3] - coordinate_list_x[-4])/2
        y = coordinate_list_y[-4] + (coordinate_list_y[-3] - coordinate_list_y[-4]) / 2
        coordinate_list_x.append(x)
        coordinate_list_y.append(y)
        turtle.setposition(x, y)
        x = coordinate_list_x[-4] +(coordinate_list_x[-3] - coordinate_list_x[-4])/2
        y = coordinate_list_y[-4] + (coordinate_list_y[-3] - coordinate_list_y[-4]) / 2
        coordinate_list_x.append(x)
        coordinate_list_y.append(y)
        turtle.setposition(x, y)
        x = coordinate_list_x[-4] +(coordinate_list_x[-3] - coordinate_list_x[-4])/2
        y = coordinate_list_y[-4] + (coordinate_list_y[-3] - coordinate_list_y[-4]) / 2
        coordinate_list_x.append(x)
        coordinate_list_y.append(y)
        turtle.setposition(x, y)
        x = coordinate_list_x[-3]
        y = coordinate_list_y[-3]
        turtle.setposition(x, y)
        Sierpinski(iterations)



initial(15)

print(coordinate_list_x)
print(coordinate_list_y)
