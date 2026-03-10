'''
Problem 5 - Smallest Multiple

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

# i think the solution is quite simple to do analytically on paper, less so using python, but the general principle
# is to find prime divisors of the numbers from 1 to 20 first and then multiply them all together in a way that we 
# take the maximum required power of each prime divisor

prime_divisors = {x:[] for x in range(2, 21)}
# print(prime_divisors)

def is_prime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

def find_prime_implicants (n):
    rem = n
    while rem > 1:
        for i in range(2, rem + 1):
            if is_prime(i) and rem % i == 0:
                rem = rem // i
                prime_divisors[n].append(i)
                break

for i in range (2,21):
    find_prime_implicants(i)

print(prime_divisors) # found prime implicants of each number from 2 to 20 and listed in dict

required = {x:0 for x in range(2, 21)}

for number, implicant in prime_divisors.items():
    for i in implicant:
        if implicant.count(i) > required[i]:
            required[i] = implicant.count(i)
        
print(required) # found what power each implicant has to be in solutino

sm = 1
for prime, power in required.items():
    sm *= (prime ** power)
print(sm) # calculated smallest multiple that is evenly divisible by all numbers from 1 to 20

# Answer: 232,792,560
