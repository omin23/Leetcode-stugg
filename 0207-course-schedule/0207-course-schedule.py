from collections import defaultdict 
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        mapper = defaultdict(list)
        for i in prerequisites: 
            mapper[i[0]].append(i[1])

        visited = set()
        def dfs(course):
            if course in visited: return False
            if mapper[course] == []: return True

            visited.add(course)
            for i in mapper[course]:
                if not dfs(i): return False
            visited.remove(course)
            mapper[course] = []
            return True

        for j in range(numCourses):   
            if not dfs(j): return False
        return True


