class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dataMap = {}
        for i in nums:
            if i not in dataMap:
                dataMap[i] = 1
            else:
                return True
        
        return False