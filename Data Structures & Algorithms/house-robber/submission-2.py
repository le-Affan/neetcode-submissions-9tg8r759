class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        Please watch NeetCode's video solution to understand.
        I can't help using comments for this one buddy:(
        '''

        rob1, rob2 = 0, 0 

        # [...rob1, rob2, n, n+1...]
        for n in nums:
            temp = max(n + rob1, rob2) # this will give the max until 'n'
            
            # moving rob1 and rob2 by one step basically
            rob1 = rob2 
            rob2 = temp
        return rob2
