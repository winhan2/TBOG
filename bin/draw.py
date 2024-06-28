# coding: utf-8

import turtle
import random

def draw(num, angle, step_a, colormode, bg):
    turtle.pensize(1)
    turtle.speed(-1)
    turtle.colormode(255)
    turtle.bgcolor(bg)
    turtle.pendown()

    try:
        step = 0
        for i in range(num):
            i = i
            turtle.pencolor((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) if colormode == 'rand' else colormode)
            if i % step_a == 0:
                step += 1
            turtle.forward(i + step)
            turtle.left(angle)

    except turtle.Terminator:
        pass
    turtle.hideturtle()
    turtle.penup()
    turtle.home()
    turtle.down()
    turtle.mainloop()


if __name__ == '__main__':
    draw(200, 70, 5, 'rand')