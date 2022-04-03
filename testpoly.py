"""
testpoly.py
Illustrates the use of begin_poly, end_poly, and get_poly to
create custom turtle shapes.
"""

from turtle import *

def regularPolygon(length, numSides):
    """Draws a regular polygon.
    Arguments: the length and number of sides."""
    interiorAngle = 360 / numSides
    for count in range(numSides):
        forward(length)
        left(interiorAngle)

def makeShape(length, numSides, shapeName):
    """Creates and registers a new turtle shape with the given name.
    The shape is a regular polygon with the given length and number
    of sides.
    Arguments: the length, number of sides, and shape name."""
    up()
    goto(0, 0)
    setheading(0)
    begin_poly()
    #regularPolygon(length, numSides)
    end_poly()
    shape = get_poly()
    #addshape(shapeName, shape)
        
def main():
    """Creates two turtles with custom shapes and allows you
    to drag them around the window."""
    hideturtle()
    speed(0)
    makeShape(40, 5, "pentagon")
    makeShape(20, 8, "octagon")
    sleepy = Turtle(shape = "pentagon")
    sleepy.color("brown", "green")
    sleepy.up() 
    sleepy.goto(100, 50)
    sleepy.tilt(90)
    happy = Turtle(shape = "octagon")
    happy.color("blue", "pink")
    happy.up()
    sleepy.ondrag(lambda x, y: sleepy.goto(x, y))
    happy.ondrag(lambda x, y: happy.goto(x, y))
    listen()
    return "Done!"

if __name__ == '__main__':
    msg = main()
    print(msg)
    mainloop()
