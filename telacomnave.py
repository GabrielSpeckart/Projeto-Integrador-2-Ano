import turtle

tela = turtle.Screen()
tela.bgcolor("black")

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
    speed += 1

turtle.onkey(virarlt, "Left")
turtle.onkey(virarrt, "Right")
turtle.onkey(acelerar, "Up")
turtle.onkey(desacelerar, "Down")
turtle.listen()

while True:
    jogador1.forward(speed)