#include <cstdlib>
#include <ctime>

using namespace std;

// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* head;
    /** @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node. */
    Solution(ListNode* head) {
        this->head = head;
        srand(time(NULL));
    }
    
    /** Returns a random node's value. */
    int getRandom() {
        // revervoir samping algorithm, O(n)
        ListNode* node = head;
        int k = 1, i = 1; // randomly pick k numbers
        int ans = node->val;
        while(node){
            if(i <= k) ans = node->val;
            else{
                int d = rand() % i;
                if(d < k) ans = node->val;
            }
            node = node->next;
            i++;
        }
        return ans;
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(head);
 * int param_1 = obj->getRandom();
 */
