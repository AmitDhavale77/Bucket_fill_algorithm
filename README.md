# Bucket Fill Algorithm - Recursive Approach

Project Overview

This project implements a bucket fill algorithm in Python, inspired by the "paint bucket" tool found in many graphics editing software. The goal of this algorithm is to "fill" an area with a new color, starting from a given starting point, by replacing the old color.

The core functionality is implemented in the fill() function in the bucket_fill.py file. The algorithm uses a recursive approach to traverse through the grid (or image matrix), identifying all adjacent cells (up, down, left, right) that share the same color as the starting point and filling them with the new color.

Recursive Approach

The recursive approach algorithm works as follows:

Base Case:
If the current cell is out of bounds or already filled with the new color, the function returns immediately.
This avoids infinite recursion and unnecessary processing.

Recursive Case:
If the current cell has the original color, it is filled with the new color.
The algorithm then recursively checks the neighboring cells (up, down, left, right) and applies the same logic.

Steps:
Check Boundary Conditions: Ensure the current pixel is within the grid's bounds.
Check Current Color: If the current pixel's color is the same as the old color, change it to the new color.
Recursive Fill: Recursively apply the fill function to the four neighboring pixels.
