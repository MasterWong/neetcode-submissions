class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(listOfNums):
            if len(listOfNums) == 1:
                return [listOfNums[:]]
            n = listOfNums.pop(0)
            perm = dfs(listOfNums)
            res = []
            for p in perm:
                for i in range(len(p) + 1):
                    temp = p[:]
                    temp.insert(i, n)
                    res.append(temp)
            return res
            
        return dfs(nums)