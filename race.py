import turtle
import random
import time

#players

p1 = turtle.Turtle()
p1.speed(10)
p2 = turtle.Turtle()
p2.speed(10)

p1.shape('turtle')
p2.shape('turtle')

p1.color('blue')
p2.color('red')

#bg screen

turtle.bgcolor('cyan')

#movement

p1.penup()
p1.goto(-400, 280)

p2.penup()
p2.goto(-400, -280)

p1.goto(400, -300)
p1.left(90)
p1.pendown()
p1.color('black')
p1.goto(400, 300)
p1.write('FINISH', font = "30")

p1.penup()
p1.color('blue')

p1.goto(-400, 280)
p1.right(90)
time.sleep(4)

p1.pendown()
p2.pendown()

p1.speed(3)
p2.speed(3)

dice = [1, 2, 3, 4, 5, 6]

for i in range(30):

    if p1.pos() >= (400, 300):

        p1.penup()
        p1.goto(0, 0)
        p1.write('PLAYER ONE WON!',font=1000)
        break

    elif p2.pos() >= (400, 300):
        p2.penup()
        p2.goto(0, 0)
        p2.write('PLAYER TWO WON!',font=1000)
        break

    else:

        dice_roll = random.choice(dice)

        p1.forward(dice_roll * 30)
        time.sleep(2)

        dice_roll2 = random.choice(dice)

        p2.forward(dice_roll2 * 30)
        time.sleep(2)


turtle.done()