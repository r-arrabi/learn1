import turtle
import colorsys

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create a turtle
t = turtle.Turtle()
t.speed(0)
t.width(2)

# Number of colors
n = 36
hue = 0

# Draw the pattern
for i in range(360):
    color = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
    t.pencolor(color)
    t.forward(i * 3 / n + i)
    t.left(59)
    hue += 1 / n

# Hide the turtle and display the window
t.hideturtle()
turtle.done()