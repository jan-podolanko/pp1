import turtle

def drawSquare(x,y,n):
    turtle.up()
    turtle.setposition(x,y)
    turtle.down()
    for i in range(1,5):
        turtle.forward(n)
        turtle.right(90)