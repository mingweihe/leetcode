#include <set>
#include <vector>

using namespace std;


class Solution {
public:
    const int mod = 1e9+7;
    int getNumberOfBacklogOrders(vector<vector<int>>& orders) {
        multiset<pair<int, int>> sell;
        multiset<pair<int, int>> buy;
        for(vector<int> order: orders){
            if(order[2] == 0) buy.insert(make_pair(order[0], order[1]));
            else sell.insert(make_pair(order[0], order[1]));
            while(!sell.empty() && !buy.empty() && (*sell.begin()).first <= (*buy.rbegin()).first){
                int match = min((*sell.begin()).second, (*buy.rbegin()).second);
                int a1 = (*sell.begin()).second - match;
                int p1 = (*sell.begin()).first;
                sell.erase(sell.begin());
                if(a1) sell.insert(make_pair(p1, a1));
                int a2 = (*buy.rbegin()).second - match;
                int p2 = (*buy.rbegin()).first;
                buy.erase(prev(buy.end()));
                if(a2) buy.insert(make_pair(p2, a2));
            }
        }
        int ans = 0;
        for(auto it = buy.begin(); it != buy.end(); ++it)
            ans = (ans + (*it).second) % mod;
        for(auto it = sell.begin(); it != sell.end(); ++it)
            ans = (ans + (*it).second) % mod;
        return ans;
    }
};
