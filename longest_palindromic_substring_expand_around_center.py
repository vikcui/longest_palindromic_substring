# author : YANG CUI
"""
Approach: Expand Around Center
In fact, we could solve it in O(n^2) time using only constant space.
We observe that a palindrome mirrors around its center.
Therefore, a palindrome can be expanded from its center, and
there are only 2n − 1 such centers.
You might be asking why there are 2n - 12n−1 but not nn centers?
The reason is the center of a palindrome can be in between two letters.
Such palindromes have even number of letters (such as "abba")
and its center are between the two 'b's.
"""

def expand_around_center(InputString):
    """
    :param InputString: the actual input string whose palindromic substring we wanna explore
    :return: the longest palindromic substring of that input string
    : time complexity : O(n^2)
    : space complexity : O(1)
    """
    # compute the length of the input string
    lenOfString = len(InputString)
    maxLen = 0
    maxString = ""
    for center in range(2 * lenOfString - 1):
        left = center // 2
        right = left + center % 2
        while left >= 0 and right < lenOfString and InputString[left] == InputString[right]:
            left -= 1
            right += 1
            if abs(right-1-left-1+1) > maxLen:
                maxLen = abs(right-1-left-1+1)
                maxString = InputString[left+1:right]
    # print(maxString)
    return maxString

expand_around_center("")