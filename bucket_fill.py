""" Coursework 1: Bucket Fill
"""

def load_image(filename):
    """ Load image from file made of 0 (unfilled pixels) and 1 (boundary pixels) and 2 (filled pixel)

    Example of content of filename:

0 0 0 0 1 1 0 0 0 0
0 0 1 1 0 0 1 1 0 0
0 1 1 0 0 1 0 1 1 0
1 1 0 0 1 0 1 0 1 1
1 0 0 1 0 0 1 0 0 1
1 0 0 1 0 0 1 0 0 1
1 1 0 1 0 0 1 0 1 1
0 1 1 0 1 1 0 1 1 0
0 0 1 1 0 0 1 1 0 0
0 0 0 0 1 1 0 0 0 0

    Args:
        filename (str) : path to file containing the image representation

    Returns:
        list : a 2D representation of the filled image, where
               0 represents an unfilled pixel,
               1 represents a boundary pixel
               2 represents a filled pixel
    """

    image = []
    with open(filename) as imagefile:
        for line in imagefile:
            if line.strip():
                row = list(map(int, line.strip().split()))
                image.append(row)
    return image


def stringify_image(image):
    """ Convert image representation into a human-friendly string representation

    Args:
        image (list) : list of lists of 0 (unfilled pixel), 1 (boundary pixel) and 2 (filled pixel)

    Returns:
        str : a human-friendly string representation of the image
    """
    
    if image is None:
        return ""

    # The variable "mapping" defines how to display each type of pixel.
    mapping = {
        0: " ",
        1: "*",
        2: "0"
    }

    image_str = ""
    if image:
        image_str += "+ " + "- " * len(image[0]) + "+\n"
    for row in image:
        image_str += "| "
        for pixel in row:
            image_str += mapping.get(pixel, "?") + " "
        image_str += "|"
        image_str += "\n"
    if image:
        image_str += "+ " + "- " * len(image[0]) + "+\n" 
        
    return image_str


def show_image(image):
    """ Show image in terminal

    Args:
        image (list) : list of lists of 0 (unfilled pixel), 1 (boundary pixel) and 2 (filled pixel)
    """
    print(stringify_image(image))


def is_not_integer(seed_point):
    ''' Check wether the seed_point has a non-integer coordinate

    Args:
        seed_point (tuple) :  a 2-element tuple representing the (row, col) 
                       coordinates of the seed point to start filling
    
    Return:
        bool : Wether the seed_pont is integer or not

    '''

    return type(seed_point[0]) != int or type(seed_point[1]) != int


def is_outside_image(image, seed_point):
    ''' Check wether the seed_point is outside the image or not

    Args:
        image (list) : a 2D nested list representation of an image, where
                       0 represents an unfilled pixel, and
                       1 represents a boundary pixel
        seed_point (tuple) :  a 2-element tuple representing the (row, col) 
                       coordinates of the seed point to start filling
    
    Return:
        bool : Wether the seed_pont lies outside the image or not

    '''
    return seed_point[0]<0 or seed_point[1]<0 or (seed_point[0]>len(image)-1) or seed_point[1]>len(image[0])-1


def is_boundary_pixel(image, seed_point):
    ''' Check wether the seed_point is on a boundary pixel or not

    Args:
        image (list) : a 2D nested list representation of an image, where
                       0 represents an unfilled pixel, and
                       1 represents a boundary pixel
        seed_point (tuple) :  a 2-element tuple representing the (row, col) 
                       coordinates of the seed point to start filling
    
    Return:
        bool : Wether the seed_pont is on a boundary pixel or not 

    '''

    return image[seed_point[0]][seed_point[1]] == 1


def recursive_fill(image, row, col):
    ''' 
    Recursively fill the image from seed point to boundary

    Args:
        image (list) : a 2D nested list representation of an image, where
                       0 represents an unfilled pixel, and
                       1 represents a boundary pixel
        seed_point (tuple) :  a 2-element tuple representing the (row, col) 
                       coordinates of the seed point to start filling
    
    Return:
        bool : Wether the seed_pont is on a boundary pixel or not 

    '''

    row_len = len(image)
    col_len = len(image[0])

    # Base condition: When the seed_point is outside the image, the position of seed_point is filled

    if row>=row_len or row<0 or col>=col_len or col<0 or image[row][col]==2: 
        return None

    # Fill the adjacent pixels of the seed_point if the pixel is not a boundary pixel

    if image[row][col] != 1:
        image[row][col] = 2
        recursive_fill(image, row, col+1)
        recursive_fill(image, row, col-1)
        recursive_fill(image, row+1, col)
        recursive_fill(image, row-1, col)


def fill(image, seed_point):
    """ Fill the image from seed point to boundary

    the image should remain unchanged if:
    - the seed_point has a non-integer coordinate
    - the seed_point is on a boundary pixel
    - the seed_point is outside of the image

    Args:
        image (list) : a 2D nested list representation of an image, where
                       0 represents an unfilled pixel, and
                       1 represents a boundary pixel
        seed_point (tuple) : a 2-element tuple representing the (row, col) 
                       coordinates of the seed point to start filling

    Returns:
        list : a 2D representation of the filled image, where
               0 represents an unfilled pixel,
               1 represents a boundary pixel, and
               2 represents a filled pixel
    """

    # TODO: Complete this function

    row, col = seed_point

    if is_not_integer(seed_point):
        return image

    if is_outside_image(image,seed_point):
        return image

    if is_boundary_pixel(image, seed_point):
        return image

    recursive_fill(image, row, col)

    return image



def example_fill():
    image = load_image("data/text_25.txt")

    print("Before filling:")
    show_image(image)

    image = fill(image=image, seed_point=(1, 10))

    print("-" * 25)
    print("After filling:")
    show_image(image)
    print(image)

if __name__ == '__main__':
    example_fill()

