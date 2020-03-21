def fib_3(n: int) ->int:
    if n == 1 or n == 2:
        result = 1
    bottom_up = [None] * (n + 1)
    bottom_up[1] = 1
    bottom_up[2] = 1

    for i in range(3, n + 1):
        bottom_up[i] = bottom_up[i - 1] + bottom_up[i - 2]

    return bottom_up[n]


for i in range(5, 1105, 100):  # must start at least n = 2 
    print(fib_3(i))


#this is 3rd dynamic programming example best one 
# faster than memo + resursion and solves limit  1000 rec calls 
