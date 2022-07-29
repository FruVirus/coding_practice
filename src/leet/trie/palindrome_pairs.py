"""
Palindrome Pairs
----------------

Given a list of unique words, return all the pairs of the distinct indices (i, j) in the
given list, so that the concatenation of the two words words[i] + words[j] is a
palindrome.

Input: words = ["abcd","dcba","lls","s","sssll"]
Output: [[0,1],[1,0],[3,2],[2,4]]
Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]

Intuition
---------

What are the ways we could form a palindrome with 2 words?

The simplest way to make a palindrome is to take 2 words that are the reverse of each
other and put them together. In this case, we get 2 different palindromes, as we can put
either word first.

We know that there are always 2 unique palindromes that can be formed by 2 words that
are the reverse of each other, because the words must be different. The problem
statement is clear that there are no duplicates in the word list.

Let's now think about all the words that could pair with a word 1 of "CAT" to make a
palindrome. We'll assume that all the possibilities for word 2 we're looking at are 8
letters long. While this assumption might seem too specific, remember that we're just
using it as a starting point to identify possible cases. We'll do a more general proof
later.

To start with, we know that the last letter of word 2 has to be "C". Otherwise, it would
be impossible to form a palindrome.

By that same logic, we also know the 2nd to last and 3rd to last characters must be "A"
and "T" respectively.

Here's where things start to get a bit interesting. We know that the 2 letters
highlighted in the next diagram must be the same for the combined word to be a
palindrome. We'll use numbers to show where letters must be the same.

[C, A, T, 1, ?, ?, ?, 1, T, A, C]

The same argument applies for the next pair of highlighted letters.

[C, A, T, 1, 2, ?, 2, 1, T, A, C]

And that last letter in the center can be anything.

[C, A, T, 1, 2, 3, 2, 1, T, A, C]

Let's now take a step back and see what we have. Our experimenting has shown us that if
word 2 is the concatenation of a 5-letter palindrome and then the reverse of word 1,
that the combined pair of word 1 and word 2 is a palindrome.

[C, A, T,| 1, 2, 3, 2, 1, T, A, C]
 word 1           word 2

Another case can also be seen here. If instead word 1 was the concatenation of the
reverse of word 2 and then a 5-letter palindrome, the combined pair of word 1 and word 2
would also be a palindrome.

[C, A, T, 1, 2, 3, 2, 1,| T, A, C]
         word 1           word 2

Don't forget that the empty string is also a valid word. How could we form a palindrome
with it? This is an important edge case we'll now think about.

Appending an empty string with another word will simply give the non-empty string word.
If this word was a palindrome by itself, we will have a valid palindrome pair. If it
wasn't, we won't. So any words that by themselves are a palindrome will form a
palindrome pair with the empty string.

Depending on the implementation you use, you might not need to treat this as a special
case, as it is really just a sub case of case 2 and case 3. It's just that the bit that
is reversed is of length-0. Make sure to test your implementation on this case though!

By experimenting, we've discovered a few cases. But for these kinds of questions, it's
very important to convince ourselves that we haven't overlooked any cases. One way we
can do this is by considering the relative length of each pair of words. There are 2
cases for the relative lengths within each pair.

    1. The words are both of the same length.
    2. The words are of different lengths.

We then need to show how each of these 2 cases fully map onto the palindrome pair cases
we've already discovered. We'll do this by considering where the middle of the combined
word (word we get by appending the second word to the first word) is.

For the first possibility, the center of the combined word is between the two words.

For the pair to form a palindrome, the letters before the center must be the reverse of
the letters after the center. The following diagram uses numbers to show where 2 letters
must be the same.

[1, 2, 3, 4, 5 | 5, 4, 3, 2, 1]

We can also see that this means word 1 must be the reverse of word 2.

Therefore, when 2 words of the same length form a palindrome, it must be because word 1
is the reverse of word 2 (which also means word 2 is the reverse of word 1). This is
equivalent to palindrome pair case 1.

For the second relative word-length case, we know that one of the words must be shorter
than the other. We'll assume for now that word 1 is shorter. The exact same argument
will make will also apply for when word 2 is shorter.

Like before, there must be a middle of the combined word. We know that because word 1 is
shorter, word 2 will overlap this center point.

We know that a palindrome must mirror around that center point. Therefore, we know that
the end of word 2 must be the reverse of word 1.

We are now left with the region between word 1 and the reverse of word 1. We know that
this middle region is divided equally in 2 by the middle line because we took the same
number of characters off each end of the combined word. Therefore, for the overall
combined word to be a palindrome, the piece in the middle must be a palindrome.

Which is equivalent to palindrome-pair case 2.

Using this same line of reasoning, you can easily show that when word 2 is shorter, it
is equivalent to palindrome pair case 3.

Therefore, we have proven that the only possible ways of forming a palindrome pair out
of 2 words are covered by the 3 palindrome-pair cases we discovered during our
exploration.

How can we put all this into code?

The simplest way to put all of this into code is to iterate over the list of words and
do the following for each word.

    1. Check if the reverse of word is present. If it is, then we have a case 1 pair by
appending the reverse onto the end of word. In addition, we should check that the index
of the reversed word is not the same as the current word since this would mean that a
word is forming a palindrome with itself (which is not allowed). This can happen if the
word is a single character.

    2. For each suffix of word, check if the suffix is a palindrome. If it is a
palindrome, then reverse the remaining prefix and check if it's in the list. If it is,
then this is an example of case 2.

    3. For each prefix of word, check if the prefix is a palindrome. If it is a
palindrome, then reverse the remaining suffix and check if it's in the list. If it is,
then this is an example of case 3.

To ensure the implementation is efficient, we can put all the words into a hash table
with the word as the key and the original index as the value (as the output must be the
original indexes of the words).

Examples of case 1 can be found by reversing the current word and looking it up. One
edge case to be careful of is that if a word is a palindrome by itself, then we don't
want to add a pair that includes that same word twice. This case only comes up in case
1, because case 1 is the only case that deals with pairs where the words are of equal
length.

Examples of case 2 can be found by calling remaining_prefixes and then reversing each of
the prefixes found and looking them up.

Examples of case 3 can be found by calling remaining_suffixes and then reversing each of
the suffixes found and looking them up.

It would be possible to simplify further (not done here) by recognizing that case 1 is
really just a special case of case 2 and case 3. This is because the empty string is a
palindrome prefix/suffix of any word.

Complexity
==========

Time
----

palindromePairs(words): O(n * k^2), where n is the number of words and k is the length
of the longest word. Building the hash table takes O(n * k) time and each word takes
O(k) time to insert.

Space
-----

palindromePairs(words): O((n + k)^2).
"""


def sol(words):
    idx_map, sol = {word: i for i, word in enumerate(words)}, []

    def is_palindrome(word):
        return word == word[::-1]

    def remaining_prefixes(word):
        return [word[:i] for i in range(len(word)) if is_palindrome(word[i:])]

    def remaining_suffixes(word):
        return [word[i + 1 :] for i in range(len(word)) if is_palindrome(word[: i + 1])]

    for i, word in enumerate(words):
        reversed_word = word[::-1]
        if reversed_word in idx_map and i != idx_map[reversed_word]:
            sol.append([i, idx_map[reversed_word]])
        for prefix in remaining_prefixes(word):
            reversed_prefix = prefix[::-1]
            if reversed_prefix in idx_map:
                sol.append([i, idx_map[reversed_prefix]])
        for suffix in remaining_suffixes(word):
            reversed_suffix = suffix[::-1]
            if reversed_suffix in idx_map:
                sol.append([idx_map[reversed_suffix], i])
    return sol
