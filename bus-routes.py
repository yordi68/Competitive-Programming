class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        adjList = defaultdict(list)

        for i in range(len(routes)):
            for j in routes[i]:
                adjList[j].append(i)
    

        queue = deque([(source, 0)])
        visitedStation = set([source])
        visitedBuses = set()
        

        while queue:
            station, buses = queue.popleft()

            if station == target:
                return buses 

            for nxtBuses in adjList[station]:
                if nxtBuses not in visitedBuses:
                    for stations in routes[nxtBuses]:
                        if stations not in visitedStation:
                            visitedStation.add(stations)
                            queue.append((stations, buses + 1))

                    visitedBuses.add(nxtBuses)

        return -1