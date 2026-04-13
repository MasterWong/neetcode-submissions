class Solution:
    def search(self, nums: List[int], target: int) -> int:
        currIdx = len(nums) >> 1
        lp = 0
        rp = len(nums) - 1
        if target == nums[0]: return 0
        while lp <= rp:
            if nums[currIdx] == target:
                return currIdx
            elif nums[currIdx] < target:
                if lp == currIdx: break
                lp = currIdx
            else:
                if rp == currIdx: break
                rp = currIdx
            currIdx = (lp + rp + 1) >> 1
        return -1