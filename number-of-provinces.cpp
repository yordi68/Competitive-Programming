class Solution {
private:
    void dfs(int node, vector<vector<int>>& adjList, vector<int> &vis){
        vis[node] = 1;
        for(auto it : adjList[node]){
            if(!vis[it]){
                dfs(it, adjList, vis);
            }
        }

    }

    // space complexity: 0(n) + 0(n) -> 0(n)
    // 0(n) -> visited array
    // 0(n) -> recursion stack space
    // time complexity: 0(n) + 0(V + 2E)
public:
    int findCircleNum(vector<vector<int>>& isConnected) {
        int n = isConnected[0].size();
        vector<vector<int>> adjList(n);

        // to change the adjacency matrix into adjacency list
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                if(isConnected[i][j] && i != j){
                    adjList[i].push_back(j);
                    adjList[j].push_back(i);
                }
            }
        }
        
        vector<int> vis(n, 0);
        int cnt = 0;
        for(int i = 0; i < n; i++){
            if(!vis[i]){
                cnt ++;
                dfs(i, adjList, vis);
            }
        }

        return cnt;


    }
};