class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums2 = {}
        for idx, value in enumerate(nums):
            nums2[(target - value)] = idx
            
        print(nums2)

        for idx, value in enumerate(nums):
            print(value)
            if value in nums2.keys():
                if idx != nums2[value]:
                    returnValue = [idx, nums2[value]]
                    returnValue.sort()
                    return returnValue
        