import turtle

def drawSquare(x,y,n):
    turtle.up()
    turtle.setposition(x,y)
    turtle.down()
    for i in range(1,5):
        turtle.forward(n)
        turtle.right(90)

drawSquare(50,50,50)

x = 0
y = 0
for i in range(1,17):
    x += 50
    drawSquare(x,y,50)
    if x == 200:
        x = 0
        y += 50