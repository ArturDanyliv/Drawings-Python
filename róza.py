import turtle
import colorsys

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('black')
t.speed(0)
n=200
h=0
for i in range (360):
    c = colorsys.hls_to_rgb(h, 1, 0.8)
    h+= 1/n
    t.color(c)
    t.left(2)
    t.forward(i*2)
    t.right(150)
    for j in range (3):
        t.rt(2)
        t.forward(4)
        t.lt(150)