class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        resultHeap = []
        for i in nums:
            heapq.heappush(resultHeap, i)
            if len(resultHeap) > k:
                heapq.heappop(resultHeap)

        return resultHeap[0]
