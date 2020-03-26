# Ch. 3 - Algorithm Optimization
import matplotlib.pyplot as plt
import numpy as np
import math

# Reinforcement
# 1. Done on paper


# 2. The number of operations executed by algorithms A and B is 8n log n and 2n**2.  Determine n0 so that A is better
# than B for n >= n0.

# A = 8nlogn
# B = 2n**2
# A > B
# Simplified, A becomes 4nlogn and B becomes n

# both equations have the same X but different Ys

# x = [x / 100 for x in range(1, 1000)]
# y_a = list(map(lambda x: 4 * math.log(x), x))
# y_b = x
#
# algo_a = plt.plot(x, y_a, label="A")
# algo_b = plt.plot(x, y_b, label="B")
# plt.legend(["A", "B"])
# plt.show()

# Answer:  ~ 1.5 is where A becomes better than B

# 3. The number of operations executed by algorithms A and B is 40n**2 and 2n**3.  Determine n0 so that A is better
# than B for n>= n0.

# x = [x for x in range(1, 100)] # not starting at zero to avoid a /0 error
# y_a = list(map(lambda x: 40 * x ** 2, x))
# y_b = list(map(lambda x: 2 * x ** 3, x))
#
# algo_a = plt.plot(x, y_a, label="A")
# algo_b = plt.plot(x, y_b, label="B")
# plt.legend(["A", "B"])
# plt.show()

# Answer:  ~ 25 is where A becomes better than B.

# 4. Give an example of a function that is plotted the same on a log-log scale as it is on a standard scale.

# A constant function

# 5. Explain why the plot of the function n**c is a straight line with slope c on a log-log scale.

# if on a log-log scale, y = n**c becomes log(y) = log n ** c.
# this lets you pull out the constant, transforming into y = c * n
# y = c * n is simply a form of y = mx + b, minus the b intercept term and using c instead of m for the slope.

# # Proof on a normal scale its not a linear slope
# x = [x for x in range(1, 15)]
# y = list(map(lambda x: x ** 2, x))
#
# plt.plot(x, y)
# plt.show()

# 6. What is the sum of all the even numbers from 0 to n for any positive integer n?

# n = 100
# for i in range(0, n):
#     if i % 2 == 0:
#         total = total + i
# print(total)

# quadratic because is a nested loop
# the equation then always becomes (n(n + 1)) / 2 --> p. 115, Carl Gauss example


# 7. Show the following two statements are equivalent:
# a. The running time of algorithm A is always O(f(n)).
# b. In the worst case, the running time of algorithm A is O(f(n)).

# A = O(f(n))
# worst case = O(f(n))

# if a = b and b = c, then

# 8. Order functions by asymptotic growth rate (fastest to slowest below):

# constant term - 2 ** 10
# 3n + 100 log n
# 4n
# n log n
# 4 n log n + 2n
# n ** 2 + 10n
# n ** 3
# 2 ** log n assuming 3 < n < 10
# 2 ** n assuming 3 < n < 10


# 9. Show that if d(n) is O(f(n)) then ad(n) is O(f(n)) for any constant a > 0.

# d(n) * a = ad(n)
# old constant * new constant(n), which will maintain the original condition


# 14. Show that if O(max{f(n), g(n)}) = O(f(n) + g(n)).

# if f(n) gives us the y value and g(n) gives us a y value, then 2y must = f(n) + g(n)]