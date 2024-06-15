from turtle import Turtle

class Score(Turtle):
    def __init__(self,name1,name2):
        super().__init__()
        self.name1 = name1
        self.name2 = name2
        self.color('Yellow')
        self.speed(0)
        self.penup()
        self.hideturtle()
        self.player_score = 0
        self.player_2_score = 0
        self.scoreboard()


    def scoreboard(self):
        self.goto(-100,200)
        self.write(arg=f"{self.name1}:"f"{self.player_score}",align="center",font=("Courier", 20, "normal"))
        self.goto(100,200)
        self.write(arg=f"{self.name2}:"f"{self.player_2_score}",align="center",font=("Courier", 20, "normal"))

    def playerscore(self):
        self.clear()
        self.player_score += 1
        self.scoreboard()

    def player2score(self):
        self.clear()
        self.player_2_score += 1
        self.scoreboard()

    def Player_win(self):
        self.penup()
        self.goto(0, 0)
        if self.player_score == 10 :
            self.write(arg=f"{self.name1} wins",align="center",font=("Courier", 20, "normal"))
            return False

    def Player_2_win(self):
        self.penup()
        self.goto(0, 0)
        if self.player_2_score == 10 :
            self.write(arg=f"{self.name2} wins",align="center",font=("Courier", 20, "normal"))
            return False