class ThroneInheritance:

    def __init__(self, kingName: str):
        self.adjList = defaultdict(list)
        self.deathList = set()
        self.kingName = kingName

    def birth(self, parentName: str, childName: str) -> None:
        self.adjList[parentName].append(childName)

    def death(self, name: str) -> None:
        self.deathList.add(name)

    def getInheritanceOrder(self) -> List[str]:
        self.inheritanceOrder = []
        if len(list(self.adjList.keys())) > 0:
            self.dfs(list(self.adjList.keys())[0])
        else:
            return [self.kingName]

        return self.inheritanceOrder

    def dfs(self, king):
        if king not in self.deathList:
            self.inheritanceOrder.append(king)

        for succesor in self.adjList[king]:
            self.dfs(succesor)

        

# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()