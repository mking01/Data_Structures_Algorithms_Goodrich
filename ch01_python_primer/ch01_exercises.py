# Reinforcement
# 1. Write a short python function, is_multiple(n, m) that takes two integer
# values and returns True if n is a multiple of m, that is n = mi for some integer, i
# and false if otherwise.

# def is_multiple(n, m):
#     all_totals = []
#     for i in range(0, 10):
#         int_total = i * m
#         all_totals.append(int_total)
#     if n in all_totals:
#         return True
#     else:
#         return False
#
# n = 15
# m = 5
#
# print(is_multiple(n,m))

# 3. Write a short function, minmax(data), that takes a sequence of one or more numbers and returns the smallest and
# largest numbers in the form of a tuple of length two.  Do not use the built-in min max functions when implementing
# your solution.

# def minmax(data):
#     # sort list values
#     data.sort()
#
#     #grab the first value as the min
#     min = data[0]
#
#     # grab the last value as the max
#     max = data[-1]
#
#     return (min, max)
#
# data = [8, 7, 4]
#
# print(minmax(data))


# 4. Write a short function that takes a positive integer n and returns the sum of squares of all positive integers
# smaller than n.

# def sum_squares(n):
#     total = []
#     for i in range(0, n):
#         int_squared = i ** 2
#         total.append(int_squared)
#
#     sum_squares = sum(total)
#     return sum_squares
#
# n = 3
# print(sum_squares(n))


# 9. step = 10
# 10. step = -2
# 11. Use Python's list comprehension syntax to produce the list [1, 2, 4, 8, 16, 32, 64, 128, 256].
# requested_list = [2 ** x for x in range(9)]
# print(requested_list)

# 14. Write a short Python function that takes a sequence of integer values and determines if there is a distinct
# pair of numbers in the sequence whose product is odd.

# seq = [1, 2, 3]
#
#
# def odd_product(seq):
#     # ensure each sequence value is distinct
#     seq = list(set(seq))
#
#     product_dict = {}
#     for i in range(len(seq) + 1):
#         try:
#             prod = seq[i] * seq[i + 1]
#             product_dict[prod] = seq[i], seq[i + 1]
#         # ignores error for last index value saying list out of range
#         except:
#             pass
#
#     total_odds = 0
#     for key in product_dict.keys():
#         if key % 2 != 0:
#             total_odds += 1
#         else:
#             total_odds += 0
#
#
#     if total_odds == 0:
#         return print("No odd products")
#     else:
#         return print(total_odds, "odd products")
#
# print(odd_product(seq))


# 15. could just use set()


# 17.  Had we implemented the scale function as is below, does it work properly?
# Explain why or why not.

# def scale(data, factor):
#     for val in data:
#         val *= factor
#
# data = [1,2,3,4,5]
# factor = 2
#
# scaled = scale(data, factor)
# print(scaled)

# Answer: No, current function returns "None."  The function does not return anything back.  Further, the list is not
# updated in place after the multiplication occurs.  Finally, this should be done through looping through index
# values, then accessing the value through data[index] and multiplying it by the factor, set equal to an updated
# list.  Then return the list.

# 19. Demonstrate how to produce a list of all individual alphabet characters without having to type all 26
# characters literally.

#print([chr(97 + x) for x in range(26)])

# 29. Write a Python program outputting all possible strings formed by using the characters of catdog exactly once.

# A lot of repeats!  Not sure of a better way to build that would be less lines of code.
# would be a great recursion problem
string_list = ['c','a','t','d','o','g']

def get_combos(string_list):
    all_words = []

    #doubles
    for i in string_list:
        for j in string_list:
            combo = i + j
            all_words.append(combo)

    #triples
    for i in string_list:
        for j in string_list:
            for k in string_list:
                combo = i + j + k
                all_words.append(combo)


    #fours
    for i in string_list:
        for j in string_list:
            for k in string_list:
                for m in string_list:
                    combo = i + j + k + m
                    all_words.append(combo)


    #fives
    for i in string_list:
        for j in string_list:
            for k in string_list:
                for m in string_list:
                    for n in string_list:
                        combo = i + j + k + m + n
                        all_words.append(combo)
    return all_words

print(get_combos(string_list))
#
#
# # 34. Common punishment is write out a sentence multiple times. Write a python standalone program that will write out
# # the following sentence 100x: "I will never spam my friends again." Your program should number each of the sentences
# # and make eight different random-looking typos.
#
# sentence = "I will never spam my friends again."
# n_times = 100
#
# def automate_my_punishment(sentence, n_times):
#     punishment_dict = {}
#     for i in range(n_times):
#         if i <= 99:
#             punishment_dict[i] = sentence
#         # for time's sake I'm just doing 1 error, omit last 2 words
#         elif i == 100:
#             punishment_dict[i] = "I will never spam"
#     return punishment_dict
#
#
# print(automate_my_punishment(sentence, n_times))