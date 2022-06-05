from turtle import Turtle, Screen
from food import Food

RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270

class Snake:
    def __init__(self, color):
        self.segments = []                          
        self.color = color
        for i in range(0,-60,-20):                  # Create our snake as 3 turtles
            self.make_snake(self.color, i)
        self.head = self.segments[0]                # Our head of the snake will be important to check if we've eaten or crashed

    def make_snake(self, color, x_position=0, y_position=0):
        square = Turtle()
        square.penup()
        square.color(color)
        square.shape('square')
        square.setposition(x=x_position,y=y_position)
        self.segments.append(square)

    def move(self):
        for index in range(len(self.segments)-1, 0, -1):            # Replicating the movement of a catepillar, it is easier to move from 
            x_cor = self.segments[index-1].xcor()                   # the back to the front, replacing each segment by it's follower and then moving the head
            y_cor = self.segments[index-1].ycor()                   
            self.segments[index].goto(x_cor, y_cor)
        self.head.forward(20)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def get_coords(self):
        return self.head.pos()
    
    def add_square(self):
        square = Turtle()
        square.color(self.color)
        square.penup()
        square.shape('square')
        self.segments.append(square)

    def does_crash(self):
        (x, y) = self.get_coords()                          # Here we check to see if the head has ran into the body at any point

        for i in range(1, len(self.segments)):
            seg_x = self.segments[i].xcor()
            seg_y = self.segments[i].ycor()
            if (x <= seg_x + 10) and (x >= seg_x - 10) and (y >= seg_y - 10) and (y <= seg_y + 10):
                return True
        
        return False

    def does_eat(self, food):                               # We check to see if our snake has eaten a snack
        (snake_x, snake_y) = self.get_coords()
        food_x = food.xcor()
        food_y = food.ycor()

        if food_x - 15 < snake_x and snake_x < (food_x + 15) and food_y - 15 < snake_y and snake_y < food_y + 15:
            return True
        else:
            return False

    def is_out_of_bounds(self, screen_length):
        (x, y) = self.get_coords()
        bounds = screen_length / 2
        if x <= -bounds or x >= bounds or y <= -bounds or y >= bounds:
            return True
        return False
