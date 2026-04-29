class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
         mapping = {}
         p = 0

         while p < len(nums):
            if nums[p] in mapping.keys() and abs(p - mapping[nums[p]]) <= k:
                return True
            else:
                mapping[nums[p]] = p
                p += 1
        
         return False


        
        