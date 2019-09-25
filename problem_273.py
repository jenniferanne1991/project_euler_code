
# 
# Project Euler problem 273
# Solution written by Jennifer Ralph
# 

import math

# Determines whether a number is prime or not
def is_prime(n):
	for i in range(2, int(math.sqrt(n)+1)):
		if n%i == 0:
			return False
	return True

# Lists all prime numbers of the form 4k+1 below a
# specified maximum
def one_mod_four_primes(maximum):
	current = 5
	ans = []
	while current < maximum:
		if is_prime(current):
			ans.append(current)
		current = current + 4
	return ans

# Lists squarefree numbers that are only divisible
# by specified factors
def squarefree_numbers(factors):
	if len(factors) == 0:
		return []
	first = factors[0]
	ans = [first]
	factors.pop(0)
	temp = squarefree_numbers(factors)
	ans.extend(temp)
	ans.extend([i*first for i in temp])
	return ans

# Returns the unique solution of a^2 + b^2 = N, where N
# is prime and 0 < a <= b, a, b, N integers. Note that if
# N is congruent to 3 mod 4, no solutions exist and the 
# function will return 0
def root_summands_of_prime(N):
	if N%4 == 3:
		return 0
	a = 0
	maximum = math.sqrt(N/2)
	while a <= maximum:
		a_squared = a**2
		b_squared = N - a_squared
		b = math.sqrt(b_squared)
		if b == round(math.sqrt(b_squared)):		
			return [a, int(b)]
		a = a + 1


def root_summands_of_composite(summands_list):
	if len(summands_list) == 0:
		return []
	first = summands_list[0]
	ans = [first]
	summands_list.pop(0)
	temp = root_summands_of_composite(summands_list)
	for t in temp:
		ans.append(t)
		ans.append([first[0]*t[0]+first[1]*t[1], abs(first[0]*t[1]-first[1]*t[0])])
		ans.append([first[0]*t[1]+first[1]*t[0], abs(first[0]*t[0]-first[1]*t[1])])
	return ans

def add_mins(summands_list):
	total = 0
	for summands in summands_list:
		total += min(summands)
	return total

def overall_solution(maximum):
	primes = one_mod_four_primes(maximum)
	summands_list = []
	for p in primes:
		summands_list.append(root_summands_of_prime(p))
	summands_list = root_summands_of_composite(summands_list)
	sum_s_of_n = add_mins(summands_list)
	return sum_s_of_n

if __name__ == "__main__":
	print(overall_solution(150))
