"""
File: ghost.py
--------------
ADD YOUR DESCRIPTION HERE

TODO - Understand pixel distance and how it factors into final code
        why is it needed?
        can i use it to make pixel selection more or less sensitive?

"""

import os
import sys

# The line below imports SimpleImage for use here.
# It depends on the Pillow package being installed.
from simpleimage import SimpleImage


# Returns the square of the color distance between pixel and mean RGB value
def get_pixel_dist(pixel, red, green, blue):
    return (pixel.red - red) ** 2 + (pixel.green - green) ** 2 + (pixel.blue - blue) ** 2


# Given three pixels, returns the pixel with the smallest
# distance from the average red, green, and blue values across all pixels.
def get_best_pixel(pixel1, pixel2, pixel3):
    # get R,G,B pixel averages
    pixel_red_average = (pixel1.red + pixel2.red + pixel3.red) / 3
    pixel_green_average = (pixel1.green + pixel2.green + pixel3.green) / 3
    pixel_blue_average = (pixel1.blue + pixel2.blue + pixel3.blue) / 3
    # compare pixel in each image with pixel averages
    one_comp = abs(pixel1.red - pixel_red_average) + abs(pixel1.green - pixel_green_average) + abs(
        pixel1.blue - pixel_blue_average)
    two_comp = abs(pixel2.red - pixel_red_average) + abs(pixel2.green - pixel_green_average) + abs(
        pixel2.blue - pixel_blue_average)
    three_comp = abs(pixel3.red - pixel_red_average) + abs(pixel3.green - pixel_green_average) + abs(
        pixel3.blue - pixel_blue_average)
    # return pixel closest to average
    if one_comp <= two_comp and one_comp <= three_comp:
        return pixel1
    if two_comp <= one_comp and two_comp <= three_comp:
        return pixel2
    if three_comp <= one_comp and three_comp <= two_comp:
        return pixel3


# creates a ghost image from 3 images, by using best pixel
def create_ghost(image1, image2, image3):
    # create blank image
    ghost_image = SimpleImage.blank(image1.width, image1.height)
    # look at individual pixels for all three images and assign best pixel as ghost pixel
    for x in range(image1.width):
        for y in range(image1.height):
            pixel1 = image1.get_pixel(x, y)
            pixel2 = image2.get_pixel(x, y)
            pixel3 = image3.get_pixel(x, y)
            ghost_pixel = get_best_pixel(pixel1, pixel2, pixel3)
            ghost_image.set_pixel(x, y, ghost_pixel)
    return ghost_image


######## DO NOT MODIFY ANY CODE BELOW THIS LINE ###########


def jpgs_in_dir(directory):
    """
    DO NOT MODIFY
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(directory):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(directory, filename))
    return filenames


def load_images(directory):
    """
    DO NOT MODIFY
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints to terminal the names of the files it loads.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(directory)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # DO NOT MODIFY
    args = sys.argv[1:]

    if len(args) != 1:
        print('Please specify directory of images on command line')
        return

    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    result = create_ghost(images[0], images[1], images[2])
    if result:
        print("Displaying image!")
        result.show()
    else:
        print("No image to display!")


if __name__ == '__main__':
    main()
