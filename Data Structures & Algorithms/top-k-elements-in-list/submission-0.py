class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        vals=sorted(list(set(nums)),reverse=True)

        lst=[]
        for i in range(0,k):
            lst.append(vals[i])
        return lst
