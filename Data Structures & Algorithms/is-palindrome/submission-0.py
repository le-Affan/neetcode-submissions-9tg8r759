class Solution:
    def isPalindrome(self, s: str) -> bool:
        act_string = list(c.lower() for c in s if c.isalnum())

        l,r = 0,(len(act_string)-1)

        while l<r:
            if act_string[l] == act_string[r]:
                l += 1
                r -= 1
            elif act_string[l] != act_string[r]:
                return False
            
        if l>=r:
            return True

