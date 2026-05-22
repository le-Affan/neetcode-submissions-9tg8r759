class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        currSum = 0
        prefix = {0 : 1}
        res = 0

        for i in nums:
            currSum += i

            if (currSum - k) in prefix.keys():
                res += prefix[currSum - k]
            
            if currSum in prefix.keys():
                prefix[currSum] += 1
            
            else:
                prefix[currSum] = 1
            
        return res
            
            