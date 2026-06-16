class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        lst=[]

        for i in range(len(numbers)-1):
            l=i
            r=l+1
            while l<=len(numbers)-1:
                if numbers[l]+numbers[r]==target:
                    lst.append(l)
                    lst.append(r)
                    return lst
                else:
                    r += 1
            
            



        