def sum_it(n):
    sum = 0
    for i in range(0, n+1, 2):
        sum += i ** 3
    return sum

def sum_rec(n):
    if n % 2 == 1:
        n -= 1
    if n > <= 0:
        return 0
    return sum_rec(n-2) + n ** 3

def sum_acc(n, acc):
    if n % 2 == 1:
        n -= 1
    if n <= 0:
        return acc
    return sum_acc(n-2, acc + n ** 3)

CheckResult.check(sum_it(0), 0)
CheckResult.check(sum_it(1), 0)
CheckResult.check(sum_it(2), 8)
CheckResult.check(sum_it(3), 8)
CheckResult.check(sum_it(4), 72)

CheckResult.check(sum_rec(0), 0)
CheckResult.check(sum_rec(1), 0)
CheckResult.check(sum_rec(2), 8)
CheckResult.check(sum_rec(3), 8)
CheckResult.check(sum_rec(4), 72)

CheckResult.check(sum_acc(0), 0)
CheckResult.check(sum_acc(1), 0)
CheckResult.check(sum_acc(2), 8)
CheckResult.check(sum_acc(3), 8)
CheckResult.check(sum_acc(4), 72)
