from turtle import Turtle
import random

class Food(Turtle):
     
    def __init__(self, screensize, default_step):
        super().__init__()
        self.screen_size = screensize
        self.step = default_step
        self.shape("circle")
        self.color("blue")
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.position_food()

    def position_food(self):
        food_x = self.step*random.randint(int(-1*(self.screen_size-self.step)/(2*self.step)), int((self.screen_size-self.step)/(2*self.step)))
        food_y = self.step*random.randint(int(-1*(self.screen_size-self.step)/(2*self.step)), int((self.screen_size-self.step)/(2*self.step)))
        self.teleport(x=food_x, y=food_y)
