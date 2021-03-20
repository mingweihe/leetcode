#include <vector>
#include <queue>

using namespace std;


class Solution {
public:
    vector<vector<int>> kSmallestPairs(vector<int>& nums1, vector<int>& nums2, int k) {
        // Appraoch 2, priority queue O(k*log(k))
        vector<vector<int>> ans;
        int m = nums1.size(), n = nums2.size();
        if(m == 0 || n == 0) return ans;
        priority_queue<pair<int, pair<int, int>>, vector<pair<int, pair<int, int>>>,
            greater<pair<int, pair<int, int>>>> pq;
        for(int i = 0; i < min(m, k); ++i)
            pq.push(make_pair(nums1[i]+nums2[0], make_pair(i, 0)));
        int i, j;
        while(!pq.empty() && ans.size() < k){
            pair<int, int> pr = pq.top().second;
            pq.pop();
            i = pr.first;
            j = pr.second;
            ans.push_back({nums1[i], nums2[j]});
            if(j == n-1) continue;
            pq.push(make_pair(nums1[i]+nums2[j+1], make_pair(i, j+1)));
        }
        return ans;
        
        // // Approach 1, O(m*n*log(m*n))
        // vector<vector<int>> t;
        // for(int i = 0; i < nums1.size(); ++i){
        //     for(int j = 0; j < nums2.size(); ++j){
        //         t.push_back({nums1[i], nums2[j]});
        //     }
        // }
        // sort(t.begin(), t.end(), [](vector<int>& a, vector<int>& b){
        //     return a[0] + a[1] < b[0] + b[1];
        // });
        // if(t.size() <= k) return t;
        // vector<vector<int>> ans;
        // for(int i = 0; i < k; ++i) ans.push_back(t[i]);
        // return ans;
    }
};
