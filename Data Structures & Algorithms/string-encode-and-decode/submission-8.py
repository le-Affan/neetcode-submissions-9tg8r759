class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            length = str(len(word)).zfill(3)   # Always 3 digits
            encoded += f"#{length}{word}"
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        
        while i < len(s):
            if s[i] == "#":
                i += 1
                # Always read exactly 3 digits for length
                length = int(s[i:i+3])
                i += 3
                word = s[i:i+length]
                decoded.append(word)
                i += length


        return decoded
