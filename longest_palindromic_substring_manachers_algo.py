# author: YANG CUI
"""
There is even an O(n)O(n) algorithm called Manacher's algorithm that finds the
longest palindromic substring.

Manacher's algorithm is a textbook algorithm that finds in linear time,
the maximum size palindrome for any possible palindrome center.
If we had such an algorithm, finding the answer is straightforward.
"""
def modifyString(InputString):
    """

    :param InputString: the string to be modified
    :return: modified string i.e (#a#b# if inputString its ab)
    :complexity O(n)
    """
    stringList = list(InputString)
    tempString = "#".join(stringList)
    modifiedString = "#"+tempString+"#"
    return modifiedString


def manachers_algorithm(InputString):
    # modify the string into the format we want
    InputString = modifyString(InputString)
    # The new length of the new string will always be 2 * N + 1 (odd!)
    stringLen = len(InputString)
    # construct the maxExpansionArray array to store max expansion lengths at each index
    maxExpansionArray = [0] * stringLen
    # c stores the center of the longest palindromic substring until now
    c = 0
    # r stores the right boundary of the longest palindromic substring until now
    r = 0
    # maxLen stores the length of the longest palindromic substring till n
    maxLen = 0
    maxString = ""
    # basic loop structure to fill in the maxExpansionArray
    for i in range(stringLen):
        # get mirror index of i, since mirror - c = c - i
        mirror = (2 * c) - i

        # see if the mirror index of i is expanding beyond the left boundry of the current longest palindromic substring at center c
        # if it is, then take r-i as maxExpansionArray[i]
        # else take P[mirror] as P[i]

        if i < r:
            maxExpansionArray[i] = min(r - i, maxExpansionArray[mirror])

        # expand at index i
        expandLeft = i - (1 + maxExpansionArray[i])
        expandRight = i + (1 + maxExpansionArray[i])
        while expandRight < stringLen and expandRight >= 0 and InputString[expandLeft] == InputString[expandRight]:
            maxExpansionArray[i] += 1
            expandLeft -= 1
            expandRight += 1

        # check if the expanded palindromic substring at i is expanding beyond the right boundry of the current longest palindromic substring at center c
        # if it is, update the new center to be i
        if i + maxExpansionArray[i] > r:
            c = i
            r = i + maxExpansionArray[i]
            # update maxLen and maxString
            if maxExpansionArray[i] > maxLen:
                maxLen = maxExpansionArray[i]
                maxString = InputString[c-maxExpansionArray[i]:c+maxExpansionArray[i]+1]

    # process the string to get rid of the # signs

    return maxString.replace("#","")


