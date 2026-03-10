'''
Problem 10 - Summation of Primes

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all primes below two million.
'''

import math

primes = []
target = int(2e6)
sqrt_target = math.sqrt(target)

numbers = [x for x in range(2, target)]

def is_prime(n):
    n_sqrt = math.sqrt(n)
    if n == 2:
        return True
    else:
        for p in primes:
            if p < n_sqrt: # each number n has at most 1 primefactor greater than sqrt(n), if none below, then n is prime
                if n % p == 0: 
                    return False
            else:
                break
    return True

index = 2
while index < sqrt_target:
    if is_prime(index):
        primes.append(index)
        for j in range(index ** 2 - 2, target - 2, index):
            numbers[j] = 0
    index += 1

print(sum(numbers))

# Answer: 142,913,828,922
# my basic algorithm idea and speeding up the process:
# define an is_prime algorithm that checks division against a set of previously found prime numbers.
# if n is not a prime, it will have prime implicants smaller than itself, thus only division with primes need to be checked
# 
# second part: create an array containing all numbers between 2 and the target number
# when a prime is found, set all of its multiples to zero over the entire array (the is_prime function returns false for is_prime(0) obviously)
# key insight: only primes up to sqrt(target) need to be considered for the elimination
# all non-primes that are between sqrt(target) and target have at least one prime implicant below sqrt(target) and thus will be eliminated
# the first non-prime that is not eliminated by this method is above the target value
# sum the remaining numbers which are all the primes below the target