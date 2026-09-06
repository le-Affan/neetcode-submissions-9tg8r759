class Solution:

    def encode(self, strs: List[str]) -> str:
        return ''.join('#' + str(len(w)).zfill(3) + w for w in strs)

    def decode(self, s: str) -> List[str]:
        res = []

        i = 0
        while i < len(s):
            if s[i] == "#":
                curr = int(s[i + 1:i + 4])
                res.append(s[i + 4: i + 4 + curr])
                i += 4 + curr
        
        return res

