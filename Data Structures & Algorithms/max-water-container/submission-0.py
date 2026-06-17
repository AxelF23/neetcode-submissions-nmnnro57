class Solution:
    def maxArea(self, h: List[int]) -> int:
        l = 0
        r = len(h) - 1
        max_s = 0
        while l < r:
            min_h = min(h[l], h[r])
            s = (r-l)*min_h
            if min_h == h[l]:
                l += 1
            else:
                r -= 1
            max_s = max(max_s, s)
        return max_s