class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        alphabet = ['a','b','c','d','e', 'f', 'g', 'h', 'i','j','k','l','m','n', 'o', 'p','q', 'r', 's', 't','u','v','w','x','y','z']
        strs = tuple(strs)
        dic = dict()
        for word in strs:
            vector = [0] * 26
            for ch in word:
                index = ord(ch) - ord('a')
                vector[index] += 1
            vector = tuple(vector)
            if vector in dic:
                dic[vector].append(word)
            else:
                dic[vector] = [word]
        lst = list()
        for group in dic.values():
            lst.append(group)
        return lst