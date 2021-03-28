#include <set>

using namespace std;

class Solution {
public:
    int lastRemaining(int n) {
        // Approach 2, O(log(N))
        int head = 1, rem = n, left = 1, step = 1;
        while(rem > 1){
            if(left || rem % 2 == 1)
                head += step;
            rem >>= 1;
            left ^= 1;
            step <<= 1;
        }
        return head;
        
        // // Approach 1, set, O(nlog^2(n)), TLE but well implemented brute force solution
        // set<int> st;
        // for(int i = 1; i <= n; ++i) st.insert(i);
        // set<int>::iterator it, tmp;
        // set<int>::reverse_iterator rit, rtmp;
        // while(st.size() > 1){
        //     it = st.begin();
        //     while(st.size() > 1 && it != st.end()){
        //         tmp = it;
        //         if(next(it) != st.end()) it = next(next(it));
        //         else it = next(it);
        //         st.erase(tmp);
        //     }
        //     rit = st.rbegin();
        //     while(st.size() > 1 && rit != st.rend()){
        //         rtmp = rit;
        //         if(next(rit) != st.rend()){
        //             rit = next(next(rit));
        //             st.erase(--rtmp.base());
        //         }else{
        //             st.erase(--rtmp.base());
        //             rit = st.rend();
        //         }
        //     }
        // }
        // return *st.begin();
    }
};
