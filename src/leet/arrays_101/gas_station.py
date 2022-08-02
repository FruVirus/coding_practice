"""
Gas Station
-----------

There are n gas stations along a circular route, where the amount of gas at the ith
station is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the
ith station to its next (i + 1)th station. You begin the journey with an empty tank at
one of the gas stations.

Given two integer arrays gas and cost, return the starting gas station's index if you
can travel around the circuit once in the clockwise direction, otherwise return -1. If
there exists a solution, it is guaranteed to be unique.

Intuition
---------

The first idea is to check every single station:

    - Choose the station as starting point.

    - Perform the road trip and check how much gas we have in tank at each station.

That means O(N ^ 2) time complexity, and for sure one could do better.

Let's notice two things.

    1. It's impossible to perform the road trip if sum(gas) < sum(cost). In this
situation the answer is -1.

    2. It's impossible to start at a station i if gas[i] - cost[i] < 0, because then
there is not enough gas in the tank to travel to i + 1 station.

The second fact could be generalized. Let's introduce curr_tank variable to track the
current amount of gas in the tank. If at some station curr_tank is less than 0, that
means that one couldn't reach this station (from some starting point).

Next step is to mark this station as a new starting point, and reset curr_tank to zero
since one starts with no gas in the tank.

In other words, if sum(gas) >= sum(cost), there has to be a solution, and a solution is
guaranteed to be unique. Therefore if we can go from S to the last station, and a
solution exists, we can assume we can complete a circuit back to S.

Complexity
==========

Time
----

canCompleteCircuit(gas, cost): O(n).

Space
-----

canCompleteCircuit(accounts): O(1).
"""


def sol(gas, cost):
    curr_tank = total_tank = start = 0
    for i, (g, c) in enumerate(zip(gas, cost)):
        total_tank += g - c
        curr_tank += g - c
        if curr_tank < 0:
            curr_tank, start = 0, i + 1
    return start if total_tank >= 0 else -1
