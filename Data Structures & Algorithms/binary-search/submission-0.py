class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_helper(left, right):
            if left > right:
                return -1
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return binary_helper(left,mid-1)
            elif nums[mid] < target:
                return binary_helper(mid+1, right)
        return binary_helper(0, len(nums) - 1)
        