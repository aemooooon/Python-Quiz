class Node(object):
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class LinkedList(object):
    dict = {}

    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def append(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def __iter__(self):
        if not self.head:
            return
        current = self.head
        yield current.data
        while current.next:
            current = current.next
            yield current.data

    def peek(self):
        return self.head.data

    def pop(self):
        if self.head is None:
            return
        temp = self.head.data
        self.head = self.head.next
        return temp

    def __len__(self):
        current = self.head
        count = 0
        if current is None:
            raise Exception("The LinkedList is empty")
        while current is not None:
            count += 1
            current = current.next
        return count
    
    def _getdata(self, index):
        current =self.head
        target = None
        for _ in range(index):
            current = current.next
        target = current
        return target

    def __getitem__(self, index):
        if isinstance(index, int):
            if index >= 0 and index < self.__len__():
                node = self._getdata(index)
                self.dict[index] = node.data
                return self.dict[index]
            else:
                raise IndexError
        else:
            raise('Index must an integer')


if __name__ == "__main__":

    link_list = LinkedList()

    

    # append function
    for i in range(37, 40):
        link_list.append(i)

    print("The length of linked_list is: ", len(link_list))

    # Iterator function
    for node in link_list:
        print(f"iterator value by for loop: {node}")

    print("pop value is:", link_list.pop())

    print('after by pop')
    for node in link_list:
        print(f"node: {node}")

    print('accessed by [index]')
    print("link_list[0]: ", link_list[0])
    print("link_list[1]: ", link_list[1])
