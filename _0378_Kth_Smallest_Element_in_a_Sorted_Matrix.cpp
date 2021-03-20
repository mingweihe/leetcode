#include <vector>
#include <queue>

using namespace std;


class Solution {
public:
    int kthSmallest(vector<vector<int>>& matrix, int k) {
        // Approach 3, binary search, O(nlog(max-min))
        int n = matrix.size();
        int lo = matrix[0][0], hi = matrix[n-1][n-1];
        int mid;
        while(lo <= hi){
            mid = (lo+hi) / 2;
            int cnt = 0, j = n-1;
            for(int i = 0; i < n; ++i){
                while(j >= 0 && matrix[i][j] > mid)
                    j--;
                cnt += j + 1;
            }
            if(cnt >= k) hi = mid - 1;
            else lo = mid + 1;
        }
        return lo;
        
        // // Approach 2, priority_queue, O(klog(n))
        // priority_queue<pair<int, pair<int, int>>, vector<pair<int, pair<int, int>>>,
        //     greater<pair<int, pair<int, int>>>> pq;
        // int n = matrix.size();
        // for(int i = 0; i < n; ++i)
        //     pq.push(make_pair(matrix[i][0], make_pair(i, 0)));
        // int i, j;
        // while(k--){
        //     auto p = pq.top();
        //     pq.pop();
        //     i = p.second.first, j = p.second.second;
        //     if(j == n-1) continue;
        //     pq.push(make_pair(matrix[i][j+1], make_pair(i, j+1)));
        // }
        // return matrix[i][j];
        
        // // Approach 1, O(nk)
        // int n = matrix.size();
        // vector<int> indices(n);
        // for(int i = 0; i < n; ++i) indices[i] = 0;
        // int ans = 0;
        // for(int i = 0; i < k; ++i){
        //     int r = 0, mini = INT_MAX;
        //     for(int j = 0; j < n; j++){
        //         if(indices[j] == n) continue;
        //         if(matrix[j][indices[j]] < mini){
        //             r = j;
        //             mini = matrix[j][indices[j]];
        //         }
        //     }
        //     ans = matrix[r][indices[r]];
        //     indices[r] += 1;
        // }
        // return ans;
    }
};
