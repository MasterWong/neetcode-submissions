class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        substring = []
        for c in s:
            if c not in substring:
                substring.append(c)
                longest = max(longest, len(substring))
            else:
                idx = substring.index(c)
                substring = substring[idx+1:]
                substring.append(c)

        return longest