class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * (1+len(cost))

        for a in range(2, 1+len(cost)):
            dp[a] = min(dp[a-2]+cost[a-2], dp[a-1]+cost[a-1])

        return dp[len(cost)]