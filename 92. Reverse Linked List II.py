
from typing import Optional


class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

def reverseBetween(head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    if not head or left == right:
        return head
    
    # Create a dummy node to simplify edge cases where left == 1
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy
    
    # Step 1: Move `prev` pointer to the node just before the starting node of the sublist
    for _ in range(left - 1):
        prev = prev.next
    
    right_node = prev.next
    for _ in range(right - left - 1):
        right_node = right_node.next

    dummy = prev
    dummy.next = prev.next
    prev = right_node
    prev.next = right_node.next
    right_node = dummy
    right_node.next = dummy.next
    
    return head

def create_linked_list(nums):
    dummy_head = ListNode()
    current = dummy_head
    for num in nums:
        current.next = ListNode(num)
        current = current.next
    return dummy_head.next

def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" ")
        current = current.next
    print()

nums = [1,2,3,4,5]
head = create_linked_list(nums)
result = reverseBetween(head, 2, 5)
print_linked_list(result)  # Output: 1 4 3 2 5