#include <iostream>
#include <vector>
#include <queue>
#include <unordered_map>
#include <algorithm>
using namespace std;
class Solution {
public:
    bool hasValidPath(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();

        queue<pair<int,int>> q;
        vector<vector<bool>> visited(m,vector<bool>(n,false));
        unordered_map<int,vector<pair<int,int>>> dirs = {
            {1, {{0, -1}, {0, 1}}},   // 1：左右
            {2, {{-1, 0}, {1, 0}}},   // 2：上下
            {3, {{0, -1}, {1, 0}}},   // 3：左 → 下
            {4, {{0, 1}, {1, 0}}},    // 4：右 → 下
            {5, {{0, -1}, {-1, 0}}},  // 5：左 → 上
            {6, {{0, 1}, {-1, 0}}}    // 6：右 → 上
        };

        q.push({0,0});
        visited[0][0] = true;

        while (!q.empty()){
            pair<int,int> loc = q.front();
            q.pop();
            int x = loc.first;
            int y = loc.second;

            if (x == m-1 && y == n-1){
                return true;
            }

            vector<pair<int,int>> available_dirs = dirs[grid[x][y]];
            for (pair<int,int>& dir : available_dirs){
                int x1 = x + dir.first;
                int y1 = y + dir.second;
                if (x1 >= 0 && x1 <= m-1 && y1 >= 0 && y1 <= n-1 && !visited[x1][y1] && (find(dirs[grid[x1][y1]].begin(),dirs[grid[x1][y1]].end(),make_pair(-dir.first, -dir.second)) != dirs[grid[x1][y1]].end())){
                    visited[x1][y1] = true;
                    q.push({x1,y1});
                }
            }
        }

        return false;
    }
};
int main(){
    Solution sol;
    vector<vector<int>> grid = {{2,4,3},{6,5,2}};
    cout << sol.hasValidPath(grid) << endl;
}