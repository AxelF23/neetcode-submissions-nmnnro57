class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, suffix = [1]*len(nums), [1]*len(nums)
        for i in range(len(nums)):
            if i > 0:
                prefix[i] = prefix[i-1]*nums[i-1]
            j = len(nums) - i - 1
            if j < len(nums) - 1:
                suffix[j] = suffix[j+1]*nums[j+1]
        answer = [prefix[i]*suffix[i] for i in range(len(nums))]
        return answer