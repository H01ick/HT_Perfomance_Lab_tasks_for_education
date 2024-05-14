class Node:
    def __init__(self, value = None, next = None) -> None:
        self.value = value
        self.next = next
    def __str__(self) -> str:
        return str(self.value)

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.length = 0

    def append(self, value) -> None:
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.length += 1
            return
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node
        self.length += 1

    def get(self, node_index) -> int:
        current_node = self.head
        list_index = 0
        while list_index <= node_index:
            if list_index == node_index:
                return current_node.value
            list_index += 1
            current_node = current_node.next

    # def printList(self):
    #     current_node = self.head
    #     while current_node:
    #         print(current_node.value)
    #         current_node = current_node.next

def main():
    n, m = [int(x) for x in input().split()]
    result: int
    new_list = LinkedList()
    for i in range(1, n + 1):
        new_list.append(i)
    value = new_list.head.value
    result = str(value)
    if m > n:
        m %= n
    while True:
        if value + m - 2 < new_list.length:
            value = new_list.get(value + m - 2)
        else:
            value = new_list.get(value + m - 2 - new_list.length)
        if value == 1:
            break
        result += str(value)
    print(result)

if __name__ == "__main__":
    main()