def reverse(llist): 
    prev = None
    curr = llist
    next = None
    while curr != None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev    
