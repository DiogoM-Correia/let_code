class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    # Initialization
    dummy_head = ListNode(0)  # Dummy node to act as the head of the result list
    current = dummy_head
    carry = 0
    
    # Iterate through lists l1 and l2
    while l1 or l2 or carry:
        # Get the values from the current nodes, if present
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        
        # Calculate the sum and determine the new carry
        total = val1 + val2 + carry
        carry = total // 10  # new carry
        digit = total % 10   # current digit to store in the node
        
        # Create a new node with the digit and move to the next position
        current.next = ListNode(digit)
        current = current.next
        
        # Move to the next nodes in l1 and l2, if present
        if l1: l1 = l1.next
        if l2: l2 = l2.next
    
    # Return the next of dummy node, i.e., the start of the result list
    return dummy_head.next

# Example usage
# Helper function to create a linked list from a list
def create_linked_list(nums):
    dummy = ListNode()
    current = dummy
    for num in nums:
        current.next = ListNode(num)
        current = current.next
    return dummy.next
   
# Helper function to convert a linked list to a list
def linked_list_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

# Test cases
l1 = create_linked_list([2, 4, 3])
l2 = create_linked_list([5, 6, 4])
result = addTwoNumbers(l1, l2)
print(linked_list_to_list(result))  # Output: [7, 0, 8]
l1 = create_linked_list([0])
l2 = create_linked_list([0])
result = addTwoNumbers(l1, l2)
print(linked_list_to_list(result))  # Output: [0]
l1 = create_linked_list([9, 9, 9, 9, 9, 9, 9])
l2 = create_linked_list([9, 9, 9, 9])
result = addTwoNumbers(l1, l2)
print(linked_list_to_list(result))  # Output: [8, 9, 9, 9, 0, 0, 0, 1]