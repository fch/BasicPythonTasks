WEEKLY_HOURS = 40

def overtime(hours_worked):
    return 0 if hours_worked <= 40 else (hours_worked - WEEKLY_HOURS)


CheckResult.check(overtime(45), 5)
CheckResult.check(overtime(40), 0)
CheckResult.check(overtime(35), 0)
