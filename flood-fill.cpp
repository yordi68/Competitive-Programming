class Solution {
public:
    vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int color) {
        int n = image.size();
        int m = image[0].size();
        int mainColor = image[sr][sc];

        vector<pair <int, int>> directions{{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        vector<vector<int>> vis(n, vector<int>(m,0));
        queue<pair<int, int>> q;
        q.push({sr, sc});
        image[sr][sc] = color; 
        vis[sr][sc] = 1;

        while(!q.empty()){
            int row = q.front().first;
            int col = q.front().second;
            q.pop();
            for(auto dxn : directions){
                int newRow = row + dxn.first;
                int newCol = col + dxn.second;
                if(newRow >= 0 && newRow < n && newCol >= 0 && newCol < m && image[newRow][newCol] == mainColor){
                        if(vis[newRow][newCol] == 0){
                        q.push({newRow, newCol});
                        image[newRow][newCol] = color;
                        vis[newRow][newCol]=1;
                        }

                }
            }
        }

        return image;
    }
};