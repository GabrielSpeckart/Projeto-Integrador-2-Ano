import turtle

tela = turtle.Screen()
tela.bgcolor("black")

turtle.register_shape("CenturiumEagleCima.gif")

jogador1 = turtle.Turtle()
jogador1.shape("CenturiumEagleCima.gif")
jogador1.penup()

speed = 1

def turnlt():
    jogador1.left(45)

def turnrt():
    jogador1.right(45)

turtle.onkey(turnlt, "Left")
turtle.onkey(turnrt, "Right")
turtle.listen()

while True:
    jogador1.forward(speed)