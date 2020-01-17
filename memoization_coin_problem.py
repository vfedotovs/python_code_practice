# This is dynamic programing example

coins = [1,3,5,7]
t = 200


ready = [False] * t
value = [0] * t


def solve(target:int):
	# meoization with using 2  arrays
	


	#print(ready)
	#print(value)
	if target < 0:
		return 999  # infinity 
	if target == 0:
		return 0
	if ready[target - 1] == True:
		return value[target - 1]
	best = 999  # infinity 
	for c in coins:
		x = solve(target - c) + 1
		best = min(best, x)

	value[target - 1] = best
	ready[target - 1] = True

	return best

for i in range(1,t): ## carefull take lot to calculate 30 plus
	print("Target :", i, "min coin count: ", solve(i))


## code woks counts 200 target in amazing speed sub 1 second
