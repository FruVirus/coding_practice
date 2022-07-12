"""
Container With Most Water
-------------------------

You are given an integer array height of length n. There are n vertical lines drawn such
that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container
contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Intuition
---------

We have to maximize the Area that can be formed between the vertical lines using the
shorter line as length and the distance between the lines as the width of the rectangle
forming the area.

The intuition behind this approach is that the area formed between the lines will always
be limited by the height of the shorter line. Further, the farther the lines, the more
will be the area obtained.

We take two pointers, one at the beginning and one at the end of the array constituting
the length of the lines. Further, we maintain a variable maxarea to store the maximum
area obtained till now. At every step, we find out the area formed between them, update
maxarea and move the pointer pointing to the shorter line towards the other end by one
step.

Initially we consider the area constituting the exterior most lines. Now, to maximize
the area, we need to consider the area between the lines of larger lengths. If we try to
move the pointer at the longer line inwards, we won't gain any increase in area, since
it is limited by the shorter line. But moving the shorter line's pointer could turn out
to be beneficial, as per the same argument, despite the reduction in the width. This is
done since a relatively longer line obtained by moving the shorter line's pointer might
overcome the reduction in area caused by the width reduction.

Complexity
==========

Time
----

maxArea(height): O(n).

Space
-----

maxArea(height): O(1).
"""


def sol(height):
    maxarea, left, right = 0, 0, len(height) - 1
    while left < right:
        width = right - left
        maxarea = max(maxarea, min(height[left], height[right]) * width)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return maxarea
