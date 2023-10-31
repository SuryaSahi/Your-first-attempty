curr = llist
    count = 1
    while count != position:
        curr = curr.next
        count+=1
    node = SinglyLinkedListNode(data)
    node.next = curr.next
    curr.next = node
    
    return llist
