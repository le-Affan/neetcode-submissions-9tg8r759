class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = (len(nums)) // 2

        freq = defaultdict(int)

        for i in nums:
            freq[i] += 1

            if freq[i] > n:
                return i