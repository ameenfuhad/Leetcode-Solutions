/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* reverseList(struct ListNode* head) {
    struct ListNode *start = NULL;
    struct ListNode *temp = head;
    struct ListNode *just = NULL;
    while(temp!=NULL)
    {
        just=temp;
        temp=temp->next;
        just->next=start;
        start=just;
    }
    return start;
}