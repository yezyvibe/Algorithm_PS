class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node()
        self.size = 0

    def append(self, data):
        new_node = Node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node
        self.size += 1

    def display(self):
        elems = []
        cur = self.head
        while cur.next != None:
            cur = cur.next
            elems.append(cur.data)
        return elems

    def add(self, index):
        cur_idx = 0
        cur_node = self.head
        first_node = cur_node.next

        while True:
            last_node = cur_node
            cur_node = cur_node.next

            if cur_idx == index:
                if index != self.size:
                    new_node = Node(last_node.data + cur_node.data)
                    last_node.next = new_node
                    new_node.next = cur_node
                    self.size += 1
                    return

                else:
                    new_node = Node(last_node.data + first_node.data)
                    last_node.next = new_node
                    self.size += 1
                    return
            cur_idx += 1

for tc in range(1, int(input())+1):
    my_list = LinkedList()
    n, m, k = map(int, input().split())
    numbers = list(map(int, input().split()))
    for number in numbers:
        my_list.append(number)

    index = 0
    for i in range(k):
        index += m
        if index > my_list.size:
            index = index % my_list.size
        my_list.add(index)
    result = my_list.display()
    result.reverse()
    if len(result) > 10:
        result = result[:10]
    print('#{} {}'.format(tc, ' '.join(list(map(str, result)))))
