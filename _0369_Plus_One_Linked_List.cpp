//Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* plusOne(ListNode* head) {
        if(head->next != nullptr){
            ListNode* nx = plusOne(head->next);
            if(head->next == nx) return head;
        }
        // adding 1 to the last digit is same with carrying 1 to the other digits
        int carry = (head->val + 1) / 10;
        head->val = (head->val + 1) % 10;
        if(carry == 0) return head;
        ListNode *node = new ListNode(carry, head);
        return node;
    }
};
