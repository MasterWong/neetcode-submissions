class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strList = list(strs)
        ansDict = {}
        for string in strList:
            key = [0] * 26
            for char in string:
                key[ord(char) - ord('a')] += 1
            dictKey = tuple(key)
            if dictKey in ansDict:
                ansDict[dictKey].append(string)
            else:
                ansDict[dictKey] = [string]
        ans = []
        for lst in ansDict.values():
            ans.append(lst)

        return ans