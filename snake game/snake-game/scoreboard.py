from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 15, 'normal')
ORIGIN = (0,0)

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = int(open("data.txt").read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Your current score is {self.score} and High Score is {self.high_score}", False, align = ALIGNMENT, font = FONT)

    def increase_the_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        if self.score > self.high_score:
            self.high_score = self.score
            open("data.txt", "w").write(str(self.high_score))
        self.goto(ORIGIN)
        self.write(f"GAME OVER\nFinal score: {self.score}", align=ALIGNMENT, font=FONT)

        # def reset(self):
    #     if self.score > self.high_score:
    #         self.high_score = self.score
    #         open("data.txt", "w").write(str(self.high_score))
    #     self.score = 0

        self.update_scoreboard()

