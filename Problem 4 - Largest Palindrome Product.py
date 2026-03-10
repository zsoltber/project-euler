'''
Problem 4 - Largest Palindrome Product

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2 digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

import math

palindromes = []

def is_palindrome (n):
    n = str(n)
    if len(n) == 1:
        return True
    for i in range(math.ceil(len(n)/2)):
        if n[i] != n[-i-1]:
            return False
    return True
        
for k in range(1, 1000):
    for j in range(1, 1000):
        if is_palindrome(k * j):
            # print(f'{k * j} is a palindrome made from the product {k} x {j}.')
            palindromes.append(k * j)

print(max(palindromes))
