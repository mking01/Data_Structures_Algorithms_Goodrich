# Ch. 05 - Array-Based Sequences
# p. 224


# 1. Execute the experiment from Code Fragment 5.1.  Compare results to Code Fragment 5.2.
# 5.1
# import sys
# data = []
# for k in range(26):
#     data.append(k)
#     a = len(data)
#     b = sys.getsizeof(data)
#     print('Length: {0:3d}; Size in bytes: {1:4d}'.format(a, b))

# Their max at 26 items was 352 bytes, mine was 344 bytes.
# Theirs was 72, 104, 136, 200, 272, 352
# Mine was 96, 128, 192, 264, 344

# 2. In fragment 5.1, we compare list length to underlying memory usage.  Redesign the output so you only print
# values where k is completely exhausted.
# import sys
# data = []
# byte_size = []
# for k in range(26):
#     data.append(k)
#     a = len(data)
#     b = sys.getsizeof(data)
#     byte_size.append(b)
#     if byte_size[k] != byte_size[k - 1]:
#         print('Length: {0:3d}; Size in bytes: {1:4d}'.format(a, b))

# 3. Modify the experiment from fragment 5.1 to demonstrate python's list class occasionally shrinks the size of its
# underlying array when elements are popped from a list.
# import sys
# data = []
# for k in range(26):
#     data.append(k)
#     a = len(data)
#     b = sys.getsizeof(data)
#
#     if k % 2 == 0:
#         data.pop()
#         a = len(data)
#         c = sys.getsizeof(data)
#         print('Length: {0:3d}; Size in bytes: {1:4d}, Size after pop: {1:4d}'.format(a, b, c))


# 7. Let A be an array of size n >= 2 containing integers from 1 to n - 1 inclusive, with exactly one repeated.
# Describe a fast algorithm for finding the integer in A that is repeated.

# sort the list
# then compare item to item + 1 via index positions until you find the one that has two duplicates in a row
# this avoids a for loop situation so it's a faster run time to find the repeat
# alternately use set() ;) but that defeats the point of this exercise


# 11. Use standard control structures to compute the sum of all numbers in an n x n data set represented as a list of
# lists.

# create list of lists
# cols = 5
# rows = 5
# l_of_ls = [[1] * cols for j in range(rows)]
#
# total = 0
# for i in l_of_ls:
#     total += sum(i)
#
# print(total)


# 12. Describe how the built-in sum function can be combined with Python's comprehension syntax to compute the sum of
# all numbers in an n x n dataset, represented as a list of lists.


# create list of lists
# cols = 5
# rows = 5
# l_of_ls = [[1] * cols for j in range(rows)]
#
# total = sum([sum(i) for i in l_of_ls])
# print(total)