class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = defaultdict(list)
        incoming = defaultdict(int)
        queue = deque()
        order = []
        for course, pre in prerequisites:
            graph[pre].append(course)
            incoming[course] += 1

        for course in range(numCourses):
            if incoming[course] == 0:
                queue.append(course)

        
        while queue:
            currCourse = queue.popleft()
            order.append(currCourse)

            for neighbour in graph[currCourse]:
                incoming[neighbour] -= 1
                if incoming[neighbour] == 0:
                    queue.append(neighbour)

        if len(order) != numCourses:
            return False

        return True