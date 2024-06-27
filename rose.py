import random
import turtle

turtle.pensize(1)
turtle.speed(-1)
turtle.colormode(255)
turtle.bgcolor((0, 0, 0))

step = 0
i = 0
for i in range(300):
    i = i
    turtle.pencolor((random.randint(255, 255), random.randint(0, 255), random.randint(0, 255)))
    if i % 5 == 0:
        step += 1
    turtle.forward(i + step)
    turtle.left(70)

turtle.hideturtle()
turtle.down()
turtle.mainloop()