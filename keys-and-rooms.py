class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        queue = deque(num for num in rooms[0])
        visited = set()
        visited.add(0)

        while queue:
            curr = queue.popleft()
            visited.add(curr)
            
            for num in rooms[curr]:
                if num not in queue and num not in visited:
                    queue.append(num)

        return True if len(rooms) == len(visited) else False