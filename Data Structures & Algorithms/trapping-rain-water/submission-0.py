class Solution:
    def trap(self, height: List[int]) -> int:
        pl = 0
        pr = len(height) - 1
        lmax = height[pl]
        rmax = height[pr]
        res = 0
        while pr > pl:
            if height[pl] > height[pr]:
                pr -= 1
                rmax = max(rmax, height[pr])
                res += rmax - height[pr]
            else:
                pl += 1
                lmax = max(lmax, height[pl])
                res += lmax - height[pl]
        return res
