from turtle import Turtle

ALIGMENT = "center"
FONT = ("Arial", 24, "bold")

class Score(Turtle):

    def __init__(self, screensize, default_step):
        super.__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.teleport(x=0, y=(screensize/2)-default_step)  
        self.refresh_score()

    def increase_score():
        self.score += 1
        self.refresh_score()

    def refresh_score():
        self.clear()
        self.write(arg=f"SCORE: {self.score}",  align=ALIGMENT, font=FONT)
    
    def game_over():
        self.teleport(0,0)
        self.write(arg="GAME OVER",  align=ALIGMENT, font=FONT)
