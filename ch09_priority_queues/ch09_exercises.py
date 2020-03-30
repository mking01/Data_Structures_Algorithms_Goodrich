# Ch. 09 - Priority Lists
# p. 395


# Reinforcement
# 1.  How long would it take to remove the [log n] smallest elements from a heap that contains n
# entries, using the remove_min operation?

# removing -> O(1)
# rearranging -> O(log n)
# combined -> O(1) + O(log n) = O(log n)

# 2. Suppose you label each position p of a binary tree T with a key equal to its preorder rank.  Under what
# circumstances is T a heap?

# Always because the parent node will always be smaller than the child node.

# 3. What does each remove_min call return within the following sequence of priority queue ADT methods?

# add(5,A)        #(5,A)
# add(4,B)        #(5,A), (4,B)
# add(7,F)        #(5,A), (4,B), (7,F)
# add(1,D)        #(5,A), (4,B), (7,F), (1,D)
# remove_min()    #(5,A), (4,B), (7,F)
# add(3,J)        #(5,A), (4,B), (7,F), (3,J)
# add(6,L)        #(5,A), (4,B), (7,F), (3,J), (6,L)
# remove_min()    #(5,A), (4,B), (7,F), (6,L)
# remove_min()    #(5,A), (7,F), (6,L)
# add(8,G)        #(5,A), (7,F), (6,L), (8,G)
# remove_min()    #(7,F), (6,L), (8,G)
# add(2,H)        #(7,F), (6,L), (8,G), (2,H)
# remove_min()    #(7,F), (6,L), (8,G)
# remove_min()    #(7,F), (8,G)


# 7. Illustrate the execution of the selection-sort algorithm on the following input sequence:
# (22,15,36,44,10,3,9, 13,29,25)

# Phase 1:
# Input / C: (22,15,36,44,10,3,9, 13,29,25)
# Priority Queue P: ()
# Incrementally moved over

# (22,15,36,44,10,3,9,13,29,25)  | ()
# (15,36,44,10,3,9,13,29,25)     | (22,)
# (36,44,10,3,9,13,29,25)        | (22,15,)
# (44,10,3,9,13,29,25)           | (22,15,36,)
# (10,3,9,13,29,25)              | (22,15,36,44,)
# (3,9,13,29,25)                 | (22,15,36,44,10,)
# (9,13,29,25)                   | (22,15,36,44,10,3,)
# (13,29,25)                     | (22,15,36,44,10,3,9,)
# (29,25)                        | (22,15,36,44,10,3,9,13,)
# (25)                           | (22,15,36,44,10,3,9,13,29,)
# ()                             | (22,15,36,44,10,3,9,13,29,25)


# Phase 2:
# Input / C: ()
# Priority Queue P: (22,15,36,44,10,3,9,13,29,25)
# Removed in sort order

# ()                            | (22,15,36,44,10,3,9,13,29,25)
# (3)                           | (22,15,36,44,10,9,13,29,25)
# (3,9)                         | (22,15,36,44,10,13,29,25)
# (3,9,10)                      | (22,15,36,44,13,29,25)
# (3,9,10,13)                   | (22,36,44,15,29,25)
# (3,9,10,13,15)                | (22,36,44,29,25)
# (3,9,10,13,15,22)             | (36,44,29,25)
# (3,9,10,13,15,22,25)          | (36,44,29)
# (3,9,10,13,15,22,25,29)       | (36,44)
# (3,9,10,13,15,22,25,29,36)    | (44)
# (3,9,10,13,15,22,25,29,36,44) | ()

# 10 - smallest keys at top / towards beginning
# 11 - largest keys towards the end










