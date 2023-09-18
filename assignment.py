import turtle
s = turtle.getscreen()
t= turtle.Turtle()

# background

t.penup()
t.goto(-350,-230)
t.pendown()
t.forward(700)
t.left(90)
t.forward(460)
t.left(90)
t.forward(700)
t.left(90)
t.forward(460)






#circle
t.penup()
t.home()
t.penup()
t.goto(110,0)

t.pendown()
t.fillcolor("red")
t.begin_fill()
t.left(90)
t.circle(110,180)
t.circle(55,180)
t.circle(-55,180)
t.end_fill()  

t.penup()
t.goto(-110,0)
t.pendown()
t.fillcolor("blue")
t.begin_fill()
t.circle(110,180)
t.circle(55,180)
t.circle(-55,180)
t.end_fill()


#left top

t.penup()
t.goto(-240,70)
t.left(60)

t.pendown()
t.fillcolor("black")
t.begin_fill()
t.forward(30)
t.left(-90)
t.forward(130)
t.left(-90)
t.forward(30)
t.left(-90)
t.forward(130)
t.end_fill()

t.penup()
t.left(90)
t.forward(10)

t.pendown()
t.fillcolor("black")
t.begin_fill()
t.forward(30)
t.left(90)
t.forward(130)
t.left(90)
t.forward(30)
t.left(90)
t.forward(130)
t.left(90)
t.forward(30)
t.end_fill()

t.penup()
t.forward(10)

t.pendown()
t.fillcolor("black")
t.begin_fill()
t.forward(30)
t.left(90)
t.forward(130)
t.left(90)
t.forward(30)
t.left(90)
t.forward(130)
t.left(90)
t.forward(30)
t.end_fill()


#rigth top 마지막 밑
t.penup()
t.goto(240,70)
t.left(60)

t.pendown()
t.fillcolor("black")
t.begin_fill()
t.forward(30)
t.left(90)
t.forward(62.5)
t.left(90)
t.forward(30)
t.left(90)
t.forward(62.5)
t.end_fill()

# rigth top 마지막 위
t.penup()
t.left(90)
t.forward(30)
t.left(90)
t.forward(67.5) #위 아래 간격 5

t.pendown()
t.fillcolor("black")
t.begin_fill()
t.forward(62.5)
t.left(90)
t.forward(30)
t.left(90)
t.forward(62.5)
t.left(90)
t.forward(30)
t.end_fill()

#rigth top, 중간

t.penup()
t.left(90)
t.forward(62.5)
t.left(90)
t.forward(40)

t.pendown()
t.fillcolor("black")
t.begin_fill()
t.forward(30)
t.left(90)
t.forward(130)
t.left(90)
t.forward(30)
t.left(90)
t.forward(130)
t.end_fill()

#rigth top, 처음 위

t.penup()
t.left(90)
t.forward(40)

t.pendown()
t.fillcolor("black")
t.begin_fill()
t.forward(30)
t.left(90)
t.forward(62.5)
t.left(90)
t.forward(30)
t.left(90)
t.forward(62.5)
t.end_fill()

#rigth top, 처음 밑
t.penup()
t.left(90)
t.forward(30)
t.left(90)
t.forward(67.5)

t.pendown()
t.fillcolor("black")
t.begin_fill()
t.forward(62.5)
t.left(90)
t.forward(30)
t.left(90)
t.forward(62.5)
t.left(90)
t.forward(30)
t.end_fill()


#left top

t.penup()
t.goto(-240,-70)

t.pendown()
t.fillcolor("black")
t.begin_fill()
t.forward(30)
t.left(90)
t.forward(130)
t.left(90)
t.forward(30)
t.left(90)
t.forward(130)
t.end_fill()

t.penup()
t.left(270)
t.forward(10)

t.pendown()
t.fillcolor("black")
t.begin_fill()
t.forward(30)
t.right(90)
t.forward(62.5)
t.right(90)
t.forward(30)
t.right(90)
t.forward(62.5)
t.end_fill()

t.penup()
t.left(180)
t.forward(67.5)

t.pendown()
t.fillcolor("black")
t.begin_fill()
t.forward(62.5)
t.left(90)
t.forward(30)
t.left(90)
t.forward(62.5)
t.left(90)
t.forward(30)
t.end_fill()

t.penup()
t.left(180)
t.forward(30)
t.right(90)
t.forward(62.5)
t.left(90)
t.forward(10)

t.pendown()
t.fillcolor("black")
t.begin_fill()
t.forward(30)
t.left(90)
t.forward(130)
t.left(90)
t.forward(30)
t.left(90)
t.forward(130)
t.end_fill()



t.penup()
t.goto(240,-70)
t.left(30)

t.pendown()
t.fillcolor("black")
t.begin_fill()
t.forward(30)
t.right(90)
t.forward(62.5)
t.right(90)
t.forward(30)
t.right(90)
t.forward(62.5)
t.end_fill()

t.penup()
t.left(180)
t.forward(67.5)

t.pendown()
t.fillcolor("black")
t.begin_fill()
t.forward(62.5)
t.left(90)
t.forward(30)
t.left(90)
t.forward(62.5)
t.left(90)
t.forward(30)
t.end_fill()

t.penup()
t.forward(10)

t.pendown()
t.fillcolor("black")
t.begin_fill()
t.forward(30)
t.left(90)
t.forward(62.5)
t.left(90)
t.forward(30)
t.left(90)
t.forward(62.5)
t.end_fill()

t.penup()
t.forward(5)

t.pendown()
t.fillcolor("black")
t.begin_fill()
t.forward(62.5)
t.left(90)
t.forward(30)
t.left(90)
t.forward(62.5)
t.left(90)
t.forward(30)
t.end_fill()

t.penup()
t.left(180)
t.forward(40)

t.pendown()
t.fillcolor("black")
t.begin_fill()
t.forward(30)
t.right(90)
t.forward(62.5)
t.right(90)
t.forward(30)
t.right(90)
t.forward(62.5)
t.end_fill()

t.penup()
t.forward(10)

t.pendown()
t.fillcolor("black")
t.begin_fill()
t.forward(62.5)
t.right(90)
t.forward(30)
t.right(90)
t.forward(62.5)
t.right(90)
t.forward(30)
t.end_fill()


















