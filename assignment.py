"""import turtle
s = turtle.getscreen()
t= turtle.Turtle()
s.bgcolor("light blue")
t.color("brown")
t.penup()
t.goto(-300,-250)
t.pendown()
t.goto(-300,30) #tree left
t.goto(-325,37)
t.penup()
t.goto(-275,30)
t.pendown()
t.goto(-315,45)
t.penup()
t.goto(-200,-250)
t.pendown()
t.goto(-200,30)
t.goto(-170,90)
t.penup()
t.goto(-220,30)
t.pendown()
t.goto(-180,90)
t.goto(-183,100)
t.penup()
t.goto(-170,90) 
t.pendown()
t.goto(-173,100)
t.penup()
t.goto(-270,37)
t.pendown()
t.goto(-270,140)
t.penup()
t.goto(-260,37)
t.pendown()
t.goto(-260,110)
t.goto(-250,135)
t.penup()
t.goto(-265,110)
t.pendown()
t.goto(-255,135)
t.penup()
t.goto(-265,110)
t.pendown()
t.goto(-265,140)
t.penup()
t.goto(-230,25) 
t.pendown()
t.goto(-235,90)
t.penup()
t.goto(-219,17)
t.pendown()
t.goto(-215,120)
t.penup()
t.goto(-250,37)
t.pendown()
t.goto(-250,110)
t.penup()
t.goto(-240,35)
t.pendown()
t.goto(-238,134)
t.goto(-220,170)
t.penup()
t.goto(-243,134)
t.pendown()
t.goto(-225,170)
t.penup()
t.goto(-243,134)
t.pendown()
t.goto(-253,160)
t.penup()
t.goto(-260,165)
t.pendown()
t.goto(-250,134)
t.penup()
t.goto(100,0)

t.pendown()
t.pensize(10)
t.pencolor("red")
t.left(90)
t.circle(100,180)
t.right(270)

t.penup()
t.goto(101,-8)
t.pendown()
t.pencolor("orange")
t.left(90)
t.circle(105,185)
t.right(275)"""



import turtle
s = turtle.getscreen()
t= turtle.Turtle()

# background

t.penup()
t.goto(-300,-200)
t.pendown()
t.forward(600)
t.left(90)
t.forward(400)
t.left(90)
t.forward(600)
t.left(90)
t.forward(400)


#top circle
t.penup()
t.home()
t.penup()
t.goto(110,0)




#circle
t.penup()
t.home()
t.penup()
t.goto(110,0)

t.pendown()
t.fillcolor("blue")
t.begin_fill()
t.left(90)
t.circle(110,180)
t.circle(55,180)
t.circle(-55,180)
t.end_fill()  

t.penup()
t.goto(-110,0)
t.pendown()
t.fillcolor("red")
t.begin_fill()
t.circle(110,180)
t.circle(55,180)
t.circle(-55,180)
t.end_fill()



#left top

t.penup()
t.goto(-240,50)
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

"""
#inside circle
t.penup()
t.goto(110,0)
t.pendown()
t.fillcolor("blue")   
t.left(90)
t.begin_fill()
t.circle(55,180)
t.circle(-55,180)

t.penup()
t.goto(0,100)
t.pendown()"""

