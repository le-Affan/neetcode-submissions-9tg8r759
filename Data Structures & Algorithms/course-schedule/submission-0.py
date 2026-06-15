class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:       
        mapping = defaultdict(list)       
        for i in prerequisites:
            mapping[i[0]].append(i[1])
        

        visiting = set() # Recursion stack to detect loops

        # This dfs will run on each of the COURSE
        # For each course the prerequisite will again be treated as am individual course
        def dfs(crs):
            if crs in visiting: # Loop detected
                return False
            if mapping[crs] == []: # It is a completable course
                return True
            
            visiting.add(crs)

            for pre in mapping[crs]:
                if not dfs(pre):
                    return False
            visiting.remove(crs)
            mapping[crs] = [] # Indicates that the course can be completed
            return True
        

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True           
