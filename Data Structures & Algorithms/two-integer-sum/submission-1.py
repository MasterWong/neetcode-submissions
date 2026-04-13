class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = {}
        for index, number in enumerate(nums):
            result[target - number] = index

        for index, number in enumerate(nums):
            if number in result.keys():
                if index != result[number]:
                    return [index, result[number]]
        