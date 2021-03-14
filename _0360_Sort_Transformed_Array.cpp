#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<int> sortTransformedArray(vector<int>& nums, int a, int b, int c) {
        vector<int> ans;
        int n = nums.size();
        if(a == 0){
            for(int i = 0; i < n; ++i)
                ans.push_back(f(nums[i], a, b, c));
            if(b < 0)
                reverse(ans.begin(), ans.end());
        }else{
            int l = 0;
            int r = n-1;
            int left, right;
            if(a < 0){
                while(l <= r){
                    left = f(nums[l], a, b, c);
                    right = f(nums[r], a, b, c);
                    if(left <= right){
                        ans.push_back(left);
                        l++;
                    }else{
                        ans.push_back(right);
                        r--;
                    }
                }
            }else{
                while(l <= r){
                    left = f(nums[l], a, b, c);
                    right = f(nums[r], a, b, c);
                    if(left >= right){
                        ans.push_back(left);
                        l++;
                    }else{
                        ans.push_back(right);
                        r--;
                    }
                }
                reverse(ans.begin(), ans.end());
            }
        }
        return ans;
    }
    
    int f(int x, int a, int b, int c){
        return a * x * x + b * x + c;
    }
};
