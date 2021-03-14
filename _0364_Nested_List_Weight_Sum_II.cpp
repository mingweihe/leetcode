#include <vector>

using namespace std;
/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * class NestedInteger {
 *   public:
 *     // Constructor initializes an empty nested list.
 *     NestedInteger();
 *
 *     // Constructor initializes a single integer.
 *     NestedInteger(int value);
 *
 *     // Return true if this NestedInteger holds a single integer, rather than a nested list.
 *     bool isInteger() const;
 *
 *     // Return the single integer that this NestedInteger holds, if it holds a single integer
 *     // The result is undefined if this NestedInteger holds a nested list
 *     int getInteger() const;
 *
 *     // Set this NestedInteger to hold a single integer.
 *     void setInteger(int value);
 *
 *     // Set this NestedInteger to hold a nested list and adds a nested integer to it.
 *     void add(const NestedInteger &ni);
 *
 *     // Return the nested list that this NestedInteger holds, if it holds a nested list
 *     // The result is undefined if this NestedInteger holds a single integer
 *     const vector<NestedInteger> &getList() const;
 * };
 */
class Solution {
public:
    // Approach 2: one pass with no multiplications
    int depthSumInverse(vector<NestedInteger>& nestedList) {
        int ans = 0;
        int accum = 0;
        while(!nestedList.empty()){
            vector<NestedInteger> next;
            for(NestedInteger& nes: nestedList){
                if(nes.isInteger()) accum += nes.getInteger();
                else{
                    vector<NestedInteger> vec = nes.getList();
                    next.insert(next.end(), vec.begin(), vec.end());
                }
            }
            nestedList = next;
            ans += accum;
        }
        return ans;
    }
    
    // Approach 1: two passes
//     int depthSumInverse(vector<NestedInteger>& nestedList) {
//         int ans = 0;
//         int depth = get_depth(nestedList);
//         dfs(nestedList, depth, ans);
//         return ans;
//     }
    
//     int get_depth(vector<NestedInteger>& nestedList){
//         int depth = 0;
//         for(NestedInteger& nes: nestedList){
//             if(nes.isInteger()) continue;
//             depth = max(depth, get_depth(nes.getList()));
//         }
//         return depth + 1;
//     }
    
//     void dfs(vector<NestedInteger>& nestedList, int depth, int& ans){
//         for(NestedInteger& nes: nestedList){
//             if(nes.isInteger()) ans += nes.getInteger() * depth;
//             else dfs(nes.getList(), depth-1, ans);
//         }
//     }
};
