import turtle

tela = turtle.Screen()
tela.bgcolor("black")

borda = turtle.Turtle()
borda.penup()
borda.setposition(-375,-375) 
borda.pendown()
borda.pensize(3)
borda.color("white")
borda.hideturtle()

for side in range(4):
    borda.forward(750)
    borda.left(90)


turtle.register_shape("CenturiumEagleCima.gif")

jogador1 = turtle.Turtle()
jogador1.shape("CenturiumEagleCima.gif")
jogador1.penup()

speed = 1

def virarlt():
    jogador1.left(45)

def virarrt():
    jogador1.right(45)

def acelerar():
    global speed
    speed += 1

def desacelerar():
    global speed
    speed -= 1

turtle.onkey(virarlt, "Left")
turtle.onkey(virarrt, "Right")
turtle.onkey(acelerar, "Up")
turtle.onkey(desacelerar, "Down")
turtle.listen()

while True:
    jogador1.forward(speed)

    if jogador1.xcor() > 345 or jogador1.xcor() < -345:
        jogador1.right(180)

    if jogador1.ycor() > 345 or jogador1.ycor() < -345:
        jogador1.right(180)