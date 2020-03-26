# Ch. 02 - OOP, p.103

# Reinforcement
# 1. Give 3 examples of life-critical software applications.
# a. self-driving cars
# b. self-cleaning smart ovens ovens
# c. smart medical equipment

# 2. Give an example of a software application which adaptability means the difference between a prolonged sales
# lifetime and bankruptcy.
# Microsoft Office is a good example of this.  They have vastly expanded and updated their product over decades to
# maintain relevancy and competitiveness to all kinds of companies.

# 3. Describe a component from a text-editor GUI and the methods it encapsulates.
# Component: Background
# Methods: default_color: white
# change_color
# set_pattern
# set_picture
# set_picture/pattern_transparency

# 4. Write a Python class, Flower, that has 3 instance variables of type str, int, and float that represent the name,
# number of petals, and price.  You must include a constructor that initializes each to an appropriate value and your
# class should include methods for setting the value of each type and retrieving the value of each type.
# class Flower():
#     '''
#     Class to manage flower name (str), petal count (int), and price (float)
#     '''
#     def __init__(self, name=None, petals=None, price=None):
#         self._name = name
#         self._petals = petals
#         self._price = price
#
#     def set_name(self, name):
#         try:
#             self._name = str(name)
#         except:
#             print('Input must be a string.')
#
#     def set_petal_count(self, petals):
#         try:
#             self._petals = int(petals)
#         except:
#             print('Input must be int')
#
#     def set_price(self, price):
#         try:
#             self._price = float(price)
#         except:
#             print('Input must be decimal (no $ character).')
#
#     def get_name(self):
#         if self._name is None:
#             print('Attribute has not been set yet.')
#         else:
#             return self._name
#
#     def get_petal_count(self):
#         if self._petals is None:
#             print('Attribute has not been set yet.')
#         else:
#             return self._petals
#
#     def get_price(self):
#         if self._price is None:
#             return print('Attribute has not been set yet.')
#         else:
#             return self._price
#
#
# # test
# sunflower = Flower('Sunflower', 25, 15)
# print(sunflower.get_name(), sunflower.get_petal_count(), sunflower.get_price())

# 5.  Revise the charge and make_payment methods of the CreditCard class to ensure the caller sends a number as a
# parameter.
# class CreditCard():
#     def __init__(self, customer, bank, acnt, limit):
#         self._customer = customer
#         self._bank = bank
#         self._acnt = acnt
#         self._limit = limit
#         self._balance = 0  # beginning balance always $0 upon opening card
#
#     def set_balance(self, value):
#         self._balance = value
#
#     def charge(self, price):
#         try:
#             price = float(price)
#             if price + self._balance > self._limit:
#                 return False
#             else:
#                 self._balance += price
#                 return True
#         except:
#             print("Please enter a number.")
#             return False
#
#     def make_payment(self, amount):
#         try:
#             amount = float(amount)
#             self._balance -= amount
#             return True
#         except:
#             print("Please enter a number.")
#             return False
#
# mk_card = CreditCard('Molly King', 'BOA', 55555, 1000000000)
# print(mk_card.charge(10))
# print(mk_card.charge("banana"))
# print(mk_card.make_payment(.01))
# print(mk_card.make_payment("bitcoin"))

# 6. If the parameter to the make_payment method were a negative number, that would have the effect of raising the
# balance on the account.  Revise the implementation so it raises a ValueError if sent.
# class CreditCard():
#     def __init__(self, customer, bank, acnt, limit):
#         self._customer = customer
#         self._bank = bank
#         self._acnt = acnt
#         self._limit = limit
#         self._balance = 0  # beginning balance always $0 upon opening card
#
#     def set_balance(self, value):
#         self._balance = value
#
#     def charge(self, price):
#         if price + self._balance > self._limit:
#             return False
#         else:
#             self._balance += price
#             return True
#
#     def make_payment(self, amount):
#         if amount >= 0:
#             self._balance -= amount
#             return True
#         else:
#             return ValueError, print("Negative payments not allowed.")

# mk_card = CreditCard('Molly King', 'BOA', 55555, 1000000000)
# print(mk_card.make_payment(.01))
# print(mk_card.make_payment(-1000))

# 10. Implement the __neg__ method for the Vector class so the expression -v returns a new vector instance whose
# coordinates are all negated values of the respective coordinates of v.
# class Vector:
#     def __init__(self, d):
#         self._coords = [0] * d
#
#     def __len__(self):
#         return len(self._coords)
#
#     def __getitem__(self, j):
#         return self._coords[j]
#
#     def __setitem__(self, j, val):
#         self._coords[j] = val
#
#     def __add__(self, other):
#         if len(self) != len(other):
#             raise ValueError('dimensions must agree')
#         result = Vector(len(self))
#         for j in range(len(self)):
#             result[j] = self[j] + other[j]
#         return result
#
#     def __eq__(self, other):
#         return self._coords==other._coords
#
#     def __ne__(self, other):
#         return not self == other
#
#     def __str__(self):
#         return '<' + str(self._coords)[1:-1] + '>'
#
#     def __neg__(self):
#         result = Vector(len(self))
#         for i in range(len(result)):
#             neg_val = i * -1
#             result[i] = neg_val
#         return result
#
# vector_test = Vector(5)
# print(vector_test)
# print(-vector_test)

# 12.  Implement the __mul__ method for the Vector class of 2.3.3 so the expression v * 3 returns a new vector with
# coordinates that are 3 times the respective coordinates of v.
# class Vector:
#     def __init__(self, d):
#         self._coords = [0] * d
#
#     def __len__(self):
#         return len(self._coords)
#
#     def __getitem__(self, j):
#         return self._coords[j]
#
#     def __setitem__(self, j, val):
#         self._coords[j] = val
#
#     def __add__(self, other):
#         if len(self) != len(other):
#             raise ValueError('dimensions must agree')
#         result = Vector(len(self))
#         for j in range(len(self)):
#             result[j] = self[j] + other[j]
#         return result
#
#     def __eq__(self, other):
#         return self._coords == other._coords
#
#     def __ne__(self, other):
#         return not self == other
#
#     def __str__(self):
#         return '<' + str(self._coords)[1:-1] + '>'
#
#     def __mul__(self, int):
#         result = Vector(len(self))
#         for i in range(len(result)):
#             result[i] = i * int
#         return result
#
# v_test = Vector(5)
# print(v_test)
# print(v_test*3)

# 16.  Our Range class depends on the formula max(0, (stop - start + step - 1) // step) to compute the number of
# range elements.  It is not immediately evident this formula provides a correct calculation.  Justify this formula
# in your own words.
# class Range:
#     def __init__(self, start, stop=None, step=1):
#         if step == 0:
#             raise ValueError('step cannot be 0')
#
#         if stop is None:
#             start, stop = 0, start
#
#         self._length = max(0, (stop - start + step - 1) // step)
#
#         self._start = start
#         self._step = step
#
#     def __len__(self):
#         return self._length
#
#     def __getitem__(self, k):
#         if k < 0:
#             k += len(self)
#
#         if not 0 <= k < self._length:
#             raise IndexError('index out of range')
#
#         return self._start + k * self._step

# This is correct because to calculate the length, it looks in all the values of the list and takes the largest one.
# This is done through starting at zero, then finding the difference between the end and the beginning, then adding
# the step / increment level.  One is then subtracted because python starts its first place indexing at 0 but the
# starting position is likely 1 to indicate the first position. The integer of this number divided by step is then
# returned. If this number is larger than zero, it is returned as the max length.

# 20.  What are some potential efficiency disadvantages of having very deep inheritance trees, that is, a large set
# of classes, A, B, C, and so on, so that B extends A, C extends B, D extends C?

# If behavior changes in A without D knowing, could be hard to figure out where the problem is.  Potential for
# namespace conflicts (C references something B doesn't know about).

# 21.  What are some potential efficiency disadvantages of having very shallow inheritance trees, that is,
# a large set of classes, A, B, C, and so on, such that all these classes extend a single class, Z?

# Risks incorrect aliasing.  Also if the two are exact copies but you change one and not the other, then there is
# either a need to duplicate work to change the second object to match or you also risk not updating both places
# correctly.  If any classes change, it will mess up the subclass.  Also namespace conflicts.

# 22. Modify the Sequence class to include a definition for the __eq__ method so that expression seq1 == seq2 will
# return True when the two sequences are element by element equivalent.
# class SequenceIterator:
#     def __init__(self, sequence):
#         self._seq = sequence
#         self._k = -1
#
#     def __next__(self):
#         self._k += 1
#         if self._k < len(self._seq):
#             return (self._seq[self._k])
#         else:
#             raise StopIteration()
#
#     def __iter__(self):
#         return self
#
#     def __eq__(self, other_seq):
#         if self._seq == other_seq:
#             return True
#         else:
#             print("Sequences are not equal")
#             return False
#
#
# seq1 = SequenceIterator(sequence=[1, 2, 3, 4, 5])
# print(seq1 == [1, 2, 3, 4, 5])
# print(seq1 == [1, 1, 1, 1, 1])

# Creativity
# 26.  SequenceIterator provides a forward iterator.  Implement a class named ReversedSequenceIterator that serves as
# a reverse iterator for any sequence type.  First call returns last element and so on.
# class ReversedSequenceIterator:
#     def __init__(self, sequence):
#         self._seq = sequence
#         self._max_count = len(self._seq)
#
#     def __next__(self):
#         self._max_count -= 1
#         if self._max_count > -1:
#             return (self._seq[self._max_count])
#         else:
#             raise StopIteration()
#
#     def __iter__(self):
#         return self
#
#
# seq1 = ReversedSequenceIterator(sequence=[1, 2, 3, 4, 5])
# print([x for x in seq1])

# 28.  Modify PredatoryCreditCard so once a customer has made ten calls to charge in the current month,
# each additional call results in an additional $1 surcharge.
# class CreditCard():
#     def __init__(self, customer, bank, acnt, limit):
#         self._customer = customer
#         self._bank = bank
#         self._acnt = acnt
#         self._limit = limit
#         self._balance = 0  # beginning balance always $0 upon opening card
#
#     def set_balance(self, value):
#         self._balance = value
#
#     def charge(self, price):
#         if price + self._balance > self._limit:
#             return False
#         else:
#             self._balance += price
#             return True
#
#     def make_payment(self, amount):
#         self._balance -= amount
#
# class PredatoryCreditCard(CreditCard):
#     def __init__(self, customer, bank, acnt, limit, apr):
#         super().__init__(customer, bank, acnt, limit)
#         self._apr = apr
#
#     def charge(self, price):
#         '''
#         Charge given price to card assuming sufficient limit.
#         Return true if processed
#         Return false and assess $5 fee if charge is denied.
#         '''
#         success = super().charge(price)
#         if not success:
#             self._balance += 5
#         return success
#
#     def process_month(self):
#         if self._balance > 0:
#             monthly_factor = pow(1 + self._apr, 1/12)
#             self._balance *= monthly_factor


# 29. Modify PredatoryCreditCard so a customer is assigned a minimum monthly payment as a percentage of balance.
# Assess a late fee if the customer does not pay the minimum amount before the next monthly cycle.
# class CreditCard():
#     def __init__(self, customer, bank, acnt, limit):
#         self._customer = customer
#         self._bank = bank
#         self._acnt = acnt
#         self._limit = limit
#         self._balance = 0  # beginning balance always $0 upon opening card
#
#     def set_balance(self, value):
#         self._balance = value
#
#     def charge(self, price):
#         if price + self._balance > self._limit:
#             return False
#         else:
#             self._balance += price
#             return True
#
#     def make_payment(self, amount):
#         self._balance -= amount
#
#
# class PredatoryCreditCard(CreditCard):
#     def __init__(self, customer, bank, acnt, limit, apr):
#         super().__init__(customer, bank, acnt, limit)
#         self._apr = apr
#
#     def charge(self, price):
#         '''
#         Charge given price to card assuming sufficient limit.
#         Return true if processed
#         Return false and assess $5 fee if charge is denied.
#         '''
#         success = super().charge(price)
#         if not success:
#             self._balance += 5
#         return success
#
#     def process_month(self):
#         if self._balance > 0:
#             monthly_factor = pow(1 + self._apr, 1 / 12)
#             self._balance *= monthly_factor

# Projects
