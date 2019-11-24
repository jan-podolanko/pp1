import turtle

def drawSquare(x,y,n):
    turtle.up()
    turtle.setposition(x,y)
    turtle.down()
    for i in range(1,5):
        turtle.forward(n)
        turtle.right(90)
        
def drawCircle(x,y,r):
    turtle.up()
    turtle.setposition(x,y)
    turtle.down()
    turtle.circle(r)
    
def drawTriangle(x,y,m)
    turtle.up()
    turtle.setposition(x,y)
    turtle.down()
    