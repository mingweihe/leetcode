#include <vector>

using namespace std;

class Solution {
public:
    int maxAscendingSum(vector<int>& nums) {
        int cur = nums[0], ans = nums[0];
        for(int i = 1; i < nums.size(); ++i){
            if(nums[i] <= nums[i-1]){
                ans = max(ans, cur);
                cur = nums[i];
            }else cur += nums[i];
        }
        return max(cur, ans);
    }
};
