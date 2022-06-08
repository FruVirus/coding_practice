"""
Reverse Bits
------------

Reverse bits of a given 32 bits unsigned integer.

Intuition
---------

The key idea is that for a bit that is situated at the index i, after the reversion, its
position should be 31-i (note: the index starts from zero).

1. For each bit, we reverse it to the correct position (i.e., (n & 1) << power). Then we
accumulate this reversed bit to the final result.

2. We iterate through the bit string of the input integer, from right to left (i.e.,
n = n >> 1). To retrieve the right-most bit of an integer, we apply the bit AND
operation (n & 1).

3. When there is no more bits of one left (i.e., n == 0), we terminate the iteration.

Complexity
==========

Time
----

reverseBits(n) O(1).

Space
-----

reverseBits(n): O(1).
"""


def sol(n):
	rn, power = 0, 31
	while n != 0:
		rn += (n & 1) << power
		n >>= 1
		power -= 1
	return rn
