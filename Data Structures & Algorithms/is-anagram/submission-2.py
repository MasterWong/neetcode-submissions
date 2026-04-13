class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False

        sList = [0] * 26
        tList = [0] * 26

        for char in s:
            sList[ord(char) - ord("a")] += 1

        for char in t:
            tList[ord(char) - ord("a")] += 1

        if sList == tList:
            return True
        else:
            return False 

        