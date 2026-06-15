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

                    if total == 0: 
                        triplet = [nums[i], nums[l], nums[r]]
                        res.append(triplet)
                        l += 1
                        r -= 1
                        # You move both since you are never gonna find the same sum again for any other combination since the array is sorted
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1
                    elif total > 0 :
                        r -= 1

                    else:
                        l += 1
            else:
                continue

        return res


                
