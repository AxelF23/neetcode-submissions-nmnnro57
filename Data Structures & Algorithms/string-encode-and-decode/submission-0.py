class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s))+'#'+s
        return encoded
    def decode(self, s: str) -> List[str]:
        decoded = []
        lens =""
        i = 0
        while i < len(s):
            if s[i] != '#':
                lens += s[i]
                i+=1
            elif s[i] == "#":
                decoded.append(s[i+1 : i + int(lens) + 1])
                i = i + int(lens) + 1
                lens = ""
        return decoded        
