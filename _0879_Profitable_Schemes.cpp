#include <bits/stdc++.h>

using namespace std;
#define ll long long


class Solution {
public:
    int profitableSchemes(int n, int minProfit, vector<int>& group, vector<int>& profit) {
        int mod = 1e9+7;
        int T = group.size(); // number of tasks / crimes
        ll dp[T+1][minProfit+1][n+1];
        memset(dp, 0, sizeof(dp));
        dp[0][0][0] = 1;
        for(int i = 1; i <= T; ++i){
            int g = group[i-1], p = profit[i-1];
            for(int j = 0; j <= minProfit; ++j){
                for(int k = 0; k <= n; ++k){
                    dp[i][j][k] = dp[i-1][j][k];
                    if(k < g) continue;
                    dp[i][j][k] = (dp[i][j][k] + dp[i-1][max(0, j-p)][k-g]) % mod;
                }
            }
        }
        return accumulate(dp[T][minProfit], dp[T][minProfit]+n+1, 0ll) % mod;
    }
};
