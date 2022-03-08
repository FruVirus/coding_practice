"""
Flood Fill
----------

An image is represented by an m x n integer grid image where image[i][j] represents the
pixel value of the image.

You are also given three integers sr, sc, and newColor. You should perform a flood fill
on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected
4-directionally to the starting pixel of the same color as the starting pixel, plus any
pixels connected 4-directionally to those pixels (also with the same color), and so on.
Replace the color of all of the aforementioned pixels with newColor.

Return the modified image after performing the flood fill.

Complexity
==========

Time
----

floodFill(image, sr, sc, new_color): O(n), where n is the number of pixels in the image.

Space
-----

floodFill(image, sr, sc, new_color): O(n).
"""


def sol(image, sr, sc, new_color):
    m, n = len(image), len(image[0])
    orig_color, image[sr][sc] = image[sr][sc], new_color
    for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        sr_, sc_ = sr + x, sc + y
        if 0 <= sr_ < m and 0 <= sc_ < n and image[sr_][sc_] != new_color:
            if image[sr_][sc_] == orig_color:
                sol(image, sr_, sc_, new_color)
    return image
