# coding: utf-8

import turtle

turtle.pensize(10)
turtle.pencolor("red")
turtle.speed(-1)
turtle.penup()
turtle.goto(-200, 0)
turtle.right(90)
turtle.pendown()

turtle.circle(100, 180)
turtle.left(180)
turtle.circle(100, 180)

turtle.circle(100, 180)
turtle.left(180)
turtle.circle(100, 180)


turtle.hideturtle()
turtle.down()
turtle.mainloop()