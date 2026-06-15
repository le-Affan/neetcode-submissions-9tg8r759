class Solution:
    def twoSum(self, num: List[int], target: int) -> List[int]:
        l, r = 0, len(num) - 1

        while l < r:
            currSum = num[l] + num[r]

            if currSum == target:
                return [l + 1,r + 1]
            elif currSum < target:
                l += 1
            else:
                r -= 1
        