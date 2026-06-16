class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out_dict={}
        for i in range(len(nums)):
            ind=nums[:i]+nums[i+1:]
            out_dict[nums[i]]=ind
        out_arr=[]
        for value in out_dict.values():
            prod=1
            for i in value:
                prod*=i
            out_arr.append(prod)
        return out_arr








            
        