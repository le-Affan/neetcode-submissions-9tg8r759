class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Logic is that you iterate through each element and then perform the Two Sum II algorithm for all elements after the current element
        nums = sorted(nums)
        res = []

        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i - 1]: # Makes sure the 'Element Number - 1' of each triplet is always different hence avoids duplicates
                l, r = i + 1 , len(nums) - 1
                
                while l < r:
                    total = nums[i] + nums[l] + nums[r]
                    ind = {i, l, r}

                    if total == 0 and len(ind) == 3: # Ensures all 3 indices are different
                        triplet = [nums[i], nums[l], nums[r]]
                        res.append(triplet)
                        l += 1

                    elif total >= 0 and len(ind) == 3:
                        r -= 1

                    else:
                        l += 1
            else:
                continue

        res = list({tuple(x) for x in res}) # Gets rid of any duplicates that might have slipped in from edge cases

        return res


                
