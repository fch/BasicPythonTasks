def fib_rec(n):
    if n == 0:
        return 0
    return 1 if n < 2 else fib_rec(n-1) + fib_rec(n-2)

def fib_it(n):
    if n == 1:
        return 1
    fib = 0
    fib_1 = 1
    fib_2 = 0
    for i in range(2, n+1):
        fib = fib_1 + fib_2
        fib_2 = fib_1
        fib_1 = fib
    return fib

CheckResult.check(fib_rec(0), 0)
CheckResult.check(fib_rec(1), 1)
CheckResult.check(fib_rec(2), 1)
CheckResult.check(fib_rec(3), 2)
CheckResult.check(fib_rec(4), 3)
CheckResult.check(fib_rec(5), 5)

CheckResult.check(fib_it(0), 0)
CheckResult.check(fib_it(1), 1)
CheckResult.check(fib_it(2), 1)
CheckResult.check(fib_it(3), 2)
CheckResult.check(fib_it(4), 3)
CheckResult.check(fib_it(5), 5)
