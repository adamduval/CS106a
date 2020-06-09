"""
File: quilt.py
--------------
Draws a quilt pattern of bars, eye and bowtie.
Input width, height and number of patches (n)
"""


import sys
import tkinter


# draws evenly space horizontal lines filling the patch
def draw_bars(canvas, x, y, width, height, num_lines):
    canvas.create_rectangle(x, y, x + width, y + height, outline='lightblue')
    # need to account for number of spaces in between (why -1 is needed)
    line_space = width/(num_lines - 1)
    for i in range(num_lines):
        canvas.create_line(x + (i * line_space), y, x + (i * line_space), y + height)


# draws an oval with evenly spaced lines radiating from the center
def draw_eye(canvas, x, y, width, height, num_lines):
    canvas.create_rectangle(x, y, x + width, y + height, outline='lightblue')
    canvas.create_oval(x, y, x + width, y + height, outline ='yellow', fill='yellow')
    line_space = width/(num_lines - 1)
    # need to account for shifting center on each set of lines (why +x, +y is needed)
    center_x = x + (width // 2)
    center_y = y + (height // 2)
    for i in range(num_lines):
        canvas.create_line(center_x, center_y, x + (i * line_space), y + height)


# draws evenly space diagonal lines (top left to bottom right) intersecting the center of the of patch
def draw_bowtie(canvas, x, y, width, height, num_lines):
    canvas.create_rectangle(x, y, x + width, y + height, outline='lightblue')
    line_space = height/(num_lines - 1)
    # need to account for shifting center ( why +y is needed)
    for i in range(num_lines):
        canvas.create_line(x, y + (i * line_space), x + width, y + height - (i * line_space), fill='red')


# draws quilt with rotating n number of pratches
def draw_quilt(canvas, width, height, n):
    num_lines = n
    sub_width = width // n
    sub_height = height // n
    for row in range(n):
        for col in range(n):
            choice = (row + col) %3
            if choice == 0:
                draw_bars(canvas, row * sub_width, col * sub_height, sub_width, sub_height, num_lines)
            if choice == 1:
                draw_bowtie(canvas,row * sub_width, col * sub_height, sub_width, sub_height, num_lines)
            if choice == 2:
                draw_eye(canvas, row * sub_width, col * sub_height, sub_width, sub_height, num_lines)



######## DO NOT MODIFY ANY CODE BELOW THIS LINE ###########

# main() code is complete and should not be modified.
# There are 5 command lines that work here,
# with width/height/n being positive integers.
#  -bars width height num_lines
#  -eye width height num_lines
#  -bowtie width height num_lines
#  -quilt width height n
# e.g. run like this in the terminal:
#  py quilt.py -bars 600 400 10


# This function is provided to you and should not be modified.
# It creates a window that contains a drawing canvas that you
# will use to make your drawings.
def make_canvas(width, height):
    """
    DO NOT MODIFY
    Creates and returns a drawing canvas of the
    of the given int size, ready for drawing.
    """
    top = tkinter.Tk()
    top.minsize(width=width + 10, height=height + 10)
    top.title('quilt')
    canvas = tkinter.Canvas(top, width=width + 1, height=height + 1)
    canvas.pack()
    canvas.xview_scroll(8, 'units')  # add this so (0, 0) works correctly
    canvas.yview_scroll(8, 'units')  # otherwise it's clipped off

    return canvas


def main():
    # Standard first line of main to get args
    args = sys.argv[1:]

    if len(args) != 4:
        print('usage: (one of -bars, -eye, -bowtie, -quilt) width height n')
        return

    # Parse width/height/n from command line, giving a helpful
    # error message if it fails.
    try :
        width = int(args[1])
        height = int(args[2])
        n = int(args[3])
    except Exception as e:
        print("Error parsing int width/height/n from command line:" + ' '.join(args))
        return

    # Tricky: we do all the drawing in a try, so that if it takes an exception,
    # we can still do the mainloop() at the end. If we do not do this, an exception
    # causes no graphics output to appear which makes debugging hard.
    try:
        if args[0] == '-bars':
            canvas = make_canvas(width * 2, height * 2)
            # Can change to fast_draw=False .. drawing plays out more slowly
            draw_bars(canvas, 0, 0, width, height, n)
            draw_bars(canvas, width, height, width, height, n)

        if args[0] == '-eye':
            canvas = make_canvas(width * 2, height * 2)
            draw_eye(canvas, 0, 0, width, height, n)
            draw_eye(canvas, width, height, width, height, n)

        if args[0] == '-bowtie':
            canvas = make_canvas(width * 2, height * 2)
            draw_bowtie(canvas, 0, 0, width, height, n)
            draw_bowtie(canvas, width, height, width, height, n)

        if args[0] == '-quilt':
            canvas = make_canvas(width, height)
            draw_quilt(canvas, width, height, n)

    # Print out exception from draw
    except Exception as e:
        print(e)

    """
    Calls the tkinter.mainloop(), typically last line of main().
    This version checks that there is a window on screen first,
    doing nothing if there is no window.
    """
    if tkinter._default_root:
        tkinter._default_root.update()
        tkinter.mainloop()


if __name__ == '__main__':
    main()
