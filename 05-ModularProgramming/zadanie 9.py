import shapes

x = 0
y = 0
for i in range(1,17):
    x += 50
    shapes.drawSquare(x,y,50)
    if x == 200:
        x = 0
        y += 50