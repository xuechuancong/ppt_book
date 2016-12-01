from turtle import Screen, Turtle
from time import sleep

boxsize = 200
caught = False
score = 0

window = Screen()
mouse = Turtle()
cat = Turtle()
mouse.penup()
cat.penup()
mouse.goto(100, 100)

def checkbound():
    global boxsize
    if mouse.xcor() > boxsize:
        mouse.goto(boxsize, mouse.ycor())
    if mouse.xcor() < -boxsize:
        mouse.goto(-boxsize, mouse.ycor())
    if mouse.ycor() > boxsize:
        mouse.goto(mouse.xcor(), boxsize)
    if mouse.ycor() < -boxsize:
        mouse.goto(mouse.xcor(), -boxsize)


def up():
    mouse.forward(10)
    checkbound()

def back():
    mouse.backward(10)
    checkbound()

def left():
    mouse.left(45)
    checkbound()

def right():
    mouse.right(45)
    checkbound()

def quitTurtles():
    window.bye()


window.onkeypress(up, "Up")
window.onkeypress(back, "Down")
window.onkeypress(left, "Left")
window.onkeypress(right, "Right")
window.onkeypress(quitTurtles, "Escape")

difficulty = window.numinput("Difficulty",
                             "Enter a difficulty from easy (1), for hard (5)",
                             minval=1, maxval=5)

window.listen()

while not caught:
    cat.setheading(cat.towards(mouse))
    cat.forward(8+difficulty)
    score = score+1
    if cat.distance(mouse) < 5:
        caught = True
    sleep(0.2 - difficulty * 0.01)

window.textinput("GAME OVER", "Well done. Your score:"
                 + str(score*difficulty))











