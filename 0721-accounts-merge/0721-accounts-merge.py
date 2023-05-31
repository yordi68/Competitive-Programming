class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = {}
        size = defaultdict(int)
        ans = []
        name_email = {}


        for i in range(len(accounts)):
            for j in range(1,len(accounts[i])):
                if accounts[i][j] not in parent:
                    parent[accounts[i][j]] = accounts[i][j]
                    name_email[accounts[i][j]] = accounts[i][0]
                    size[accounts[i][j]] += 1

        


        def find(node):
            if parent[node] == node:
                return node

            allParent = find(parent[node])
            parent[node] = allParent

            return allParent

        def union(From, To):
            parentFrom = find(From)
            parentTo = find(To)

            if parentFrom == parentTo:
                return
            if size[parentFrom] > size[parentTo]:
                parent[parentTo] = parentFrom
                size[parentFrom] += size[parentTo]
            else:
                parent[parentFrom] = parentTo
                size[parentTo] += size[parentFrom]

        for i in range(len(accounts)):
            if len(accounts[i]) > 1:
                for j in range(1, len(accounts[i]) - 1):
                    union(accounts[i][j], accounts[i][j + 1])
        
        parentHub = defaultdict(set)


        for pr in parent:
            parentHub[find(pr)].add(pr)

        for key in parentHub.keys():
            lst = [name_email[key]] + sorted(list(parentHub[key]))
            print(lst)
            ans.append(lst)

        return ans


















        