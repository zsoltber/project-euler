'''
Problem 7 - 10 001st Prime

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''
primes = [2,3,5,7,11,13]

def is_prime(n):
    for p in primes:
        if n % p == 0:
            return False
    return True

# dramatically reduce the required computational capacity by applying that a number either is a prime or has prime implicants smaller than itself
# thus not all numbers smaller than a given number need to be checked to know if it is a prime, only the primes that are smaller than itself

counter = 6 # number of primes found
index = 2 # current number
while counter < 10001:
    if is_prime(index):
        primes.append(index)
        # print(index)
        counter += 1
    index += 1

print(primes[-1])

# Answer: 104743

# e.g. in this case, towards the end of the question there are only AT MOST ~10,000 numbers to be checked below the index during every cycle in comparison to 100,000 
