import turtle


def move(x, y, a=0):
    turtle.penup()
    turtle.setheading(a)
    turtle.goto(x-150, y)
    turtle.pendown()


# ㄱ
move(20, 100)
turtle.forward(40)
turtle.right(90)
turtle.forward(40)

# ㅣ
move(80, 100, -90)
turtle.forward(60)

# ㅁ
move(40, 40)
turtle.forward(40)
turtle.right(90)
turtle.forward(40)
turtle.right(90)
turtle.forward(40)
turtle.right(90)
turtle.forward(40)

# ㅌ
move(120, 80)
turtle.forward(40)
move(120, 60)
turtle.forward(40)
move(120, 40)
turtle.forward(40)
move(120, 80, -90)
turtle.forward(40)

# ㅐ
move(160, 60)
turtle.forward(20)
move(160, 100, -90)
turtle.forward(80)
move(180, 100, -90)
turtle.forward(80)

# ㅎ
move(240, 100)
turtle.forward(20)
move(220, 80)
turtle.forward(60)
move(250, 40)
turtle.circle(15)

# ㅕ
move(260, 60)
turtle.forward(20)
move(260, 40)
turtle.forward(20)
move(280, 100, -90)
turtle.forward(80)

# ㄴ
move(240, 20, -90)
turtle.forward(20)
turtle.left(90)
turtle.forward(40)

turtle.exitonclick()
