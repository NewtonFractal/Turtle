import turtle
import math
t = 1
r = 100
for t in range(1,1000):
    x = r*math.cos(t/math.pi)
    y = r*math.sin(t/math.pi)
    turtle.setposition(x,y)






