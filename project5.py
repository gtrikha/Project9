'''
Gaurav Trikha
Project 5 Refactored (Single House)
'''

import turtle

def setup_turtle():
    """Sets up the turtle and screen."""
    t = turtle.Turtle()
    t.speed(0)
    screen = turtle.Screen()
    screen.title("Compact House Scene (Refactored)")
    screen.setup(width=600, height=600)
    screen.bgcolor("skyblue")
    return t, screen

def draw_rectangle(t, x, y, width, height, fill_color=None):
    """Draws a rectangle at the specified position."""
    jump_to(t, x, y)
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    if fill_color:
        t.end_fill()

def draw_triangle(t, x, y, size, fill_color=None):
    """Draws a triangle with its base centered at the specified x, y."""
    jump_to(t, x - size / 2, y)  # Adjust starting x to center base
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    for _ in range(3):
        t.forward(size)
        t.left(120)
    if fill_color:
        t.end_fill()

def draw_circle(t, x, y, radius, fill_color=None):
    """Draws a circle at the specified position."""
    jump_to(t, x, y - radius) # Adjust y to start drawing at the bottom
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    t.circle(radius)
    if fill_color:
        t.end_fill()

def jump_to(t, x, y):
    """Moves the turtle to the specified coordinates without drawing."""
    t.penup()
    t.goto(x, y)
    t.pendown()

def draw_house_base(t, x, y, width, height, color):
    """Draws the base of the house."""
    draw_rectangle(t, x, y, width, height, color)

def draw_house_roof(t, x, y, size, color):
    """Draws the roof of the house."""
    draw_triangle(t, x, y, size, color)

def draw_house_door(t, x, y, width, height, color):
    """Draws the door of the house."""
    draw_rectangle(t, x, y, width, height, color)

def draw_house_window(t, x, y, size, color):
    """Draws the left window of the house."""
    draw_rectangle(t, x, y, size, size, color)

def draw_sun(t, x, y, radius, color):
    """Draws the sun."""
    draw_circle(t, x, y, radius, color)

def draw_cloud(t, x, y, radius, color):
    """Draws the first cloud."""
    draw_circle(t, x, y, radius, color)

def draw_scene(t):
    """Draws the compact house scene using individual functions."""
    screen = t.getscreen()
    screen.setup(width=600, height=600)
    screen.bgcolor("skyblue")

    # House
    draw_house_base(t, -100, 0, 200, 300, "red")
    draw_house_roof(t, 0, 0, 250, "brown")
    draw_house_door(t, -40, -150, 75, 150, "yellow")
    draw_house_window(t, -75, -50, 50, "blue")
    draw_house_window(t, 25, -50, 50, "blue")

    # Sun
    draw_sun(t, 175, 150, 75, "yellow")

    # Clouds
    draw_cloud(t, -150, 150, 40, "white")
    draw_cloud(t, -175, 155, 40, "white")
    draw_cloud(t, -170, 170, 40, "white")
    draw_cloud(t, -200, 160, 40, "white")
    

def main():
    t, screen = setup_turtle()
    draw_scene(t)
    screen.mainloop()

if __name__ == "__main__":
    main()