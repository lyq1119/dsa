#include <iostream>
#include <vector>
#include <queue>
using namespace std;
class Solution {
public:
    int maxPathScore(vector<vector<int>>& grid, int k){
        int m = grid.size(), n = grid[0].size();
        vector<vector<int>> dp(n,vector<int>(k+1,-1));

        if (grid[0][0] == 0){
            dp[0][0] = 0;
        }else{
            dp[0][1] = grid[0][0];
        }

        for (int i = 0; i < m; i++){
            for (int j = 1; j < n; j++){
                if (grid[i][j] == 0){
                    for (int k1 = 0; k1 <= k; k1++){
                        if (dp[j-1][k1] >= 0){
                            dp[j][k1] = max(dp[j-1][k1],dp[j][k1]);
                        }
                    }
                }else{
                    for (int k1 = 1; k1 <= k; k1++){
                        if (dp[j-1][k1-1] >= 0){
                            dp[j][k1] = max(dp[j-1][k1-1] + grid[i][j],dp[j][k1]);
                        }
                    }
                    dp[j][0] = -1;
                }
            }

            if (i < m-1){
                for (int j = n-1; j >= 0; j--){
                    if (grid[i+1][j] != 0){
                        for (int k1 = k; k1 > 0; k1--){
                            if (dp[j][k1-1] >= 0){
                                dp[j][k1] = dp[j][k1-1] + grid[i+1][j];
                            } else{
                                dp[j][k1] = -1;
                            }
                        }
                        dp[j][0] = -1;
                    }
                }
            }

        }

        int ans = -1;
        for (int c = 0; c <= k; c++) {
            ans = max(ans, dp[n-1][c]);
        }
        return ans;
    }
};

int main(){
    Solution sol;
    vector<vector<int>> grid = {{0, 1},{1, 2}};
    int k = 1;
    cout << sol.maxPathScore(grid, k);
}