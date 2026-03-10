'''
Problem 3 - Largest Prime Factor

The prime factors of 13195 are 5, 7, 13 and 29. What is the largest prime factor of the number 600851475143
'''

import math

x = 600851475143
factors = []

def prime(n):
    for i in range (2, n):
        if n % i == 0:
            return False
    return True

# remainder = x # remainder starts at the same as the number to be factorized
# while remainder > 1:
#     div = False
#     for p in primes: # first check in primes array
#         if x % p == 0:
#             remainder = remainder / p
#             print(remainder)
#             factors.append(p)
#             div = True
#             break
#     if not div:
#         for p in range (primes[-1], remainder):
#             if prime(p):
#                 primes.append(p) # add newly found prime to the array
#                 if x % p == 0:
#                     remainder = remainder / p
#                     print(remainder)
#                     factors.append(p)
#                     break

# print(p)
# print(factors)

# simple brute force solution
remainder = 600851475143
while remainder > 1:
    for i in range(2, remainder + 1):
        if prime(i) and remainder % i == 0:
            remainder = remainder // i # is there a problem here that when dividing numbers in python, due to computer arithmetic some small decimal representation errors might arise?
            print(remainder)
            factors.append(i)
            break
print(factors)