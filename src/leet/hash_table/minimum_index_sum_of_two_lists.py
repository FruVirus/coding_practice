"""
Minimum Index Sum of Two Lists
------------------------------

Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list
of favorite restaurants represented by strings.

You need to help them find out their common interest with the least list index sum. If
there is a choice tie between answers, output all of them with no order requirement. You
could assume there always exists an answer.

All the strings of list1 are unique. All the strings of list2 are unique.

Complexity
==========

Time
----

findRestaurant(list1, list2): O().

Space
-----

findRestaurant(list1, list2): O().
"""


def sol(list1, list2):
    l1_map, min_sum, sol = {l1: i1 for i1, l1 in enumerate(list1)}, float("inf"), []
    for i2, l2 in enumerate(list2):
        if l2 in l1_map:
            index_sum = l1_map[l2] + i2
            if index_sum < min_sum:
                min_sum, sol = index_sum, [l2]
            elif index_sum == min_sum:
                sol.append(l2)
    return sol
