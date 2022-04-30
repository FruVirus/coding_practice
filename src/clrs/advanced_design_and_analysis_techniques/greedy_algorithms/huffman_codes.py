"""
16.3 Huffman codes
==================

Huffman codes compress data very effectively: savings of 20% to 90% are typical,
depending on the characteristics of the data being compressed. We consider the data to
be a sequence of characters. Huffman's greedy algorithm uses a table giving how often
each character occurs (i.e., its frequency) to build up an optimal way of representing
each character as a binary string.

We have many options for how to represent a file of information. Here, we consider the
problem of designing a binary character code (or code for short) in which each character
is represented by a unique binary string, which we call a codeword. If we use a
fixed-length code, we need a fixed number of bits to represent the characters in a file.

A variable-length code can do considerably better than a fixed-length code, by giving
frequent characters short codewords and infrequent characters long codewords.

Prefix codes
------------

We consider here only codes in which no codeword is also a prefix of some other
codeword. Such codes are called prefix codes. A prefix code can always achieve the
optimal data compression among any character code, and so we suffer no loss of
generality by restricting our attention to prefix codes.

Encoding is always simple for any binary character code; we just concatenate the
codewords representing each character of the file. For example, with a variable-length
prefix code, we can code abc as 0 101 100 = 0101100.

Prefix codes are desirable because they simplify decoding. Since no codeword is a prefix
of any other, the codeword that begins an encoded file is unambiguous. We can simply
identify the initial codeword, translate it back to the original character, and repeat
the decoding process on the remainder of the encoded file.

The decoding process needs a convenient representation for the prefix code so that we
can easily pick off the initial codeword. A binary tree whose leaves are the given
characters provides one such representation. We interpret the binary codeword for a
character as the simple path from the root to that character, where 0 means "go to the
left child" and 1 means "go to the right child". Note that these are not binary search
trees, since the leaves need not appear in sorted order and internal nodes do not
contain character keys.

An optimal code for a file is always represented by a full binary tree, in which every
non-leaf node has two children. The fixed-length code is not optimal since its tree is
not a full binary tree. Since we can now restrict our attention to full binary trees,
we can say that if C is the alphabet from which the characters are drawn and all
character frequencies are positive (i.e., > 0), then the tree for an optimal prefix code
has exactly |C| leaves, one for each letter of the alphabet, and exactly |C| - 1
internal nodes.

Constructing a Huffman code
---------------------------

In the Huffman code algorithm, we assume that C is a set of n characters and that each
character c in C is an object with attribute c.freq giving its frequency. The algorithm
builds the tree corresponding to the optimal code in a bottom-up manner. It begins with
a set of |C| leaves and performs a sequence of |C| - 1 "merging" operations to create
the final tree. The algorithm uses a min-priority queue keyed on the freq attribute to
identify the two least-frequent objects to merge together. When we merge two objects,
the result is a new object whose frequency is the sum of the frequencies of the two
objects that were merged. This pattern of merging is an optimal merge pattern (i.e.,
always merge the two objects with the lowest frequencies first). The root of the tree
gives the total number of bits required to encode C.

The codeword for a letter is the sequence of edge labels on the simple path from the
root to the letter.

Correctness of Huffman's algorithm
----------------------------------

The process of building up an optimal tree can begin with the greedy choice of merging
together those two characters of lowest frequency. This is known as the optimal merge
pattern. We can view the cost of a single merger as being the sum of the frequencies of
the two items being merged. Of all possible mergers at each step, the Huffman algorithm
chooses the one that incurs the least cost.

Complexity
==========

We assume that the queue is implemented as a binary min-heap. Each heap operation thus
requires time O(lg n) and the loop executes n - 1 times.

Time
----

huffman_bu(): O(n * lg n).
"""

# Repository Library
from src.clrs.data_structures.elementary_data_structures.heap_queue import HeapQueue


class HuffmanQueue(HeapQueue):
    def change(self, i, k):
        self.a[i] = k
        while i > 0 and self.compare(self.freq(self._parent(i)), self.freq(i)):
            self._exchange(i, self._parent(i))
            i = self._parent(i)

    def freq(self, i):
        return self.a[i].freq if isinstance(self.a[i], Node) else self.a[i]

    def heapify(self, i):
        l, r, index = self._left(i), self._right(i), i
        if l < self.heap_size and not self.compare(self.freq(l), self.freq(i)):
            index = l
        if r < self.heap_size and not self.compare(self.freq(r), self.freq(index)):
            index = r
        if index != i:
            self._exchange(i, index)
            self.heapify(index)


class Node:
    def __init__(self, c=None, freq=0):
        self.c, self.freq = c, freq
        self.left = self.right = None


def huffman_bu(c):
    q = HuffmanQueue([Node(k, v) for k, v in c.items()], False)
    for _ in range(len(c) - 1):
        z = Node()
        z.left, z.right = q.extract(), q.extract()
        z.c = z.left.c + z.right.c
        left_freq = z.left.freq if isinstance(z.left, Node) else z.left
        right_freq = z.right.freq if isinstance(z.right, Node) else z.right
        z.freq += left_freq + right_freq
        q.insert(z)
    root, sol = q.extract(), {k: [] for k in c}
    for k in c:
        node = root
        while node.c != k:
            node, code = (node.left, 0) if k in node.left.c else (node.right, 1)
            sol[k].append(code)
    return sol, sum(c[k] * len(sol[k]) for k in c)
