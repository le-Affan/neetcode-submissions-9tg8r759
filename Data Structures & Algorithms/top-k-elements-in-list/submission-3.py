class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        vals=sorted(list(set(nums)),reverse=True)

        count = defaultdict(int)

        for i in nums:
            count[i] += 1
        
        final = sorted(count , key = count.get, reverse = True)

        return final[:k]