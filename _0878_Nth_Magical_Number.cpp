#include <bits/stdc++.h>

using namespace std;
#define ll long long


class Solution {
public:
    int mod = 1e9+7;
    int nthMagicalNumber(int n, int a, int b) {
        ll mid, l = 2, r = (ll) min(a, b) * n;
        while(l <= r){
            mid = l + (r-l) / 2;
            if(valid(mid, a, b, n)) r = mid - 1;
            else l = mid + 1;
        }
        return l % mod;
    }
    
    bool valid(ll& x, int& a, int& b, int& n){
        return x / a + x / b - x / lcm(a, b) >= n;
    }
};
