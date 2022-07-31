"""
Valid Palindrome II
-------------------

Given a string s, return true if the s can be palindrome after deleting at most one
character from it.

Intuition
---------

Let's assume we have some string s = 'abbxa'. On its own, s is not a palindrome.
However, if we delete the 'x', then s becomes 'abba', which is a palindrome. If we use
the same algorithm in checkPalindrome, we will see that the first and last characters
match as 'a'. The pointers move inwards, and the "new" string we're focused on is 'bbx'.

The next check will be a mismatch - 'b' != 'x'. This means that our original string is
not a palindrome. However, we can delete one character. If s can be a palindrome after
one deletion, the deletion must be of one of these mismatched characters. Deleting the
character 'b' gives us 'bx', and deleting the character 'x' gives us 'bb'. Because 'bb'
is a palindrome (which we can verify using checkPalindrome), the original string 'abbxa'
can become a palindrome with at most one character deletion.

This leaves us two scenarios:

    1. s is a palindrome - great, we can just return true.

    2. Somewhere in s, there will be a pair of mismatched characters. We must use our
allowed deletion on one of these characters. Try both options - if neither results in a
palindrome, then return false. Otherwise, return true. We can "delete" the character at
j by moving our bounds to (i, j - 1). Likewise, we can "delete" the character at i by
moving our bounds to (i + 1, j).

NB: If we can remove at most k characters, then the approach is to reverse the given
string and find maximum subsequence length between the two. The string is k-palindromic
if the difference between the string length and subsequence length is not more then k.
(time O(n^2), space O(n)).

Complexity
==========

Time
----

validPalindrome(s): O(n).

Space
-----

validPalindrome(s): O(1).
"""


def sol(s):
    def check(i, j, removed=True):
        while i < j:
            if s[i] != s[j]:
                return False if removed else check(i + 1, j) or check(i, j - 1)
            i += 1
            j -= 1
        return True

    return check(0, len(s) - 1, False)
