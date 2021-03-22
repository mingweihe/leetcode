#include <vector>

using namespace std;

class Solution {
public:
    vector<int> lexicalOrder(int n) {
        // Approach 2, iteration
        vector<int> ans(n);
        int cur = 1;
        for(int i = 0; i < n; ++i){
            ans[i] = cur;
            if(cur * 10 <= n){
                cur *= 10;
            }else{
                if(cur >= n) cur /= 10;
                cur += 1;
                while(cur % 10 == 0){
                    cur /= 10;
                }
            }
        }
        return ans;
        // // Approach 1, recursion
        // vector<int> ans;
        // for(int i = 1; i <= 9; ++i)
        //     dfs(i, n, ans);
        // return ans;
    }
    
    void dfs(int cur, int n, vector<int>& ans){
        if(cur > n) return;
        ans.push_back(cur);
        for(int i = 0; i <= 9; ++i)
            dfs(cur*10+i, n, ans);
    }
};
