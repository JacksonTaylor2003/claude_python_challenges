class Node:
    def __init__(self, value, next=None):
      self.value = value
      self.next = next

third = Node(3)
second = Node(2, third)
first = Node(1, second)

def list_length(head):
    if not head:
        return 0

    next_node = list_length(head.next)

    return next_node + 1

print(list_length(first))
print(list_length(None))