"""
Robot Room Cleaner
------------------

You are controlling a robot that is located somewhere in a room. The room is modeled as
an m x n binary grid where 0 represents a wall and 1 represents an empty slot.

The robot starts at an unknown location in the room that is guaranteed to be empty, and
you do not have access to the grid, but you can move the robot using the given API
Robot.

You are tasked to use the robot to clean the entire room (i.e., clean every empty cell
in the room). The robot with the four given APIs can move forward, turn left, or turn
right. Each turn is 90 degrees.

When the robot tries to move into a wall cell, its bumper sensor detects the obstacle,
and it stays on the current cell.

Design an algorithm to clean the entire room using the following APIs:

    interface Robot {
      // returns true if next cell is open and robot moves into the cell.
      // returns false if next cell is obstacle and robot stays on the current cell.
      boolean move();

      // Robot will stay on the same cell after calling turnLeft/turnRight.
      // Each turn will be 90 degrees.
      void turnLeft();
      void turnRight();

      // Clean the current cell.
      void clean();
    }

Note that the initial direction of the robot will be facing up. You can assume all four
edges of the grid are all surrounded by a wall.

Intuition
---------

This solution is based on the same idea as maze solving algorithm called right-hand
rule. Go forward, cleaning and marking all the cells on the way as visited. At the
obstacle turn right, again go forward, etc. Always turn right at the obstacles and then
go forward. Consider already visited cells as virtual obstacles.

What to do if after the right turn there is an obstacle just in front?

    Turn right again.

How to explore the alternative paths from the cell?

    Go back to that cell and then turn right from your last explored direction.

When to stop?

    Stop when you explored all possible paths, i.e. all 4 directions (up, right, down,
and left) for each visited cell.

Complexity
==========

Time
----

cleanRoom(robot): O(n - m), where n is the number of cells in the room and m is the
number of obstacles.

Space
-----

combine(robot): O(n - m).
"""


def sol(robot):
    def go_back():
        robot.turn_right()
        robot.turn_right()
        robot.move()
        robot.turn_right()
        robot.turn_right()

    def backtrack(row, col, d):
        seen.add((row, col))
        robot.clean()
        for i in range(4):
            d_ = (d + i) % 4
            r, c = row + directions[d_][0], col + directions[d_][1]
            if (r, c) not in seen and robot.move():
                backtrack(r, c, d_)
                go_back()
            robot.turn_right()

    directions, seen = [(0, 1), (1, 0), (0, -1), (-1, 0)], set()
    return backtrack(0, 0, 0)
