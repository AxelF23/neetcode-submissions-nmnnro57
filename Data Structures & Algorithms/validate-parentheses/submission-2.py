class Solution:
    def isValid(self, s: str) -> bool:
       stack = []
       opens = set(("(", "[", "{"))
       brackets = {")": "(", "]": "[", "}": "{"}
       for symb in s:
        if symb in opens:
            stack.append(symb)
        else:
            if not stack or stack[-1] != brackets[symb]:
                return False
            stack.pop()
       return len(stack) == 0