class Solution {
private:
    bool check(int start, vector<vector<int>>&  adj, vector<int>& col){
        queue<int> q;
        q.push(start);
        col[start] = 0;

        while(!q.empty()){
            int node = q.front();
            q.pop();

            for(auto adjNode: adj[node]){
                // if the adjacent node is yet no colored
                // you will give the opposite color of the node
                if(col[adjNode] == -1){
                    col[adjNode] = !col[node];
                    q.push(adjNode);
                }
                // if the adjacent have the same color
                // some one else colored it in another path
                else if(col[adjNode] == col[node]){
                    return false;
                }
            }
        }

        return true;
    }
public:
    bool isBipartite(vector<vector<int>>& graph) {
        int n = graph.size();
        vector<int> col(n, -1);
        
        for(int i = 0; i < n; i++){
            if(col[i] == -1){
                if(check(i, graph, col) == false){
                    return false;
                };
            }
        }

        return true;

    }
};