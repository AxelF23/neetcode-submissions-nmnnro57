class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = dict()
        for num in nums:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1
        val = sorted(dic, key = dic.get, reverse = True)
        return val[:k]