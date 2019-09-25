
# 
# Project Euler problem 6
# Solution written by Jennifer Ralph
# 

# Function for determining the sum 1 + 2 + ... + n
def sum(n):
	ans = (n*(n + 1)) / 2
	return ans


# Function for determining the sum 1^2 + 2^2 + ... + n^2
def squares_sum(n):
	ans = (n*(n + 1)*(2*n + 1)) / 6
	return ans


# Difference between sum^2 and squares_sum
def square_sums_difference(n):
	ans = sum(n) ** 2 - squares_sum(n)
	return ans


if __name__ == "__main__":
	print(square_sums_difference(100))