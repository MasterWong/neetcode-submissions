class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []
        def dfs(i, carry):
            if i >= len(nums):
                answer.append(carry.copy())
                return
            dfs(i+1, carry+[nums[i]])
            dfs(i+1, carry)
        initial = []
        dfs(0, initial)
        return answer