#include <vector>
#include <algorithm>


using namespace std;


class Solution {
public:
    int getMaximumConsecutive(vector<int>& coins) {
        sort(coins.begin(), coins.end());
        int ans = 1;
        for(int x: coins){
            if(x > ans) break;
            ans += x;
        }
        return ans;
    }
};
