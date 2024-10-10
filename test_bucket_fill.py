from bucket_fill import (
    fill,
    recursive_fill,
    is_boundary_pixel, 
    is_outside_image, 
    is_not_integer, 
    load_image
)

#Write test cases for all valid inputs

def test_is_boundary_pixel():
    '''To validate the code when the given seed_point lies on the boundary of the image '''

    seed_point = (0, 1)
    expected_image = load_image("data/smiley.txt")
    filled_image = fill(expected_image, seed_point)

    assert expected_image == filled_image


def test_is_not_integer():
    '''To validate the code when the given seed_point has a non-integer coordinates '''

    seed_point = (1.3, "a")
    expected_image = load_image("data/smiley.txt")
    filled_image = fill(expected_image, seed_point)

    assert expected_image == filled_image


def test_is_outside_image():
    '''To validate the code when the seed_point lies outside of the image '''

    seed_point = (-1, 4)
    expected_image = load_image("data/smiley.txt")
    filled_image = fill(expected_image, seed_point)

    assert expected_image == filled_image


def test_valid_seedpoint():
    '''To validate the code when the seed_point is valid '''

    seed_point = (2, 4)
    org_image = load_image("data/smiley.txt")
    
    expected_image = [[0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], 
                    [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1], 
                    [1, 2, 2, 1, 2, 2, 2, 1, 2, 2, 1], 
                    [1, 2, 1, 0, 1, 2, 1, 0, 1, 2, 1], 
                    [1, 2, 2, 1, 2, 2, 2, 1, 2, 2, 1], 
                    [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1], 
                    [1, 2, 1, 1, 1, 1, 1, 1, 1, 2, 1], 
                    [1, 2, 1, 0, 0, 0, 0, 0, 1, 2, 1], 
                    [1, 2, 2, 1, 0, 0, 0, 1, 2, 2, 1], 
                    [1, 2, 2, 2, 1, 1, 1, 2, 2, 2, 1], 
                    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]]

    filled_image = fill(org_image, seed_point)

    assert expected_image == filled_image


def test_single_pixel_image():
    '''To validate the code when I have an image consisting of only one pixel '''

    seed_point = (0, 0)
    org_image = [[0]]

    expected_image = [[2]]

    filled_image = fill(org_image, seed_point)
    assert  expected_image == filled_image


def test_large_image():
    '''To validate the code when I have a large image of size (25x25) '''

    seed_point = (1, 10)
    org_image = load_image("data/text_25.txt")
    
    expected_image = [[0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 1, 2, 1, 2, 1, 2], 
                    [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], 
                    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], 
                    [0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], 
                    [0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], 
                    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], 
                    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], 
                    [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], 
                    [0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], 
                    [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], 
                    [1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], 
                    [1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], 
                    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], 
                    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], 
                    [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], 
                    [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], 
                    [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], 
                    [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], 
                    [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], 
                    [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], 
                    [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], 
                    [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], 
                    [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], 
                    [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], 
                    [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]]

    filled_image = fill(org_image, seed_point)

    assert expected_image == filled_image

def test_pattern():
    
    test_is_boundary_pixel()

    test_is_not_integer()

    test_is_outside_image()

    test_valid_seedpoint()

    test_single_pixel_image()

    test_large_image()

if __name__ == '__main__':
    # This is just an example. Feel free to change this to whatever suits you.
    test_pattern()
