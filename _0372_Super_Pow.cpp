#include <vector>
using namespace std;

class Solution {
public:
    // a * b % k = (a % k) * (b % k) % k
    const int base = 1337;
    int superPow(int a, vector<int>& b) {
        if(b.empty()) return 1;
        int last_d = b.back();
        b.pop_back();
        return power_mod(superPow(a, b), 10) * power_mod(a, last_d) % base; 
    }
    
    int power_mod(int a, int k){
        int result = 1;
        a %= base;
        for(int i = 0; i < k; ++i){
            result = result * a % base;
        }
        return result;
    }
};
