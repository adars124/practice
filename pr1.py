import random as rd
import string
from _collections_abc import Iterable
import math

""" Reinforcement Section"""

"""
1) Write a short Python function, is multiple(n, m), that takes two integer
values and returns True if n is a multiple of m, that is, n = mi for some
integer i, and False otherwise.
"""
def is_multiple(n: int, m: int) -> bool:
    return True if n % m == 0 else False

print(is_multiple(40, 2))
        
"""
2) Write a short Python function, is_even(k), that takes an integer value and
returns True if k is even, and False otherwise. However, your function
cannot use the multiplication, modulo, or division operators.
"""
def is_even(k: int) -> bool:
    """
    Shifting an integer one bit to the righ is effectively the same as dividing by 2
    and truncating the result.
    """
    return k == (k >> 1) + (k >> 1)

print(is_even(10))

"""
3) Write a short Python function, minmax(data), that takes a sequence of
one or more numbers, and returns the smallest and largest numbers, in the
form of a tuple of length two. Do not use the built-in functions min or
max in implementing your solution
"""
def minmax(data: list[int]) -> tuple[int, int]:
    if len(data) == 0:
        raise IndexError("Empty List!")
    
    max = data[0]
    min = data[0]
    
    for i in data:
        if i > max:
            max = i
        if i < min:
            min = i
    
    return min, max

print(minmax([1]))

"""
4) Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the positive integers smaller than n
"""
def sqsm(n: int) -> int:
    sum = 0
    if n > 0:
        if n == 1:
            return 1
        for i in range(n):
            sum += i**2
    else:
        raise ValueError("Number should be positive!")
        
    return sum 

print(sqsm(3))

"""
5) Give a single command that computes the sum from Exercise R-1.4,
relying on Python's comprehension syntax and the built-in sum function.
"""
def sqsm1(n: int) -> int:
    return sum(i**2 for i in range(n))

print(sqsm1(4))

"""
6) Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the odd positive integers smaller than n.
"""
def sqsm_odd(n: int) -> int:
    n -= 1
    sum = 0
    
    while n > 0:
        if n % 2 == 1:
            sum += n**2
        n -= 1
        
    return sum

print(sqsm_odd(6))

"""
7) Give a single command that computes the sum from Exercise R-1.6, rely-
ing on Python's comprehension syntax and the built-in sum function.
"""
def sqsm_odd1(n: int) -> int:
    return sum(i**2 for i in range(n) if i % 2 == 1)

print(sqsm_odd1(6))

"""
8) Python allows negative integers to be used as indices into a sequence,
such as a string. If string s has length n, and expression s[k] is used for 
index -n ≤ k < 0, what is the equivalent index j ≥ 0 such that s[j] references
the same element?
"""
def equivalent_index(msg: str) -> None:
    n = len(msg) # length of string
    for k in range(-n, 0):
        print(msg[k], end=" ") # prints (h, e, l, l, o) = (-5, -4, -3, -2, -1)
        
    print()
    
    for j in range(-n, 0):
        print(msg[j + n], end=" ") # prints (h, e, l, l, o) = ((-5 + 5), (-4 + 5), (-3 + 5), (-2 + 5), (-1 + 5))
                                                        #   = (0, 1, 2, 3, 4)
    print()    
        
equivalent_index("hello")

"""
9) What parameters should be sent to the range constructor, to produce a
range with values 50, 60, 70, 80?
"""
for i in range(50, 90, 10):
    print(i, end=", ")

print()

"""
10) What parameters should be sent to the range constructor, to produce a
range with values 8, 6, 4, 2, 0, -2, -4, -6, -8?
"""
for i in range(8, -10, -2):
    print(i, end=", ")

print()

"""
11) Demonstrate how to use Python's list comprehension syntax to produce
the list [1, 2, 4, 8, 16, 32, 64, 128, 256].
"""
lst = [2**i for i in range(0, 9)]
print(lst)

"""
12) Python's random module includes a function choice(data) that returns a
random element from a non-empty sequence. The random module in-
cludes a more basic function randrange, with parameterization similar to
the built-in range function, that return a random choice from the given
range. Using only the randrange function, implement your own version
of the choice function.
"""
def custom_choice(data: list) -> int | str:
    return data[rd.randrange(0, len(data)-1)]

seq = "hello world"
print(custom_choice(data=seq))

"""Creativity Section"""

"""
13) Write a pseudo-code description of a function that reverses a list of n
integers, so that the numbers are listed in the opposite order than they
were before, and compare this method to an equivalent Python function
for doing the same thing.
"""
seq = [1, 3, 5, 7, 9, 11]
def reverse_list(data: list[int]) -> list[int]:
    return data[::-1]

print(reverse_list(seq))
print(list(reversed(seq))) # comparision with an equivalent function

"""
14) Write a short Python function that takes a sequence of integer values and
determines if there is a distinct pair of numbers in the sequence whose
product is odd.
"""
def find_odd_pair(data: list[int]) -> bool:
    count = 0
    for i in data:
        if i % 2:
            count += 1
    return count >= 2

mix = [1, 5, 2, 3, 8, 7]
evens = [2, 4, 6, 8, 10, 12, 14]
data = [1, 3, 5, 7]

print(find_odd_pair(mix)) # returns True
print(find_odd_pair(evens)) # returns False
print(find_odd_pair(data))

"""
15) Write a Python function that takes a sequence of numbers and determines
if all the numbers are different from each other (that is, they are distinct).
"""
def find_distinct(data: list[int]) -> bool:
    s = list(set(data))
    if len(data) == len(s):
        return True
    
    return False
    
d = [1, 4, 32, 12, 10, 8, 4, 29, 2, 3, 4]    
print("All are distinct") if find_distinct(mix) else print("Not all are distinct!")

# Scaling function
def scale(data, factor):
    for j in range(len(data)):
        data[j] *= factor

    return data
print(scale(mix, 2))

"""
18) Demonstrate how to use Python's list comprehension syntax to produce
the list [0, 2, 6, 12, 20, 30, 42, 56, 72, 90].
"""
lst = [i * (i - 1) for i in range(1, 11)] # 0, 2, 6, 12, 20, 30, 42, 56, 56, 72, 90
print(lst)

"""
19) Demonstrate how to use Python's list comprehension syntax to produce
the list [ a , b , c , ..., z ], but without having to type all 26 such
characters literally.
"""
alpha = [chr(i) for i in range(97, 123)]
print(alpha)

"""
20) Python's random module includes a function shuﬄe(data) that accepts a
list of elements and randomly reorders the elements so that each possi-
ble order occurs with equal probability. The random module includes a
more basic function randint(a, b) that returns a uniformly random integer
from a to b (including both endpoints). Using only the randint function,
implement your own version of the shuﬄe function.
"""
def my_shuffel(data: list) -> list:
    for i in range(0, len(data) - 1):
        j = rd.randint(0, i)
        data[i], data[j] = data[j], data[i]

my_shuffel(lst)
print(lst)

"""
22) Write a short Python program that takes two arrays a and b of length n
storing int values, and returns the dot product of a and b. That is, it returns
an array c of length n such that c[i] = a[i] · b[i], for i = 0, . . . , n - 1.
"""
def find_dot(a: list[int], b: list[int]) -> list[int]:
    if len(a) != len(b):
        raise ValueError("Please input two square matrices.")
    
    c = [a[i] * b[i] for i in range(len(a))]
    return c

print(find_dot([2, 4, 5, 6], [1, 2, 3, 4]))

"""
23) Give an example of a Python code fragment that attempts to write an ele-
ment to a list based on an index that may be out of bounds. If that index
is out of bounds, the program should catch the exception that results, and
print the following error message:
“Don't try buffer overflow attacks in Python!”
"""
try:
    mix[13] = 2
except IndexError:
    print("Don't try buffer overflow attacks in Python!")
    
"""
24) Write a short Python function that counts the number of vowels in a given
character string.
"""
def count_vowel(msg: str) -> int:
    count = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    for i in msg:
        if i.lower() in vowels:
            count += 1
    
    return count

st = input("Enter any text: ")
print(f"There are {count_vowel(st)} vowels in the given string.")

"""
25) Write a short Python function that takes a string s, representing a sentence,
and returns a copy of the string with all punctuation removed. For exam-
ple, if given the string "Let's try, Mike.", this function would return
"Lets try Mike".
"""
def rem_punctuation(msg: str) -> str:
    copy = ""
    # puncs = """~!@#$%^&*()-+_{}[]|\\;\":'<>,.?/"""
    for i in msg:
        if i not in string.punctuation:
            copy += i
            
    return copy

print(rem_punctuation("Let's try Mike."))

"""
27) In Section 1.8, we provided three different implementations of a generator that computes factors of a given integer. 
The third of those implementations, from page 41, was the most efﬁcient, but we noted that it did not yield the factors 
nincreasing order. Modify the generator so that it reports factors in increasing order, while maintaining its general 
performance advantages.
"""
def sorted_factor(n: int) -> Iterable:
    k = 1
    while k*k < n:
        if n % k == 0:
            yield k
        k += 1
        
    if k*k == n:
        yield k
        
    while k <= n//2:
        k += 1
        if n % k == 0:
            yield k

    yield n
    
for fact in sorted_factor(512):
    print(fact)
    
"""
28) The p-norm of a vector v =( v1,v2,...,vn) in n-dimensional space is deﬁned as ||v||= (vp1 +vp2 +···+vpn) ^ (1/p).
For the special case of p = 2, this results in the traditional Euclidean norm, which represents the length 
of the vector. For example, the Euclidean norm of a two-dimensional vector with coordinates (4,3) has a 
Euclidean norm of √4^2 + √3^2 =√16+9 =√25 = 5. Give an implementation of a function named norm such that norm(v, p) 
returns the p-norm value of v and norm(v) returns the Euclidean norm of v. You may assume that v is a list of numbers.
"""
def p_norm(V, p: int = 2):
    out = sum(v**p for v in V)
    return math.sqrt(out)

n = [3, 4]
print(p_norm(n))


"""Birthday Paradox"""
def birthday_paradox(n: int) -> float:
    prob = 1
    for i in range(0, n):
        prob *= (365-i) / 365
        
    return 1 - prob

print(birthday_paradox(23))
            
            