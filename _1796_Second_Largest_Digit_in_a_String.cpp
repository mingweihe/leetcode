#include <set>
#include <string>

using namespace std;


class Solution {
public:
    int secondHighest(string s) {
        set<int> ans;
        for(char ch: s){
            if(isalpha(ch)) continue;
            ans.insert(ch-'0');
        }
        if(ans.size() <= 1) return -1;
        return *next(ans.rbegin());
    }
};

