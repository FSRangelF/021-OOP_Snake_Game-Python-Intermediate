from turtle import Turtle
import random

class Snake:
    
    def __init__(self, start_pos, default_step):
        self.start_position = start_pos
        self.step = default_step        
        self.snake_segments = []
        self.create_snake()
        self.head = self.snake_segments[0]
    
    def create_snake():
        for index in range(3):
            segment = Turtle(shape="square")
            segment.color("white")
            segment.penup()
            segment.setposition(self.start_position[index])
            self.snake_segments.append(segment)
            return

    def move(self):
        for index in range (len(self.snake_segments)-1, 0, -1):
        new_position = self.snake_segments[index-1].position()
        self.snake_segments[index].setposition(new_position)
        self.snake_segments[0].forward(self.step)
        return
    
    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
    
    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def increase_snake_size(self):
        segment = Turtle(shape="square")
        segment.color("white")
        segment.penup()
        segment.setposition(self.snake_segments[-1].pos())
        self.snake_segments.append(segment)
