class Solution:
    def isPalindrome(self, s: str, l: int, r: int) -> bool:

        while l <= r:
            if s[l] and s[r]:
                if s[l] == s[r]:
                    l += 1
                    r -= 1
                else:
                    return False
            else:
                if not s[l]:
                    l += 1
                if not s[r]:
                    r -= 1
        return True

    def partition(self, s: str) -> List[List[str]]:
        res = []

        part = []

        

        def dfs(i):
            if i >= len(s):
                res.append(part.copy())
                return
            
            for j in range(i, len(s)):
                if self.isPalindrome(s, i, j):
                    part.append(s[i:j+1])
                    dfs(j + 1)
                    part.pop()
        dfs(0)
        return res
