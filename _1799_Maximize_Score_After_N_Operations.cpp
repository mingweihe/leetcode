#include <vector>
#include <cmath>
#include <numeric>

using namespace std;


class Solution {
public:
    // top down dp, using array to store the ans for sub problems, O(n*2^(2n)*(2n)^2)
    int dp[8][16384] = {};
    int maxScore(vector<int>& nums, int idx = 1, int mask = 0) {
        if(idx > nums.size() / 2) return 0;
        if(dp[idx][mask]) return dp[idx][mask];
        for(int i = 0; i < nums.size()-1; ++i){
            for(int j = i+1; j < nums.size(); ++j){
                int new_mask = (1 << i) | (1 << j);
                if(new_mask & mask) continue;
                int cur_best = idx * gcd(nums[i], nums[j]) + maxScore(nums, idx+1, mask | new_mask);
                dp[idx][mask] = max(dp[idx][mask], cur_best);
            }
        }
        return dp[idx][mask];
    }
};
