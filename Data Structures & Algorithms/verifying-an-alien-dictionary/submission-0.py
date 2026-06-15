class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        mapping = defaultdict(int)

        res = []

        count = 1
        for i in order:
            mapping[i] = count
            count += 1
        
        for word in words:
            n = []
            for c in word:
                n.append((mapping[c]))
            res.append(n)
        
        isLex = True
        curr = []
        for i in res:
            if i >= curr:
                curr = i
            else:
                isLex = False
                break
        return isLex