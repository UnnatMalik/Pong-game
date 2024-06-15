from turtle import Turtle,Screen
from player_padle import padle
from ball import Ball
from score import Score
import time

t = Turtle()

class Start(Turtle):
    def __init__(self):
        super().__init__()
        self.color("Yellow")
        self.hideturtle()
        self.goto(0,0)
    def start(self):
        self.write(arg="Start the game",align="center",font=("Courier", 30, "normal"))
        

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("⚽Pong-Game⚽")
red_team = screen.textinput("Red team", "Enter your name ")
blue_team = screen.textinput("Blue team", "Enter your name ")
screen.listen()
screen.tracer(0)

player = padle((350,0),"Red")
player_2 = padle((-350,0),"Blue")

screen.onkeypress(player.up,"Up")
screen.onkeypress(player.down,"Down")
screen.onkeypress(player_2.up,"w")
screen.onkeypress(player_2.down,"s")


score = Score(blue_team,red_team)
game_start = Start()
game_on = True

start = True
while game_on == True :
    if start == True :
        game_start.start()
        screen.update()
        game_start.clear()
        time.sleep(2)
        start = False
        ball = Ball()
        t.shape("square")
        t.color("White")
        t.shapesize(30,1)
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280 :
        ball.bounce()
    if ball.distance(player) < 50 and ball.xcor() > 320 or ball.distance(player_2) < 50 and ball.xcor() < -320  :
        ball.serve()
    if ball.xcor() > 380 :
        score.playerscore()
        if score.Player_win() == False :
            game_on = False
        ball.game_over()
    if ball.xcor() < -380 :
        score.player2score()
        if score.Player_2_win() == False :
            game_on = False
        ball.game_over()
screen.exitonclick()