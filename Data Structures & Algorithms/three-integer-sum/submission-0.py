class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        out = set()
        nums.sort()
        for i in range(len(nums)):
            left,right = i+1, len(nums) - 1
            while left < right:
                if nums[left] + nums[right] > -nums[i]:
                    right -= 1
                elif nums[left] + nums[right] < -nums[i]:
                    left +=1
                else: 
                    out.add((nums[left], nums[right], nums[i]))
                    left +=1
                    right -=1

        return [list(triplet) for triplet in out]