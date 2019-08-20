# author : YANG CUI
# given an input string, return the longest palindromic substring
# contained in that string.

def longest_palindromic_substring_Dp(InputString):
    """
    :param InputString: the actual input string whose palindromic substring we wanna explore
    :return: the longest palindromic substring of that input string
    : time complexity : O(n^2)
    : space complexity : O(n^2)
    """
    # bottom up approach
    # compute the length of the input string
    lenOfString = len(InputString)
    # construct the DpTable
    DpTable = [[False]*lenOfString for i in range(lenOfString)]
    # initialize the DpTable (all the single char entries to be true)
    for i in range(lenOfString):
        DpTable[i][i] = True
    # basic loop structure to complete the fill in the DpTable
    currentLen = 1
    maxLen = lenOfString
    while currentLen < maxLen:
        for i in range(maxLen-currentLen):
            if currentLen == 1:
                DpTable[i][i+currentLen] = InputString[i] == InputString[i + currentLen]
            else:
                DpTable[i][i+currentLen] = (DpTable[i+1][i+currentLen-1] and InputString[i] == InputString[i+currentLen])
            # print(i,i+currentLen)
        currentLen+=1
    # check for max palindromic substring
    maxLen = 0
    maxString = ""
    for i in range(len(DpTable)):
        for j in range(i,len(DpTable)):
            if DpTable[i][j] == True and abs(j-i+1) > maxLen:
                maxLen = abs(j-i+1)
                maxString = InputString[i:j+1]

    return maxString

longest_palindromic_substring_Dp("cbbd")

