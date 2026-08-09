class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def flag(k, ar, h):
            sum = 0
            for a in ar:
                sum += (a + k -1) // k
                if sum > h:
                    return False
            return sum <= h
        def binary_helper(left, right, array, h):
            if left > right:
                return left
            mid = (left + right) // 2
            if flag(mid, array, h):
                return binary_helper(left, mid - 1, array, h)
            else:
                return binary_helper(mid + 1, right, array, h)
        return binary_helper(1, max(piles), piles, h)