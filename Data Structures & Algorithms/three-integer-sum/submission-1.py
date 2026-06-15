class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []

        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i - 1]:
                l, r = i , len(nums) - 1
                
                while l < r:
                    ind = {i, l, r}
                    if nums[i] + nums[l] + nums[r] == 0 and len(ind) == 3:
                        triplet = []
                        triplet.append(nums[i])
                        triplet.append(nums[l])
                        triplet.append(nums[r])
                        res.append(triplet)
                        l += 1
                    elif nums[i] + nums[l] + nums[r] >= 0 and len(ind) == 3:
                        r -= 1
                    else:
                        l += 1
            else:
                continue
        res = list({tuple(x) for x in res})
        return res


                
