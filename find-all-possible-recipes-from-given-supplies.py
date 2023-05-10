class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(list)
        dependency = defaultdict(int)
        queue = deque()
        dinner = []

        for i in range(len(ingredients)):
            dependency[recipes[i]] += len(ingredients[i])
            for ingredient in ingredients[i]:
                graph[ingredient].append(recipes[i])


        queue.extend(supplies)

        while queue:
            curr = queue.popleft()

            for neighbour in graph[curr]:
                dependency[neighbour] -= 1

                if dependency[neighbour] == 0:
                    queue.append(neighbour)
                    dinner.append(neighbour)


        return dinner