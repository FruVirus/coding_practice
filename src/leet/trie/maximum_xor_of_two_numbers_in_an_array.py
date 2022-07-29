"""
Maximum XOR of Two Numbers in an Array
--------------------------------------

Given an integer array nums, return the maximum result of nums[i] XOR nums[j], where
0 <= i <= j < n.

Intuition
---------

We want to do the comparison starting with the leftmost bit of each number going to the
rightmost bit. The leftmost bit can then be considered a "prefix" of that number and so
we can use a trie.

We first need to ensure that all numbers are the same length bit-wise.

Each root -> leaf path in Bitwise Trie represents a binary form of a number in nums, for
example, 0 -> 0 -> 0 -> 1 -> 1 is 3. As before, the same number of bits L is used for
all numbers, and L = 1 + lg(M), where M is a maximum number in nums. The depth of
Bitwise Trie is equal to L as well, and all leafs are on the same level.

Bitwise Trie is a perfect way to see how different the binary forms of numbers are, for
example, 3 and 2 share 4 bits of 5. The construction of Bitwise Trie is pretty
straightforward, it's basically nested hashmaps. At each step one has to verify, if the
child node to add (0 or 1) is already present. If yes, just go one step down. If not,
add it into the Trie and then go one step down.

To maximize XOR, the strategy is to choose the opposite bit at each step whenever it's
possible.

The implementation is also pretty simple:

    - Try to go down to the opposite bit at each step if it's possible. Add 1-bit at the
end of current XOR.
    - If not, just go down to the same bit. Add 0-bit at the end of current XOR.

NB: We first need to compute the binary representation of all numbers in nums and ensure
that their binary representations all have the same length. Thus, we find the binary
representation of the maximum number in nums and left zero-pad all other numbers as
needed.

Complexity
==========

Time
----

findMaximumXOR(nums): O(n). It takes O(l) to insert a number in the trie and O(l) to
find the max XOR of the given number with all already inserted ones. l = 1 + lg(m) is
defined by the maximum number in the array and could be considered as a constant here.
Hence, the overall time complexity if O(n).

Space
-----

findMaximumXOR(nums): O(1), since one needs at most O(2^l) = O(m) space to keep the trie
and l and m could be considered as constants here.
"""


def sol(nums):
    l = len(bin(max(nums))) - 2
    nums = [[(num >> i) & 1 for i in reversed(range(l))] for num in nums]
    max_xor, trie = 0, {}
    for num in nums:
        curr_xor, node, xor_node = 0, trie, trie
        for bit in num:
            node = node.setdefault(bit, {})
            flipped_bit = 1 - bit
            if flipped_bit in xor_node:
                curr_xor, xor_node = (curr_xor << 1) | 1, xor_node[flipped_bit]
            else:
                curr_xor, xor_node = curr_xor << 1, xor_node[bit]
        max_xor = max(max_xor, curr_xor)
    return max_xor
