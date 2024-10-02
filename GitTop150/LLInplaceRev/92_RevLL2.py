# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        #create dummy node
        dummy = ListNode(0,head)

        prev, cur = dummy, dummy.next

        #get the prev and cur nodes from left
        for _ in range(left-1):
            prev = prev.next
            cur = cur.next


        #Reverse nodes
        prevRev = None
        # print(prev.val, cur.val)
        for _ in range(right - left + 1):
            nexts = cur.next
            cur.next = prevRev
            prevRev = cur
            cur = nexts

        #point nodes correctly - node 1 should point to 4 and node 2 to 5
        # print(prevRev)
        prev.next.next = cur
        prev.next = prevRev

        return dummy.next

        #[1,3,2,4,5]
        
