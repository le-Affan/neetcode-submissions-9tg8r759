class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        minCap = max(weights)
        maxCap = sum(weights)

        def checkCap(arr: List[int], maxDays: int, currCap: int) -> bool:
            total = 0
            currDays = 0

            for i in arr:
                total += i

                if total == currCap:
                    total = 0
                    currDays += 1
                elif total > currCap:
                    total = i
                    currDays += 1

                if currDays > maxDays:
                    return False

            return True
        
        while minCap <= maxCap:
            mid = (minCap + maxCap) // 2
            x = checkCap(weights, days, mid)

            if x:
                maxCap = mid - 1
            else:
                minCap = mid + 1
        
        return mid



