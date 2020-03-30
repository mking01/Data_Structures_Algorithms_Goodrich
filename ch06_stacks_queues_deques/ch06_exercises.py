# Ch. 06 - Stacks, Queues, and Deques

# Reinforcement, p. 250

# 1. What values are returned during the following series of operations if executed upon an initially empty stack?
class ArrayStack:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, e):
        self._data.append(e)

    def top(self):
        if self.is_empty():
            raise ValueError('Stack is empty')
        return self._data[-1]

    def pop(self):
        if self.is_empty():
            raise ValueError('Stack is empty')
#         return self._data.pop()
#
# S = ArrayStack()
# S.push(5)
# S.push(3)
# S.pop()  # remove 3, 5 next
# S.push(2)
# S.push(8)
# S.pop()  # remove 8, 2 next
# S.pop()  # remove 2, 5 left
# S.push(9)
# S.push(1)
# S.pop()  # remove 1, 9 next
# S.push(7)
# S.push(6)
# S.pop()  # remove 6,  7 left
# S.pop()  # remove 7, 9 left
# S.push(4)
# S.pop()  # remove 4, 9 left
# print(S.pop()) # remove 9, 5 left

# 2. Initially empty stack, 25 push operations, 12 top operations, 10 pop operations, 3 of which raised errors.  What
# is the current size of S?

# start at 0
# + 25 push()
# - 7 pop() (10 - 3 with empty nothing to remove errors = 7)
# size = 18 elements

# 5. Implement a function that reverses a list of elements by pushing them onto a stack in one order and writes them
# back to the list in reversed order.

class ArrayStack:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, e):
        self._data.append(e)

    def top(self):
        if self.is_empty():
            raise ValueError('Stack is empty')
        return self._data[-1]

    def pop(self):
        if self.is_empty():
            raise ValueError('Stack is empty')
        return self._data.pop()


def reverse_stack(items_lst):
    '''
    Purpose: Reverses a list of elements by pushing them on to a stack in order then returning them in reverse order
    '''
    #initialize empty stack object
    S = ArrayStack()

   #push list items to stack in order
    for item in items_lst:
        S.push(item)

    # initialize empty list for result set
    return_lst = []

    # remove items from stack so list returns them in reverse order
    for item in range(len(S)):
      return_lst.append(S.pop())

    return print(return_lst)

items_lst = [1,2,3]
reverse_stack(items_lst)  #[3, 2, 1]


# 7. What values are returned during the following sequence of queue operations?

# enqueue(5)
# enqueue(3)
# dequeue()   # removes 5, 3 first
# enqueue(2)  # 3, 2
# enqueue(8)  # 3, 2, 8
# dequeue()   # 2, 8
# dequeue()   # 8
# enqueue(9)  # 8, 9
# enqueue(1)  # 8, 9, 1
# dequeue()   # 9, 1
# enqueue(7)  # 9, 1, 7
# enqueue(6)  # 9, 1, 7, 6
# dequeue()   # 1, 7, 6
# dequeue()   # 7, 6
# enqueue(4)  # 7, 6, 4
# dequeque()  # 6, 4
# dequeue()   # 4

# 8. Empty queue then executes 32 enqueue operations, 10 first operations, and 15 dequeue operations, 5 of which
# raise empty errors  What is the size of Q?

# 0
# + 32 (enqueue)
# - 10 (dequeue 15 - 5 empty)
# Q = 22 total elements

# 12. WHat values are returned during the following seuqence of deque ADT operations?

# add_first(4)    # 4
# add_last(8)     # 4, 8
# add_last(9)     # 4, 8, 9
# add_first(5)    # 5, 4, 8, 9
# back()          # 9
# delete_first()  # 4, 8, 9
# delete_last()   # 4, 8
# add_last(7)     # 4, 8, 7
# first()         # 4
# last()          # 7
# add_last(6)     # 4, 8, 7, 6
# delete_first()  # 8, 7, 6
# delete_first()  # 7, 6