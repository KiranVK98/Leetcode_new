# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #Floyds tortoise and heir algorithm

        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if(slow == fast):
                return True

        return False

        # hash_set = set()

        # cur = head

        # while(cur):
        #     if(cur in hash_set):
        #         return True

        #     hash_set.add(cur)
        #     cur = cur.next


        # return False