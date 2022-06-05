from turtle import Turtle, Screen
import random

screen = Screen()
screen.colormode(255)


class Food(Turtle):
    def __init__(self, screen_length):
        super().__init__()
        self.penup()
        self.shape('square')
        self.set_color()
        self.set_coords(screen_length)

    def set_color(self):                                    # Our food should be random colors for fun :)
        r = random.randint(1,255)
        g = random.randint(1,255)
        b = random.randint(1,255)
        self.color(r, g, b)

    def set_coords(self, screen_length):                    # Set our food at a random location
        adjusted_length = screen_length/2 - 10

        x_cor = random.randint(-adjusted_length, adjusted_length)
        y_cor = random.randint(-adjusted_length, adjusted_length)

        self.goto(x=x_cor, y=y_cor)

