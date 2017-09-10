"""
This module lets you practice one form of the ACCUMULATOR pattern,
namely, the "IN GRAPHICS" form which features:
  -- DRAWING OBJECTS via ACCUMULATING positions and/or sizes,
     as in:   x = x + pixels

Additionally, it emphasizes that you must
  ** DO A CONCRETE EXAMPLE BY HAND **
before you can implement a solution to the problem in Python. 
  
Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Joshua Osborne.
"""  # Done: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg
import math

# ----------------------------------------------------------------------
# Students: As you work each of these problems, ask yourself:
#   1. Do I need a loop?
#      If so, HOW MANY LOOPS?
#
#   2. Where I need a loop, what needs to happen:
#        -- BEFORE the loop?
#        -- IN the loop?
#        -- AFTER the loop?
# ----------------------------------------------------------------------
def main():
    """ Calls the   TEST   functions in this module. """
    # test_draw_squares_from_circle()
    # test_draw_circles_from_rectangle()
    test_draw_lines_from_rectangles()


def test_draw_squares_from_circle():
    """ Tests the   draw_squares_from_circle  function. """
    print()
    print('--------------------------------------------------')
    print('Testing the  draw_squares_from_circle  function:')
    print('  See the graphics windows that pop up.')
    print('--------------------------------------------------')

    # ------------------------------------------------------------------
    # TWO tests on ONE window.
    # ------------------------------------------------------------------
    title = 'Tests 1 and 2 of DRAW_SQUARES_FROM_CIRCLE: '
    title = title + ' 7 little squares from green circle, 4 big squares'
    window1 = rg.RoseWindow(650, 350, title)

    # Test 1:
    circle = rg.Circle(rg.Point(100, 100), 20)
    circle.fill_color = 'green'
    draw_squares_from_circle(7, circle, window1)

    # Test 2:
    circle = rg.Circle(rg.Point(350, 70), 50)
    draw_squares_from_circle(4, circle, window1)
    window1.close_on_mouse_click()

    # ------------------------------------------------------------------
    # A third test on ANOTHER window.
    # ------------------------------------------------------------------
    title = 'Test 3 of DRAW_SQUARES_FROM_CIRCLE: '
    title += ' 20 teeny squares from blue circle!'
    window2 = rg.RoseWindow(525, 300, title)

    # Test 3:
    circle = rg.Circle(rg.Point(50, 50), 10)
    circle.fill_color = 'blue'
    draw_squares_from_circle(20, circle, window2)

    window2.close_on_mouse_click()


def draw_squares_from_circle(n, circle, window):
    """
    What comes in:  Three arguments:
      -- A positive integer n.
      -- An rg.Circle.
      -- An rg.RoseWindow.
    What goes out:  Nothing (i.e., None).
    Side effects:
      See   draw_squares_from_circle.pdf   in this project for pictures
        that may help you better understand the following specification:

      First draws the given rg.Circle on the given rg.RoseWindow.
      Then draws  n  rg.Squares on the given rg.RoseWindow, such that:
        -- The first rg.Square circumscribes the given rg.Circle.
        -- Each subsequent rg.Square has its upper-left quarter
             on top of the lower-right quarter of the previous rg.Square,
             so that the squares form an overlapping sequence
             that goes down and to the right.
      Must  ** render **     but   ** NOT close **   the window.

    Type hints:
      :type n: int
      :type circle: rg.Circle
      :type window: rg.RoseWindow
    """
    # ------------------------------------------------------------------
    # Done: 2. Implement and test this function.
    #          Tests have been written for you (above).
    #
    # CONSIDER using the ACCUMULATOR IN GRAPHICS pattern,
    #             as in   draw_row_of_circles   in m1e,
    #             instead of directly using the loop variable.
    #
    ####################################################################
    # HINT: To figure out the code that computes the necessary
    #       positions of each square,
    #          ** FIRST DO A CONCRETE EXAMPLE BY HAND! **
    ####################################################################
    # ------------------------------------------------------------------
    x = circle.center.x
    y = circle.center.y
    for k in range(n):
        square_center = rg.Point(x+k*circle.radius,y+k*circle.radius)
        square = rg.Square(square_center, 2*circle.radius)
        square.attach_to(window)
        circle.attach_to(window)



    window.render()

def test_draw_circles_from_rectangle():
    """ Tests the   draw_circles_from_rectangle  function. """
    print()
    print('--------------------------------------------------')
    print('Testing the  draw_circles_from_rectangle  function:')
    print('  See the graphics windows that pop up.')
    print('--------------------------------------------------')

    # ------------------------------------------------------------------
    # Done: 3. Implement this TEST function.
    #   It TESTS the  draw_circles_from_rectangle  function
    #   defined below.  Include at least **   3   ** tests, of which
    #      ***  at least TWO tests are on ONE window and
    #      ***  at least ONE test is on a DIFFERENT window.
    #
    ####################################################################
    # HINT: Consider using the same test cases as suggested by the
    #   pictures in  draw_circles_from_rectangle.pdf   in this project.
    #   Follow the same form as the example in a previous problem.
    ####################################################################
    # ------------------------------------------------------------------

    #Test 1
    window1 = rg.RoseWindow(720,500,'Circles from Rectangle Test 1 and 2')
    corner_p1 = rg.Point(400, 250)
    corner_p2 = rg.Point(440, 325)
    rectangle_1 = rg.Rectangle(corner_p1,corner_p2)
    draw_circles_from_rectangle(4,5,rectangle_1,window1, 'purple', 'magenta')

    #Test 2
    corner_p1_2 = rg.Point(600,400)
    corner_p2_2 = rg.Point(500,450)
    rectangle_2 = rg.Rectangle(corner_p1_2, corner_p2_2)
    draw_circles_from_rectangle(8,3,rectangle_2,window1, 'red','blue')

    #Test 3
    window2 = rg.RoseWindow(720,500,'Circles from Rectangle Test 3')
    corner_p1_3 = rg.Point(350, 280)
    corner_p2_3 = rg.Point(375, 330)
    rectangle_3 = rg.Rectangle(corner_p1_3, corner_p2_3)
    draw_circles_from_rectangle(6, 10, rectangle_3, window2, 'orange', 'lightblue')

    window1.close_on_mouse_click()
    window2.close_on_mouse_click()


def draw_circles_from_rectangle(m, n, rectangle, window, recFill, recOut):
    """
    What comes in:  Four arguments:
      -- Positive integers m and n.
      -- An rg.Rectangle.
      -- An rg.RoseWindow.
    What goes out:  Nothing (i.e., None).
    Side effects:
      See   draw_circles_from_rectangle.pdf   in this project for pictures
        that may help you better understand the following specification:

      First draws the given rg.Rectangle on the given rg.RoseWindow.
      Then draws  m  rg.Circles on the given rg.RoseWindow, such that:
        -- The diameter of each rg.Circle is the same as the height
             of the given rg.Rectangle.
        -- The first rg.Circle is immediately to the left of the
             given rg.Rectangle
        -- Each subsequent rg.Circle is immediately to the left
             of the previous rg.Circle, so that the circles form a row
             that goes to the left.
        -- Each rg. Circle has the same fill_color as the given
             rg.Rectangle (and has no outline_color).
      Then draws  n  rg.Circles on the given RoseWindow, such that:
        -- The diameter of each rg.Circle is the same as the width
             of the given rg.Rectangle.
        -- The first rg.Circle is immediately above the
             given rg.Rectangle
        -- Each subsequent rg.Circle is immediately above the previous
             rg.Circle, so that the circles form a column that goes up.
        -- Each rg.Circle has the same outline_color as the given
             rg.Rectangle (and has no fill_color).
      Must  ** render **     but   ** NOT close **   the window.

    Type hints:
      :type m: int
      :type n: int
      :type rectangle: rg.Rectangle
      :type window: rg.RoseWindow
    """
    # ------------------------------------------------------------------
    # Done: 4. Implement and test this function.
    #          Tests have been written for you (above).
    #
    # CONSIDER using the ACCUMULATOR IN GRAPHICS pattern,
    #             as in   draw_row_of_circles   in m1e,
    #             instead of directly using the loop variable.
    #
    ####################################################################
    # HINT: To figure out the code that computes the necessary
    #       positions of each circle,
    #          ** FIRST DO A CONCRETE EXAMPLE BY HAND! **
    ####################################################################
    # ------------------------------------------------------------------
    recWidth = float(rectangle.get_width())
    recHeight = float(rectangle.get_height())

    for k in range(m):
        circle_pos = rg.Point(rectangle.get_center().x - (recWidth/2 + recHeight/2 + (k*recHeight)),rectangle.get_center().y)
        circle = rg.Circle(circle_pos, recHeight/2)
        circle.fill_color = recFill
        circle.attach_to(window)

    for j in range(n):
        circle_pos = rg.Point(rectangle.get_center().x,rectangle.get_center().y - (recHeight / 2 + recWidth / 2 + (j * recWidth)))
        circle = rg.Circle(circle_pos, recWidth/2)
        circle.outline_color = recOut
        circle.attach_to(window)

    rectangle.outline_color = recOut
    rectangle.fill_color = recFill
    rectangle.attach_to(window)
    window.render()


def test_draw_lines_from_rectangles():
    """ Tests the   draw_lines_from_rectangles  function. """
    print()
    print('--------------------------------------------------')
    print('Testing the  draw_lines_from_rectangles  function:')
    print('  See the graphics windows that pop up.')
    print('--------------------------------------------------')

    # TWO tests on ONE window.
    title = 'Tests 1 & 2 of DRAW_LINES_FROM_RECTANGLES:'
    title += '  5 lines, 8 lines!'
    window1 = rg.RoseWindow(900, 400, title)

    rectangle1 = rg.Rectangle(rg.Point(100, 25), rg.Point(150, 125))
    rectangle2 = rg.Rectangle(rg.Point(300, 150), rg.Point(400, 175))
    rectangle1.outline_color = 'red'
    rectangle2.outline_color = 'blue'
    draw_lines_from_rectangles(rectangle1, rectangle2, 5, window1,'blue','red')

    rectangle1 = rg.Rectangle(rg.Point(870, 30), rg.Point(750, 100))
    rectangle2 = rg.Rectangle(rg.Point(700, 90), rg.Point(650, 60))
    rectangle2.outline_color = 'green'
    draw_lines_from_rectangles(rectangle1, rectangle2, 8, window1,'lightblue','purple')

    window1.close_on_mouse_click()

    # A third test on ANOTHER window.
    title = 'Test 3 of DRAW_LINES_FROM_RECTANGLES:  11 lines!'
    window2 = rg.RoseWindow(700, 700, title)

    rectangle1 = rg.Rectangle(rg.Point(550, 200), rg.Point(650, 100))
    rectangle2 = rg.Rectangle(rg.Point(600, 50), rg.Point(650, 75))
    rectangle1.outline_color = 'brown'
    rectangle2.outline_color = 'cyan'
    rectangle2.outline_thickness = 10
    draw_lines_from_rectangles(rectangle1, rectangle2, 11, window2,'white','grape')

    window2.close_on_mouse_click()


def draw_lines_from_rectangles(rectangle1, rectangle2, n, window,start_color,subs_color):
    """
    What comes in:  Four arguments:
      -- Two rg.Rectangles.
      -- A positive integer n.
      -- An rg.RoseWindow.
    What goes out:  Nothing (i.e., None).
    Side effects:
      See   draw_lines_from_rectangles.pdf   in this project
      for pictures that may help you better understand
      the following specification:

      First draws the given rg.Rectangles on the given rg.RoseWindow.
      Then draws  n  rg.Lines on the given rg.RoseWindow, such that:
        -- The 1st rg.Line goes from the center of one of the
             1st rg.Rectangle to the center of the 2nd rg.Rectangle.
        -- The 2nd rg.Line goes from the lower-left corner of the
              1st rg.Rectangle and is parallel to the 1st rg.Line,
              with the same length and direction as the 1st rg.Line.
        -- Subsequent rg.Lines are shifted from the previous rg.Line in
              the same way that the 2nd rg.Line is shifted from the 1st.
        -- Each of the rg.Lines has thickness 5.
        -- The colors of the rg.Lines alternate, as follows:
             - The 1st, 3rd, 5th, ... rg.Line has color R1_color
             - The 2nd, 4th, 6th, ... rg.Line has color R2_color
            where
             - R1_color is the outline color of the 1st rg.Rectangle
             - R2_color is the outline color of the 2nd rg.Rectangle
      Must  ** render **     but   ** NOT close **   the window.

    Type hints:
      :type rectangle1: rg.Rectangle
      :type rectangle2: rg.Rectangle
      :type n: int
      :type window: rg.RoseWindow
      """
    # ------------------------------------------------------------------
    # Done: 5. Implement and test this function.
    #          Tests have been written for you (above).
    #
    # CONSIDER using the ACCUMULATOR IN GRAPHICS pattern,
    #             as in   draw_row_of_circles   in m1e,
    #             instead of directly using the loop variable.
    #
    ####################################################################
    # HINT: To figure out the code that computes the necessary
    #       endpoints for each line,
    #          ** FIRST DO A CONCRETE EXAMPLE BY HAND! **
    ####################################################################
    # ------------------------------------------------------------------
    x1 = float(rectangle1.get_center().x)
    x2 = float(rectangle2.get_center().x)

    y1 = float(rectangle1.get_center().y)
    y2 = float(rectangle2.get_center().y)

    for k in range(n):
        line_start = rg.Point(x1-k*30, y1+k*30)
        line_end = rg.Point(x2-k*30, y2+k*30)

        line = rg.Line(line_start,line_end)
        line.thickness = 5
        if k % 2 == 0:
            line.color = start_color
        else:
            line.color = subs_color

        line.attach_to(window)


    rectangle1.attach_to(window)
    rectangle2.attach_to(window)
    window.render()


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
