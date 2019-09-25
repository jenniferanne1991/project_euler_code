
# 
# Project Euler problem 1
# Solution written by Jennifer Ralph
# 

# Function for determining the sum 1 + 2 + ... + n
def sum(n):
	ans = (n*(n + 1)) / 2
	return ans

# Determine the sum of integers less than or equal
# to the maximum that are a multiple of n.
# Note that n + 2n + ... + xn is equal to 
# n(1 + 2 + ... + x), and we use the latter form.
def sum_one_factor(n, maximum):
	occurences = maximum / n
	ans = n * sum(occurences)
	return ans


# Determines the sum of each multiple of mult_one and 
# mult_two less than the specified maximum
def sum_two_factors(fact_one, fact_two, maximum):
	ans = sum_one_factor(fact_one, maximum) + sum_one_factor(fact_two, maximum)\
	- sum_one_factor(fact_one*fact_two, maximum)
	return ans


if __name__ == "__main__":
	print(sum_two_factors(3,5,999))