#include <string>
#include <unordered_map>

using namespace std;


class AuthenticationManager {
public:
    unordered_map<string, int> mp;
    int ttl;
    // more efficient solution: set<pair<int, string>> time_map
    AuthenticationManager(int timeToLive) {
        ttl = timeToLive;
    }
    
    void generate(string tokenId, int currentTime) {
        mp[tokenId] = currentTime + ttl;
    }
    
    void renew(string tokenId, int currentTime) {
        if(mp.find(tokenId) == mp.end() || mp[tokenId] <= currentTime)
            return;
        mp[tokenId] = currentTime + ttl;
    }
    
    int countUnexpiredTokens(int currentTime) {
        int ans = 0;
        for(auto it = mp.begin(); it != mp.end(); ++it){
            if(it->second > currentTime) ans += 1;
        }
        return ans;
    }
};

/**
 * Your AuthenticationManager object will be instantiated and called as such:
 * AuthenticationManager* obj = new AuthenticationManager(timeToLive);
 * obj->generate(tokenId,currentTime);
 * obj->renew(tokenId,currentTime);
 * int param_3 = obj->countUnexpiredTokens(currentTime);
 */
