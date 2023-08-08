class Solution {
public:
    int numEnclaves(vector<vector<int>>& grid) {

        int n = grid.size();
        int m = grid[0].size();
        // int vis[n][m] = {0};
        vector<vector<int>> vis(n, vector<int>(m, 0));
        queue<pair<int, int>> q;

        for(int i = 0; i < n; i++){
            for(int j = 0; j < m; j++){
                if(i == 0 || j == 0 || i == n - 1 || j == m - 1){
                    if(grid[i][j] == 1){
                        q.push({i, j});
                        vis[i][j] = 1;

                    }
                }
            }
        }

        vector<pair <int, int>> directions{{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        // int delrow[] = {-1, 0, 1, 0};
        // int delcol[] = {0, 1, 0, -1};
        
        while(!q.empty()){
            int row = q.front().first;
            int col = q.front().second;
            q.pop();

            for(auto dxn : directions){
                int nrow = row + dxn.first;
                int ncol = col + dxn.second;
                if(nrow >= 0 && nrow < n && ncol >= 0 && ncol < m && 
                    vis[nrow][ncol] == 0 && grid[nrow][ncol] == 1){

                    q.push({nrow, ncol});
                    vis[nrow][ncol] = 1;
                }
            }
        }
        // counting the differences b/n the vis array and the grid array
        int cnt = 0;
        for(int i = 0; i < n; i++){
            for(int j = 0; j < m; j++){
                if(vis[i][j] == 0 && grid[i][j] == 1){
                    cnt++;
                }
            }
        }

        return cnt;
    }
};