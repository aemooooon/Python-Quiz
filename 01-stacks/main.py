# Linked list class
class Node:
    def __init__(self, item, next_item):
        self.item = item
        self.next = next_item
        
# Stack class
class LinkedListStack:
    def __init__(self):
        self._top = None
        self._size = 0

    def isEmpty(self):
        return self._top is None
    
    # The length of Stack
    def __len__(self):
        return self._size

    # Return the top item without remove it
    def peek(self):
        if self._top is None:
            return "Couldnot peek at an empty stack"
        else:
            return self._top.item

    # Return the top item and remove it
    def pop(self):
        if self._top is None:
            return "Couldnot pop at an empty stack"
        else:
            node = self._top
            self._top = self._top.next
            self._size -= 1
            return node.item

    #  push an item to the stack
    def push(self, item):
        self._top = Node(item, self._top)
        self._size += 1

if __name__ == "__main__":
    # define a instance of Stack
    car_stack = LinkedListStack()

    # Test isEmpty function 
    print(car_stack.peek())
    print(car_stack.pop())

    # Test push function
    car_stack.push('Audi')
    car_stack.push('Benz')
    car_stack.push('BMW')

    # Test peek function
    print(car_stack.peek())

    # Test pop function
    for i in range(0, len(car_stack)):
        print(car_stack.pop())

