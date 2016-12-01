
from turtle import *
window = Screen()
ba = Turtle()
ba.color('red', 'green')
ba.begin_fill()
while True:
    ba.forward(200)
    ba.left(170)
    if abs(ba.pos()) < 1:
        break
ba.end_fill()
window.exitonclick()
done()