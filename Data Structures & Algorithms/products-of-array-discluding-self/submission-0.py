class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        numOfZeroes = 0
        for i in nums:
            if i == 0:
                numOfZeroes += 1
                continue
            total = total * i

        result = []
        if numOfZeroes == 1:
            for i in nums:
                if i != 0:
                    result.append(0)
                else:
                    result.append(total)
            return result

        if numOfZeroes >= 2:
            return [0]*len(nums)
        
        for i in nums:
            result.append(total//i)

        return result