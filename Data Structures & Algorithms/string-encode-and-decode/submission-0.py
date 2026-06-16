class Solution:
    

    def encode(self, strs: List[str]) -> str:
        encoded='-'
        for i in strs:
            encoded=encoded+"-"+i
        encoded=encoded+'-'
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded=[]
        word=''

        for char in s:
            if char=='-':
                if len(word)!=0:
                    decoded.append(word)
                    word=''
                continue
            word=word+char
        
        return decoded

            





