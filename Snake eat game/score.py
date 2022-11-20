from turtle import Turtle

FONT = ("Courier", 18, "normal")
class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("highscore.txt") as file:
            self.highscore = int(file.read())
        # self.highscore = 0
        self.color("white")
        self.penup()
        self.goto(x=0, y=270)
        self.show_score()
        self.hideturtle()

    def increase_score(self):
        self.score += 1
        self.show_score()

    def show_score(self):
        self.clear()
        self.write(f"Score = {self.score} High Score = {self.highscore}", False, "center", FONT)

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"Game Over", False, "center", FONT)

    def restart(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("highscore.txt", mode="w") as file:
                file.write(f"{self.highscore}")
        self.score = 0
        self.show_score()
