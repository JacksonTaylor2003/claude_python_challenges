class Node:
    def __init__(self, value, next=None):
      self.value = value
      self.next = next

third = Node(3)
second = Node(2, third)
first = Node(1, second)

def list_sum(head):
    if not head:
      return 0

    sum_of_values = list_sum(head.next)

    return sum_of_values + head.value

print(list_sum(first))
print(list_sum(None))