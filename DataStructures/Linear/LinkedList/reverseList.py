from model.model_numbers   import *

def reverseList(head):
    prev = None
    current = head
    
    while current is not None:
        next = current.next
        current.next = prev
        prev = current
        current = next
    return prev.next.val


print(reverseList(a))