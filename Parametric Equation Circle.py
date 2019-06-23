import turtle
import math
r = 100
for t in range(1,1000):
    x = r*math.cos(t)/(math.pi)
    y = r*math.sin(t)/(math.pi)
    turtle.setposition(x,y)
