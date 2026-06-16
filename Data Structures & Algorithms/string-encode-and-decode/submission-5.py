class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded = ""

        for i in strs:
            encoded += f"#{len(i)}{i}"
        
        return encoded


    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        
        while i < len(s):
            if s[i] == "#":
                i += 1
                length_str = ""
                
                while i < len(s) and s[i].isdigit():
                    length_str += s[i]
                    i += 1
                
                length = int(length_str)
                word = s[i:i+length]
                decoded.append(word)
                
                i += length

        return decoded






                

