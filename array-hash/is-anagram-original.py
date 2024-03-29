class Solution(object):
    """
    - story (of problem in terms of what should do): check if anagrams of each other
    - input: two strings
    - output: boolean
    - Requirements: return true if anagrams, false if not
    - Constraints that could help:
    - base cases: if different length then not same
    - Algo (thinking of): use hashSets --> 
    - what is an anagram --> same leters and same amount of all letters
    - maybe make a dictionary and then see is same
    - 
    - better runtime and MUCH BETTER memory than tricks one because of not needing length or anything as it just iterates through until hits end
    """
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        dictS = {}
        #goes through s and then if the letter is in dict, then adds 1 to count, otherwise, creates new entry
        for i in s:
            if i in dictS:
                dictS[i] += 1
            else:
                dictS[i] = 1
        
        dictT = {}
        for i in t:
            if i in dictT:
                dictT[i] += 1
            else:
                dictT[i] = 1

        return dictT == dictS #returns true is anagrams and false otherwise

