# author : YANG CUI
# given an input string, return the longest palindromic substring
# contained in that string.

def checkPalindrome(stringToCheck):
    """
    :param stringToCheck:
    :return: True if stringToCheck qualifies as a palindrome, false otherwise.
    :complexity: O(n) n being the len of the input string
    """
    # compute the length of the input string
    lenOfString = len(stringToCheck)

    if lenOfString == 1:
        return True
    else:
        leftSubStringStartPos = 0
        leftSubStringEndPos = lenOfString // 2
        rightSubStringEndPos = lenOfString
        # if even length:
        if lenOfString % 2 == 0:
            rightSubStringStartPos = lenOfString // 2
        # if odd length:
        else:
            rightSubStringStartPos = leftSubStringEndPos + 1

        for i in range(leftSubStringStartPos, leftSubStringEndPos):
            if stringToCheck[leftSubStringStartPos + i] != stringToCheck[rightSubStringEndPos -1 - i]:
                return False
        return True


def longestPalindromicSubstring(InputString):
    """
    :param InputString: the actual input string whose palindromic substring we wanna explore
    :return: the longest palindromic substring of that input string
    : time complexity : O(n^3)
    : space complexity : O(1)
    """
    max_len = 0
    max_String = ""
    if InputString == "":
        return ""
    elif len(InputString) == 1:
        return InputString
    else:
        for i in range(len(InputString) - 1):
            for j in range(i + 1, len(InputString)):
                if checkPalindrome(InputString[i:j + 1]):
                    if len(InputString[i:j + 1]) > max_len:
                        max_len = len(InputString[i:j + 1])
                        max_String = InputString[i:j + 1]
        return max_String


print(longestPalindromicSubstring("abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababa"))



