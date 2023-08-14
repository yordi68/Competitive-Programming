class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
    
        int n = grid.size();
        int m = grid[0].size();

        vector<vector<int>>vis(n , vector<int>(m,0));

        // {{row, col}, time}
        queue< pair < pair <int, int>, int >> q;
        int cntFresh = 0;

        for(int i = 0; i < n; i++){
            for(int j = 0; j < m; j++){
                if(grid[i][j] == 1){
                    cntFresh++;
                }
                else if(grid[i][j] == 2){
                    q.push({{i, j}, 0});
                    vis[i][j] = 2;
                }
            }
        }

        int totalTime = 0;
        vector<pair<int, int>> directions{{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        int cnt = 0;

        while(!q.empty()){
            
            auto [row,col] = q.front().first;
            int time = q.front().second;
            
            totalTime = max(time, totalTime);
            q.pop();

            for(auto [r,c] : directions){
                int nrow = r + row;
                int ncol = c + col;

                if(nrow >= 0 && nrow < n && ncol >= 0 && ncol < m &&
            vis[nrow][ncol] == 0 && grid[nrow][ncol] == 1){
                    q.push({{nrow, ncol}, time + 1});
                    vis[nrow][ncol] = 2;
                    cnt++;
                }
            }

        }

        if(cntFresh != cnt){
            return -1;
        }
        return totalTime;

    }
};