class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 3:
            if sum(nums) == 0:
                return nums
            elif sum(nums) != 0:
                return []           

        freqs = Counter(nums)
        p1 = 0
        res = []

        while p1 < len(nums) - 1:
            p2 = p1 + 1
            while p2 < len(nums):
                freq[nums[p1]] -= 1
                freq[nums[p2]] -= 1
                curr = nums[p1] + nums[p2]

                if -1 * curr in freqs.keys() and freqs[(-1 * curr)] != 0:
                    new = sorted([nums[p1], nums[p2], -1 * curr])
                    if new not in res:
                        res.append(new)
                
                p2 += 1
            p1 += 1
        

        return res


