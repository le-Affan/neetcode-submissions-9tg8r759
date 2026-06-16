class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded = ""

        for i in strs:
            encoded += f"#{len(i)}{i}"
        
        return encoded


    def decode(self, s: str) -> List[str]:

        decoded=[]

        for i in range(len(s)):
            if s[i] == "#":
                j = int(s[i+1])
                word = ""
                word += s[(i+2):(i+j+2)]
                decoded.append(word)

                i = i+1+j
        
        return decoded






                

