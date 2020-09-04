import turtle


for i in range(0, 6):
    rowHeight = 100 * i
    turtle.penup()
    turtle.goto(0, rowHeight)
    turtle.pendown()
    turtle.forward(500)

turtle.left(90)

for i in range(0, 6):
    columnWidth = 100 * i
    turtle.penup()
    turtle.goto(columnWidth, 0)
    turtle.pendown()
    turtle.forward(500)



turtle.exitonclick()