from turtle import Turtle

ALIGMENT = "center"
FONT = ("Courier", 24, "bold")

class Score(Turtle):

    def __init__(self, screensize, default_step):
        super().__init__()
        self.score = 0
        self.hi_score = 0
        self.color("white")
        self.hideturtle()
        self.teleport(x=0, y=(screensize/2)-2*default_step)  
        self.check_hi_score()
        self.refresh_score()

    def increase_score(self):
        self.score += 1
        if self.score > self.hi_score:
            self.hi_score = self.score
            self.update_hi_score()
        self.refresh_score()

    def refresh_score(self):
        self.clear()
        self.write(arg=f"SCORE: {self.score}         HI-SCORE: {self.hi_score}",  align=ALIGMENT, font=FONT)
    
    def game_over(self):
        self.teleport(0,0)
        self.write(arg="GAME OVER",  align=ALIGMENT, font=FONT)

    def check_hi_score(self):
        with open("hi_score.txt") as file:
            self.hi_score = int(file.read())

    def update_hi_score(self):
        with open("hi_score.txt", 'w') as file:
            file.write(f'{self.hi_score}')
