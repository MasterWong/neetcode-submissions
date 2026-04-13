class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        listS = list(s)
        listT = list(t)
        freqS = {}
        for letter in listS:
            if letter in freqS:
                freqS[letter] += 1
            else:
                freqS[letter] = 1

        for letter in listT:
            if letter not in freqS.keys():
                return False
            elif freqS[letter] == 1:
                del freqS[letter]
            else :
                freqS[letter] -= 1
        
        if len(freqS) == 0:
            return True
        else:
            return False
