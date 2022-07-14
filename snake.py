from turtle import Turtle

SNAKE_BONE_LENGTH = 20
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        """this is to create the main character snake itself."""
        for position in range(0, 3):
            self.add_segment()

    def add_segment(self):
        """this is to lengthen the snake after she ate the food."""
        x = 0
        snake_bone = Turtle()
        snake_bone.penup()
        snake_bone.shape("square")
        snake_bone.color("white")
        snake_bone.goto(x, y=0)
        self.snake_body.append(snake_bone)
        x -= SNAKE_BONE_LENGTH

    def move(self):
        for square in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[square - 1].xcor()
            new_y = self.snake_body[square - 1].ycor()
            self.snake_body[square].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
            
