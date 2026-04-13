class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1

        for a in range(2, n+1):
            dp[a] = dp[a-2] + dp[a-1]

        return dp[n]