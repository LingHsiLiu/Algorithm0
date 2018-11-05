# 616. Course Schedule II
# There are a total of n courses you have to take, labeled from 0 to n - 1.
# Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

# Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

# There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

# Example
# Given n = 2, prerequisites = [[1,0]]
# Return [0,1]

# Given n = 4, prerequisites = [1,0],[2,0],[3,1],[3,2]]
# Return [0,1,2,3] or [0,2,1,3]


import heapq
class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: the course order
    """
    def findOrder(self, numCourses, prerequisites):
        # write your code here
        edges = {i: [] for i in range(numCourses)}
        degrees = [0 for i in range(numCourses)] 
        for i, j in prerequisites:
            edges[j].append(i)
            degrees[i] += 1
        import queue
        queue = queue.Queue(maxsize = numCourses)
        
        for i in range(numCourses):
            if degrees[i] == 0:
                queue.put(i)

        order = []
        while not queue.empty():
            node = queue.get()
            order.append(node)

            for x in edges[node]:
                degrees[x] -= 1
                if degrees[x] == 0:
                    queue.put(x)

        if len(order) == numCourses:
            return order
        return []
