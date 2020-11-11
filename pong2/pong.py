import turtle

win = turtle.Screen()
win.title("Pong by tutorial")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0) # set max speed
paddle_a.shape("square") # by default 20px per 20px size
paddle_a.shapesize(stretch_wid=5, stretch_len=1) # change to 20x100px
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-350,0)

#  Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0) # set max speed
paddle_b.shape("square") # by default 20px per 20px size
paddle_b.shapesize(stretch_wid=5, stretch_len=1) # change to 20x100px
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(350,0)

# Ball
ball = turtle.Turtle()
ball.speed(0) # set max speed
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)

# Main game log
while True:
    win.update()
