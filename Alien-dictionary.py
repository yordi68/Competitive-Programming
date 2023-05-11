        topo = self.topoSort(K, adj)
        ans = ""
        for node in topo:
            ans += chr(node + ord('a'))
        return ans