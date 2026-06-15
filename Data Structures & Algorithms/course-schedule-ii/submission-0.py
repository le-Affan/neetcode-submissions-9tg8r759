class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []

        mapping = defaultdict(list)
        for a, b in prerequisites:
            mapping[a].append(b)

        visiting = set()

        def dfs(course):
            if course in visiting: # Loop detected
                return False
            if mapping[course] == []: # Already completed OR no prerequisites
                if course not in res: # Prevents duplicates
                    res.append(course)
                return True

            visiting.add(course)

            for pre in mapping[course]:
                if not dfs(pre): return False

            visiting.remove(course)
            mapping[course] = []   # Mark as completed in the hashmap
            res.append(course)     # Postorder append
            return True

        for course in range(numCourses):
            if not dfs(course): return []

        return res
