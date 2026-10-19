class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:         

        freqs = Counter(nums)
        p1 = 0
        res = set()

        while p1 < len(nums) - 1:
            freqs[nums[p1]] -= 1
            p2 = p1 + 1
            while p2 < len(nums):
                freqs[nums[p2]] -= 1
                curr = nums[p1] + nums[p2]

                if -1 * curr in freqs.keys() and freqs[(-1 * curr)] != 0:
                    new = tuple(sorted([nums[p1], nums[p2], -1 * curr]))
                    if new not in res:
                        res.add(new)
                
                freqs[nums[p2]] += 1
                p2 += 1
            freqs[nums[p1]] += 1
            p1 += 1
        

        return [list(t) for t in res]


