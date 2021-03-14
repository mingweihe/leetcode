using namespace std;

class Solution {
public:
    // Approach 2, gcd, O(log(n))
    bool canMeasureWater(int x, int y, int z) {
        if(x + y < z) return false;
        if(x == z || y == z || x+y == z) return true;
        return z % gcd(x, y) == 0;
    }
    // Approach 1, O(n)
    // unordered_set<int> ss;
    // int x, y;
    // bool canMeasureWater(int x, int y, int z) {
    //     if(x+y < z) return false;
    //     this->x = x;
    //     this->y = y;
    //     dfs(0);
    //     for(auto it = ss.begin(); it != ss.end(); it++)
    //         if(*it == z || (*it + x) == z || (*it + y) == z) return true;
    //     return false;
    // }
    
    // void dfs(int info){
    //     if(ss.find(info) != ss.end()) return;
    //     ss.insert(info);
    //     int new_info;
    //     if(info < x) dfs(x-info);
    //     else dfs(info - x);
    //     if(info < y) dfs(y-info);
    //     else dfs(info-y);
    // }
};
