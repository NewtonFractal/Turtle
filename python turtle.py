import turtle
shit = 1
while True:
    turtle.forward(15)
    turtle.left(10)
    shit += 1
    if shit > 10:
        shit += 1
        turtle.left(0)
        turtle.right(10)
        if shit > 30:
            turtle.right(0)
            turtle.left(10)
            shit += 1




