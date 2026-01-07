"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        if not head:
            return head

        # STEP 1: Create new nodes interleaved with original nodes
        curr=head
        while curr:
            new_node=Node(curr.val)
            new_node.next=curr.next
            curr.next=new_node
            curr=curr.next.next

        # STEP 2: Assign random pointers to copied nodes
        curr=head
        while curr:
            if curr.random:
                curr.next.random=curr.random.next
            curr=curr.next.next

        # STEP 3: Separate original and copied lists
        curr=head
        copy_head=head.next
        copy_curr=copy_head
        while curr:
            curr.next=curr.next.next
            
            if copy_curr.next:
                copy_curr.next=copy_curr.next.next
            curr=curr.next
            copy_curr=copy_curr.next
        
        return copy_head
        
            
        