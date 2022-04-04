"""
testcompound.py
Illustrates the use of begin_poly, end_poly, and get_poly to
create custom turtle shapes.
"""

from turtle import *

def makeRocketShape():
    """Creates and registers a new turtle shape for
    a rocket."""
    fusilage = ((0,0), (25, 0), (25, 10), (0, 10))
    noseCone = ((25, 0), (35, 5), (25, 10))
    fin1 = ((0, 10), (-5, 30), (10, 10))
    fin2 = ((0, 0), (-5, -20), (10, 0))
    shape = Shape("compound")
    shape.addcomponent(noseCone, "pink", "black")
    shape.addcomponent(fusilage, "red", "black")
    shape.addcomponent(fin1, "green", "black")
    shape.addcomponent(fin2, "green", "black")
    addshape("rocket", shape)
   '''     
def main():
    """Creates two turtles with custom shapes and allows you
    to drag them around the window."""
    hideturtle()
    speed(0)
    makeRocketShape()
    sleepy = Turtle(shape = "rocket")
    sleepy.up()
    sleepy.goto(100, 50)
    happy = Turtle(shape = "rocket")
    # Rotate the shape without changing the heading
    happy.tilt(90)
    happy.up()
    # Well, they don't detect the mouse drag events after all!
    sleepy.ondrag(lambda x, y: sleepy.goto(x, y))
    happy.ondrag(lambda x, y: happy.goto(x, y))
    listen()
    return "Done!"
'''
if __name__ == '__main__':
    msg = main()
    print(msg)
    mainloop()
