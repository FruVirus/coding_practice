# Standard Library
import math

# Repository Library
from clrs.selected_topics.matrix_operations.invert import invert, invert_lup


def test_invert():
    a = [[4, -2, 1], [5, 0, 3], [-1, 2, 6]]
    a_inv = invert(a)
    a_inv_answer = [
        [-0.11538461538461539, 0.2692307692307692, -0.11538461538461539],
        [-0.6346153846153846, 0.4807692307692308, -0.1346153846153846],
        [0.19230769230769232, -0.11538461538461539, 0.19230769230769232],
    ]
    for i in range(len(a)):
        for j in range(len(a[0])):
            assert math.isclose(a_inv[i][j], a_inv_answer[i][j])
    a = [[-3, 4], [2, 5]]
    a_inv = invert(a)
    a_inv_answer = [[-5 / 23, 4 / 23], [2 / 23, 3 / 23]]
    for i in range(len(a)):
        for j in range(len(a[0])):
            assert math.isclose(a_inv[i][j], a_inv_answer[i][j])


def test_invert_lup():
    a = [[4, -2, 1], [5, 0, 3], [-1, 2, 6]]
    a_inv = invert_lup(a)
    a_inv_answer = [
        [-0.11538461538461539, 0.2692307692307692, -0.11538461538461539],
        [-0.6346153846153846, 0.4807692307692308, -0.1346153846153846],
        [0.19230769230769232, -0.11538461538461539, 0.19230769230769232],
    ]
    for i in range(len(a)):
        for j in range(len(a[0])):
            assert math.isclose(a_inv[i][j], a_inv_answer[i][j])
    a = [[-3, 4], [2, 5]]
    a_inv = invert_lup(a)
    a_inv_answer = [[-5 / 23, 4 / 23], [2 / 23, 3 / 23]]
    for i in range(len(a)):
        for j in range(len(a[0])):
            assert math.isclose(a_inv[i][j], a_inv_answer[i][j])
