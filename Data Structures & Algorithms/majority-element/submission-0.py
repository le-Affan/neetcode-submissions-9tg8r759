class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # My simple solution
        count = defaultdict(int)

        for i in nums:
            count[i] += 1
        
        target = len(nums) // 2

        for key,value in count.items():
            if value > target:
                return key