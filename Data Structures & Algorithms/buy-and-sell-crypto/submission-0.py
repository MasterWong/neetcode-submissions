class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfitValue = 0
        currMin = prices[0]
        for i in prices:
            currDif = max(0, i - currMin)
            maxProfitValue = max(maxProfitValue, currDif)
            if i < currMin:
                currMin = i

        return maxProfitValue
