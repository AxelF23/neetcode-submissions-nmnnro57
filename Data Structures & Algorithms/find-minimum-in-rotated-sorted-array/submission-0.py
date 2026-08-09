class Solution:
    def findMin(self, nums: List[int]) -> int:
        def binary(l,r):
            mid = (l + r) // 2
            if l == r:
                return nums[l]
            if nums[mid] < nums[r]:
                return binary(l, mid)
            elif nums[mid] > nums[r]:
                return binary(mid+1, r)
        return binary(0, len(nums) - 1)
