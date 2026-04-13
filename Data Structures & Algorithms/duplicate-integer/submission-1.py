class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        totalDict = set()
        for i in nums:
            if i in totalDict:
                return True
            totalDict.add(i)

        return False