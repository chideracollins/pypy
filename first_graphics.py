import turtle
colors = ["red", "purple", "green", "blue", "orange"]
t = turtle.Turtle()
turtle.bgcolor("green")
for x in range(360):
    t.pencolor(colors[x%5])
    t.width(x//100 + 1)
    t.forward(x)
    t.left(59)

turtle.mainloop()
turtle.done()

