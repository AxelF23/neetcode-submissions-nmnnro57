import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        result = []
        for right in range(len(nums)):
            heapq.heappush(heap, (-nums[right], right))
            left_bound = right - k + 1
            while heap[0][1] < left_bound:
                heapq.heappop(heap)
            if right >= k - 1:
                result.append(-heap[0][0])
        return result