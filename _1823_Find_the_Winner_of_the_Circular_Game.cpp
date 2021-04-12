#include <set>

using namespace std;

class Solution {
public:
    int findTheWinner(int n, int k) {
        set<int> st;
        for(int i = 1; i <= n; ++i)
            st.insert(i);
        int idx = 0;
        set<int>::iterator it;
        while(st.size() > 1){
            int remove_idx = (idx + k - 1) % st.size();
            it = next(st.begin(),  remove_idx);
            st.erase(it);
            idx = remove_idx;
        }
        return *st.begin();
    }
};
