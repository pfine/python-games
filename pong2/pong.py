import turtle

# Window
win = turtle.Screen()
win.title("Pong by tutorial")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)  # set max speed
paddle_a.shape("square")  # by default 20px per 20px size
paddle_a.shapesize(stretch_wid=5, stretch_len=1)  # change to 20x100px
paddle_a.color("white")
paddle_a.penup()  # not draw line between moves
paddle_a.goto(-350, 0)

#  Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)  # set max speed
paddle_b.shape("square")  # by default 20px per 20px size
paddle_b.shapesize(stretch_wid=5, stretch_len=1)  # change to 20x100px
paddle_b.color("white")
paddle_b.penup()  # not draw line between moves
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)  # set max speed
ball.shape("square")
ball.color("white")
ball.penup()  # prevent dwowing line from 0,0
ball.goto(0, 0)
# add movement of the ball delat (change)- 2px at the time
ball.dx = 1/3
ball.dy = 1/3

# Pen
pen = turtle.Turtle()
pen.speed(0)  # animation speed: 0 - max
pen.color("white")
pen.penup()  # prevent dwowing line from 0,0
pen.hideturtle()  # hide , because we not need to see it
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center",
          font=("Courier", 24, "normal"))

# Score
score_a = 0
score_b = 0

# This approch not working, becaue function must be w/o params
#  turtle.onkeypress(fun, key=None)
#     Parameters:
#         fun – a function with no arguments or None
#         key – a string: key (e.g. “a”) or key-symbol (e.g. “space”)

# def paddleUp(paddleObj):
#     if not isinstance(paddleObj, turtle.Turtle):
#         print(' >>> ERROR: paddleObj must be turtle.Turtle object type !!!')
#         return
#     y = paddleObj.ycor()
#     y += 20  # add 20px up
#     paddleObj.sety(y)
#     print(' >>> LOG: move down')

# def paddleDown(paddleObj):
#     if not isinstance(paddleObj, turtle.Turtle):
#         print(' >>> ERROR: paddleObj must be turtle.Turtle object type !!!')
#         return
#     y = paddleObj.ycor()
#     y -= 20  # add 20px up
#     paddleObj.sety(y)
#     print(' >>> LOG: move down')

# win.listen()
# win.onkeypress(paddleUp(paddle_a), "q")
# win.onkeypress(paddleDown(paddle_a), "a")
# win.onkeypress(paddleUp(paddle_b), "p")
# win.onkeypress(paddleDown(paddle_b), "l")


def paddle_a_up():
    y = paddle_a.ycor()
    y += 20  # add 20px up
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20  # add 20px down
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20  # add 20px up
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20  # add 20px down
    paddle_b.sety(y)


# Keybord bindings
win.listen()
win.onkeypress(paddle_a_up, "q")
win.onkeypress(paddle_a_down, "a")
win.onkeypress(paddle_b_up, "Up")
win.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
    win.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    # top
    if ball.ycor() > 280:  # high screen = 300 - ball high = 20px
        ball.sety(280)
        ball.dy *= -1  # change to reverse
    # bottom
    if ball.ycor() < -280:  # high screen = -300 - ball high = 20px
        ball.sety(-280)
        ball.dy *= -1  # change to reverse
    # right
    if ball.xcor() > 420:
        ball.goto(0, 0)  # back to center
        ball.dx *= -1  # revers direction
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center",
                  font=("Courier", 24, "normal"))
    # left
    if ball.xcor() < -420:
        ball.goto(0, 0)  # back to center
        ball.dx *= -1  # revers direction
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center",
                  font=("Courier", 24, "normal"))

    # Paddle and ball collision
    # Paddle_B - paddle is on 350 and has 20px width and 100px hight
    if (ball.xcor() > 340 and ball.xcor() < 360) and \
            (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1
     # Paddle_A - paddle is on 350 and has 20px width and 100px hight
    if (ball.xcor() < -340 and ball.xcor() > -360) and \
            (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1

    # Score
    pen.clear()
    pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center",
              font=("Courier", 24, "normal"))
