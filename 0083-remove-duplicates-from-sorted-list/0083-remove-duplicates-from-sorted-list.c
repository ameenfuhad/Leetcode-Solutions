/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* deleteDuplicates(struct ListNode* head) {
    if(head==NULL)
    {
        return head;
    }
    struct ListNode *temp=head;
    while(temp->next!=NULL)
    {
        struct ListNode *h=temp->next;
        if(h->val==temp->val) 
        {
            temp->next=h->next;
        }
        else
        {
            temp=temp->next;
        }   
        
    }
    return head;

}