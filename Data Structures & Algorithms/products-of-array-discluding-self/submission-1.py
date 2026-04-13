class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixResult = [1]*len(nums)
        for index in range(1, len(nums)):
            prefixResult[index] = prefixResult[index - 1] * nums[index - 1]
        
        suffixResult = [1] * len(nums)
        for index in range(len(nums) - 2, -1, -1):
            suffixResult[index] = suffixResult[index + 1] * nums[index + 1]
        
        result = []
        for i in range(len(nums)):
            result.append(prefixResult[i]*suffixResult[i])

        return result
        