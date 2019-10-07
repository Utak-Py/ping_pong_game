# gui module
import turtle

win = turtle.Screen()
win.title("PingPong game")
win.bgcolor("grey")
win.setup(width=800, height=600)
win.tracer(0)

scoreA = 0
scoreB = 0
# paddlke 1

paddleA = turtle.Turtle()
paddleA.speed(0) #setting graphical speed
paddleA.shape("square")
paddleA.shapesize(stretch_wid=5, stretch_len=1)
paddleA.color("white")
paddleA.penup()
paddleA.goto(-350,0)


# paddlke 2
paddleB = turtle.Turtle()
paddleB.speed(0) #speed
paddleB.shape("square")
paddleB.shapesize(stretch_wid=5, stretch_len=1)
paddleB.color("white")
paddleB.penup()
paddleB.goto(350,0)

# ball

ball = turtle.Turtle()
ball.speed(0) #setting speed
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
#giving the ball y & x movements
ball.dx = 0.4
ball.dy = 0.4


#making a pen

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle() #we just wanna see the texr/score
pen.goto(0,260)
pen.write("Player A: {}     Player B: {} ".format(scoreA,scoreB), align="center", font=("Courier", 24, "bold"))

#functions for moving paddles using inpout

def paddle_a_Up():
    y = paddleA.ycor() #getting y cordinates to locate our paddle
    y += 20
    paddleA.sety(y) # set y value of paddle to the updated one

def paddle_a_Down():
    y = paddleA.ycor()  # getting y cordinates to locate our paddle
    y -= 20
    paddleA.sety(y)  # set y value of paddle to the updated one

#Keyboard binding
win.listen()  #tell program to listen for key board input
win.onkeypress(paddle_a_Up,"w") #when w is pressed activate the paddle_a_Up function
win.onkey(paddle_a_Down,"s")


def paddle_b_Up():
    y = paddleB.ycor() #getting y cordinates to locate our paddle
    y += 20
    paddleB.sety(y) # set y value of paddle to the updated one

def paddle_b_Down():
    y = paddleB.ycor()  # getting y cordinates to locate our paddle
    y -= 20
    paddleB.sety(y)  # set y value of paddle to the updated one

#Keyboard binding
win.listen()  #tell program to listen for key board input
win.onkeypress(paddle_b_Up,"8") #when w is pressed activate the paddle_a_Up function
win.onkey(paddle_b_Down,"2")

# getting that ball moving



# getting it to bounce off the paddles


# getting it to bounce off the walls


# gameLoop
while True:
    win.update()  # while the game is runnig keep refreshing the screen

    # in here while true we need the ball to move in the two dimentions
    ball.setx(ball.xcor()+ ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    #border Checking as in bounce on max y and max x

    if(ball.ycor()>290): # why 290 instead of 600 well because if the max range for y is 600 then we have -300 to 300
        ball.sety(290)# just a control feature
        ball.dx *= 1
        ball.dy *=-1

    if (ball.ycor() < -290):  # why 290 instead of 600 well because if the max range for y is 600 then we have -300 to 300
        ball.sety(-290)

        ball.dy *= -1

    if ball.xcor()>390:# so when ball exceeds horizontal limits reset it and change the direction
        ball.goto(0,0)
        ball.dx *= -1
        #add score to player 1
        scoreA +=1
        pen.clear()
        pen.write("Player A: {}     Player B: {} ".format(scoreA,scoreB), align="center", font=("Courier", 24, "bold"))

    if ball.xcor() < -390:  # so when ball exceeds horizontal limits reset it and change the direction
        ball.goto(0, 0)
        ball.dx *= -1
        # add score to player 2
        scoreB += 1
        pen.clear()
        pen.write("Player A: {}     Player B: {} ".format(scoreA,scoreB), align="center", font=("Courier", 24, "bold"))

    #todo trying to add paddle hit action
  #  if (ball.xcor() == paddleA.xcor() and ball.ycor()== paddleA.ycor()):
   #     ball.dx *= -1
    #    ball.dy *= -1

    if (ball.xcor()>340 and ball.xcor()<350) and (ball.ycor() < paddleB.ycor() + 50 and ball.ycor() > paddleB.ycor()-50):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor()<-340 and ball.xcor()>-350) and (ball.ycor() < paddleA.ycor() + 50 and ball.ycor() > paddleA.ycor()-50):
        ball.setx(-340)
        ball.dx *= -1


# for the scoring logic its simply if the ball touches the horizonta extremeties then award a point to player
