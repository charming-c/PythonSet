from turtle import *

turtle = Turtle()
turtle.speed(100)

# color = ("white", "#057748")

# turtle.shape('turtle')
turtle.width(2.5)
turtle.color("#057748")
turtle.circle(120, 360)

# 外面两个大圈圈
turtle.setheading(90)
turtle.penup()
turtle.forward(5)
turtle.pendown()
turtle.setheading(0)
turtle.width(1)
turtle.circle(115, 360)

# 里面的小圈
turtle.penup()
turtle.setheading(90)
turtle.forward(38)
turtle.pendown()
turtle.setheading(0)
# turtle.begin_fill()
# turtle.fillcolor("#057748")
turtle.circle(76, 360)
# turtle.end_fill()

# 大字
turtle.setheading(90)
turtle.penup()
turtle.forward(40)
turtle.pendown()

x = turtle.xcor()
y = turtle.ycor()
turtle2 = Turtle()
turtle2.speed(100)
turtle2.penup()
turtle2.setx(x)
turtle2.sety(y)
turtle2.pendown()

turtle.setheading(90)
# turtle2.setheading(90)

turtle.width(10)
turtle2.width(10)

#turtle.color = turtle2.color = ('255', '255', '255')
turtle.fillcolor('white')
turtle2.fillcolor("white")
turtle.forward(20)

# turtle.end_fill()
# turtle2.forward(20)

turtle.setheading(180)
turtle.forward(34.6)
turtle.setheading(270)
turtle.forward(10)
# turtle.begin_fill()
turtle.fillcolor("#057748")
turtle.penup()
turtle.goto(x, y+34.6-15)
turtle.pendown()
turtle.setheading(0)
turtle.forward(34.6)
turtle.setheading(270)
turtle.forward(10)

turtle2.setheading(210)
turtle2.color("#057748")
turtle2.forward(40)
turtle2.color("#057748")
turtle2.penup()
turtle2.goto(x, y)
turtle2.pendown()
turtle2.setheading(330)
turtle2.forward(40)

turtle2.setheading(90)
turtle2.penup()
turtle2.goto(x, y)
turtle2.pendown()
turtle2.forward(25)

# turtle.fillcolor('white')

turtle.setheading(90)
turtle.penup()
turtle.goto(x, y-40+76)
turtle.pendown()

turtle2.setheading(90)
turtle2.penup()
turtle2.goto(x, y-40+76)
turtle2.pendown()

turtle.forward(50)
turtle2.penup()
turtle2.goto(x-34.6, y-40+76 + 10)
turtle2.pendown()
turtle2.setheading(0)
turtle2.forward(69.2)

turtle2.penup()
turtle2.goto(x-34.6, y-40+76 + 22)
turtle2.pendown()
turtle2.setheading(0)
turtle2.forward(69.2)

# turtle2.width(10)
turtle2.penup()
turtle2.goto(x-34.6, y-40+76 + 32)
turtle2.pendown()
turtle2.setheading(15)
turtle2.forward(17)
turtle2.setheading(360-15)
turtle2.forward(17)

turtle2.penup()
turtle2.goto(x-34.6, y-40+76 + 45)
turtle2.pendown()
turtle2.setheading(15)
turtle2.forward(17)
turtle2.setheading(360-15)
turtle2.forward(17)

turtle2.penup()
turtle2.goto(x, y-40+76 + 32)
turtle2.pendown()
turtle2.setheading(15)
turtle2.forward(17)
turtle2.setheading(360-15)
turtle2.forward(17)

turtle2.penup()
turtle2.goto(x, y-40+76 + 45)
turtle2.pendown()
turtle2.setheading(15)
turtle2.forward(17)
turtle2.setheading(360-15)
turtle2.forward(17)

turtle.width(8)
turtle.penup()
turtle.goto(x-34.6, y-40+76 + 60)
turtle.pendown()

turtle.setheading(270)
turtle.forward(3)
turtle.setheading(0)
turtle.forward(30)
turtle.setheading(90)
turtle.forward(3)

turtle.penup()
turtle.goto(x-17.3, y-40+76 + 60)
turtle.pendown()
turtle.setheading(270)
turtle.forward(3)
turtle.width(8)
turtle.penup()
turtle.goto(x, y-40+76 + 60)
turtle.pendown()

turtle.setheading(270)
turtle.forward(3)
turtle.setheading(0)
turtle.forward(30)
turtle.setheading(90)
turtle.forward(3)

turtle.penup()
turtle.goto(x+17.3, y-40+76 + 60)
turtle.pendown()
turtle.setheading(270)
turtle.forward(3)

turtle.penup()
turtle.goto(x, y-76)
turtle.pendown()

s = f"CENTRAL CHINA NOMAL UNIVERSITY"
count = 0
turtle.width(100)
for c in s:
    turtle.penup()
    turtle.goto(x, y+36)
    turtle.setheading(-180 + (6.2*count))
    turtle.forward(100)
    turtle.write(c, move=True, align='center', font=("微软雅黑", 15, "normal"))
    turtle.pendown()
    count += 1

str = "华 中 师 范 大 学"
count = 1
for c in str:
    turtle.penup()
    turtle.goto(x, y+36)
    turtle.setheading(170 - (13.8*count))
    turtle.forward(98)
    turtle.write(c, move=True, align='center', font=("微软雅黑", 15, "normal"))
    turtle.pendown()
    count += 1
