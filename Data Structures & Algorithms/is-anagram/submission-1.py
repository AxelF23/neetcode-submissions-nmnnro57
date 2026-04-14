class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = dict()
        dict2 = dict()
        for ch in s:
            if ch in dict1:
                dict1[ch] += 1
            else:
                dict1[ch] = 1
        for ch in t:
            if ch in dict2:
                dict2[ch] += 1
            else:
                dict2[ch] = 1
        for ch in dict1:
            if len(dict1) != len(dict2) or ch not in dict2 or dict1[ch] != dict2[ch]:
                return False
        return True