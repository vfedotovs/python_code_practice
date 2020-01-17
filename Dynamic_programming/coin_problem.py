# coins_problem.py
# This is dynamic programing example
"""
Let solve(x) denote the minimum number of coins required for a sum x.
The values of the function depend on the values of the coins. For example, if
coins = {1,3,4}, the first values of the function are as follows:

solve(0) = 0
solve(1) = 1
solve(2) = 2
solve(3) = 1
solve(4) = 1
solve(5) = 2
solve(6) = 2
solve(7) = 2
solve(8) = 2
solve(9) = 3
solve(10) = 3

For example, solve(10) = 3, because at least 3 coins are needed to form the
sum 10. The optimal solution is 3+3+4 = 10.
"""

coins = [1,3,5,7]

def solve(target:int):
	if target < 0:
		return 999  # infinity 
	if target == 0:
		return 0
	best = 999  # infinity 
	for c in coins:
		x = solve(target - c) + 1
		best = min(best, x)
	return best


for i in range(45): ## carefull take lot to calculate 30 plus
	print("Target :", i, "min coin count: ", solve(i))

"""
Code works 
output :
Target : 1 min coin count:  1
Target : 2 min coin count:  2
Target : 3 min coin count:  1
Target : 4 min coin count:  1
Target : 5 min coin count:  2
Target : 6 min coin count:  2
Target : 7 min coin count:  2
Target : 8 min coin count:  2
Target : 9 min coin count:  3
Target : 10 min coin count:  3

"""



