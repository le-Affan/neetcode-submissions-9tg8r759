class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        l, r = 0, len(people) - 1
        count = 0
        people = sorted(people)

        while l <= r:
            if l == r:
                count += 1
                break
            elif people[l] + people[r] > limit:
                count += 1
                r -= 1
            else:
                count += 1
                l += 1
                r -= 1
        return count
            
