#include <vector>
using namespace std;

class Solution {
public:
    vector<int> getModifiedArray(int length, vector<vector<int>>& updates) {
        vector<int> ans(length+1);
        for(vector<int> x: updates){
            ans[x[0]] += x[2];
            ans[x[1]+1] -= x[2];
        }
        for(int i = 1; i < length; ++i)
            ans[i] += ans[i-1];
        ans.pop_back();
        return ans;
    }
};
