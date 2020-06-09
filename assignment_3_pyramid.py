"""
File: pyramid.py
----------------
Draws a centered pyramid on the canvas with base of BRICKS_IN_BASE and one less brick
each row until finished. Bricks are of size BRICK_WIDTH and BRICK_HEIGHT.
"""


import tkinter


CANVAS_WIDTH = 600      # Width of drawing canvas in pixels
CANVAS_HEIGHT = 300     # Height of drawing canvas in pixels

BRICK_WIDTH = 30        # The width of each brick in pixels
BRICK_HEIGHT = 12       # The height of each brick in pixels
BRICKS_IN_BASE = 14     # The number of bricks in the base


# Draws a brick starting at x,y with a specified width and height
def draw_brick(canvas, x, y, width, height):
    canvas.create_rectangle(x, y, x + width, y + height)


# draws a centered pyramid of bricks with BRICKS_IN_BASE and one less brick each row
def draw_pyramid(canvas):
    # loops through rows
    for i in range(BRICKS_IN_BASE):
        # find inset for start x,y of row
        start_x = find_row_start_x_pixel(i)
        start_y = find_row_start_y_pixel(i)
        # draws number of bricks for row
        for j in range(BRICKS_IN_BASE - i):
            draw_brick(canvas, start_x + (j * BRICK_WIDTH), start_y, BRICK_WIDTH, BRICK_HEIGHT)


# finds the starting x pixel to draw each row (zero indexed)
def find_row_start_x_pixel(row_num):
    center = CANVAS_WIDTH / 2
    brick_length = (BRICKS_IN_BASE - row_num) * BRICK_WIDTH
    x_value = center - brick_length / 2
    return x_value


# finds the starting y pixel for each row (zero indexed)
def find_row_start_y_pixel(row_num):
    # row_num + 1 to account for o indexed rows
    y_value = CANVAS_HEIGHT - (BRICK_HEIGHT * (row_num + 1))
    return y_value


######## DO NOT MODIFY ANY CODE BELOW THIS LINE ###########

# This function is provided to you and should not be modified.
# It creates a window that contains a drawing canvas that you
# will use to make your drawings.
def make_canvas(width, height):
    """
    DO NOT MODIFY
    Creates and returns a drawing canvas
    of the given int size with a blue border,
    ready for drawing.
    """
    top = tkinter.Tk()
    top.minsize(width=width + 10, height=height + 10)
    top.title('pyramid')
    canvas = tkinter.Canvas(top, width=width + 1, height=height + 1)
    canvas.pack()
    canvas.xview_scroll(8, 'units')  # This is so (0, 0) works correctly,
    canvas.yview_scroll(8, 'units')  # otherwise it's clipped off

    # Draw blue boundary line at bottom of canvas
    canvas.create_line(0, height, width, height, width=1, fill='blue')

    return canvas


def main():
    """
    This program, when completed, displays a pyramid graphically.
    """
    canvas = make_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    draw_pyramid(canvas)
    tkinter.mainloop()


if __name__ == '__main__':
    main()
