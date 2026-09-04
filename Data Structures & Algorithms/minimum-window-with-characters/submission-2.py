from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        need = Counter(t)
        window = Counter()
        required = len(need)
        formed = 0
        best_len = float('inf')
        best_left = 0
        for right in (range(len(s))):
            window[s[right]] += 1
            if s[right] in need and window[s[right]] == need[s[right]]:
                formed += 1
            while formed == required:
                if right - left + 1 < best_len:
                    best_len = right - left + 1
                    best_left = left
                if s[left] in need and window[s[left]] == need[s[left]]:
                    formed -= 1
                window[s[left]] -= 1
                left += 1
        if best_len == float('inf'):
            return ""
        return s[best_left : best_left + best_len]