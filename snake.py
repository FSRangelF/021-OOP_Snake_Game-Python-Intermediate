from turtle import Turtle
import random

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    
    def __init__(self, start_pos, default_step):
        self.start_position = start_pos
        self.step = default_step        
        self.snake_segments = []
        self.create_snake()
        self.head = self.snake_segments[0]
    
    def create_snake(self):
        for index in range(3):
            segment = Turtle(shape="square")
            segment.color("white")
            segment.penup()
            segment.setposition(self.start_position[index])
            self.snake_segments.append(segment)

    def move(self):
        for index in range (len(self.snake_segments)-1, 0, -1):
            new_position = self.snake_segments[index-1].position()
            self.snake_segments[index].setposition(new_position)
        self.head.forward(self.step)
            
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def increase_snake_size(self):
        segment = Turtle(shape="square")
        segment.color("white")
        segment.penup()
        segment.setposition(self.snake_segments[-1].pos())
        self.snake_segments.append(segment)
