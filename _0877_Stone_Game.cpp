#include <bits/stdc++.h>

using namespace std;


class Solution {
public:
    int dp[500][500];
    int dfs(int l, int r, vector<int>& piles){
        if(l > r) return 0;
        if(dp[l][r] != -1) return dp[l][r];
        int pickLeft = piles[l] + min(dfs(l+2, r, piles), dfs(l+1, r-1, piles));
        int pickRight = piles[r] + min(dfs(l+1, r-1, piles), dfs(l, r-2, piles));
        dp[l][r] = max(pickLeft, pickRight);
        return dp[l][r];
    }
    
    bool stoneGame(vector<int>& piles) {
        memset(dp, -1, sizeof(dp));
        int sum = accumulate(piles.begin(), piles.end(), 0);
        int alex = dfs(0, piles.size()-1, piles);
        int lee = sum - alex;
        return alex > lee;
    }
};
