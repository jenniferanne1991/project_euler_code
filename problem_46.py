
# 
# Project Euler problem 46
# Solution written by Jennifer Ralph
# 

import math

# Determines whether a number is prime or not
def is_prime(n):
	for i in range(2, int(math.floor(math.sqrt(n)))+1):
		if n%i == 0:
			return False
	return True

# Given a target number and list of prime numbers
# less than or equal to the target, this function
# tries to write the target as the sum of a prime 
# and twice a square.
def create_sum(target, primes):
	for prime in primes:
		if math.floor(math.sqrt((target-prime)/2)) == math.sqrt((target-prime)/2):
			return prime
	return 0

# Finds the first odd composite number that cannot 
# be written as the sum of a prime and a square.
def disprove_goldbachs_other_conjecture():
	found = False
	current = 3
	primes = [2]
	while not found:
		if is_prime(current):
			primes.append(current)
		else:
			if create_sum(current, primes) == 0:
				return current
		current = current + 2

if __name__ == "__main__":
	print(disprove_goldbachs_other_conjecture())