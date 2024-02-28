from turtle import Turtle

ALIGNMENT = "center"
FONT = ("arial", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.score = 0
        with open("data.txt", mode='r') as file:
            self.high_score = int(file.read())
        self.teleport(x=0, y=250)
        self.update_score()

    def restart(self):
        self.clear()
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_score()

    def increase_score(self):
        self.score += 1

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score = {self.high_score}", align=ALIGNMENT, font=FONT)
        with open("data.txt", mode='w') as file:
            file.write(str(self.high_score))

    # def game_over(self):
    #     self.teleport(x=0, y=0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)
