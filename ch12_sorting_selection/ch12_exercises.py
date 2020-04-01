# Ch. 12 - Sorting and Selection
# p. 574


# 1. Give a complete justification for proposition 12.1.

# Proposition: Why study sorting algorithms?

# Justification: Because sorting algorithms are used for a variety of problems that involve rearranging elements of a
# list or selecting an element from a list meeting a specific criteria. Understanding types of sorting and selecting
# needed and the various algorithm tradeoffs among solutions allows us to not just provide a solution, but select the
# optimal solution given the size of the collection and goals of the search.


# 2. In the merge-sort tree in Figures 12.2 - 12.4, edges are drawn as arrows.  What is the meaning of the downward
# arrow?  What is the meaning of the upward arrow?

# down arrows refer to the input sequences for sorting
# up arrows refer to the output sequences for sorting
# each shows half the process (the downs and then the ups)


# 4. Is the array based implementation of merge-sort given in Section 12.2.2 stable?  Why or why not?
# stable because elements are merged rather than shifted or rearranged and broken down, then recombined
# it operates on s1, then it operates on s2 in appending to S overall


# 12. If the outermost while loop of our implementation of inplace_quick_sort were changed to use condition left <
# right rather than left <= right, there would be a flaw.  Explain the flaw and give a specific input sequence on
# which such an implementation fails.

# if you just used "<" rather than "<=" right, your results end up not being inclusive of the last item in the sequence

# Ex. if left = 1 and right =5, for sequence [1,2,3,4,5,6,7,8,9,10]

# the code then becomes

#left = 1
#right = 5
#while left < right:
    #while left <= right and S[left] < pivot

# ....










