def RemoveDuplicates(head):
    if head is None:
        return head
    node = head
    while node.next:
        if node.data == node.next.data:
            node.next = node.next.next
        else:
            node = node.next
    return head
