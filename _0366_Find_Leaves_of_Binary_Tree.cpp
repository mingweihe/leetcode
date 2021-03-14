#include <vector>

using namespace std;


 // Definition for a binary tree node.
 struct TreeNode {
     int val;
     TreeNode *left;
     TreeNode *right;
     TreeNode() : val(0), left(nullptr), right(nullptr) {}
     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 };
 
class Solution {
public:
    // return distance to the longest leaf
    int dfs(TreeNode* node, vector<vector<int>>& ans){
        if(node == NULL) return 0;
        int l = dfs(node->left, ans);
        int r = dfs(node->right, ans);
        int dis = max(l, r);
        if(ans.size() == dis) ans.push_back({});
        ans[dis].push_back(node->val);
        return dis + 1;
    }
    
    vector<vector<int>> findLeaves(TreeNode* root) {
        vector<vector<int>> ans;
        dfs(root, ans);
        return ans;
    }
};
