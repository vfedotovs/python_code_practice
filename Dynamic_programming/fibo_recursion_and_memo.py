

def fib_2(n: int, memo: list) ->int:
    if memo[n] is not None:
        return memo[n]

    if n == 1 or n == 2:
        result = 1

    else:
        result = fib_2(n - 1, memo) + fib_2(n - 2, memo)
        memo[n] = result

    return result


def fib_mem(n):
    memo = [None] * (n + 1)
    return fib_2(n, memo)


for i in range(1, 41, 5):
    print(fib_mem(i))


# original fib resursion algo tome is O(2 in nth)
# memoized performance is O(n)
# this is faster thag general recursion becauses is memorizing mig results in cashe
# algo is quick but hit recursion call limit of 1000
# bottom up is solution fot ulimited

# bothom up works around call limit of 1000 and is O(n)


