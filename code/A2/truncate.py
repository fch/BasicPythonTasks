def truncate_to_8(s):
    return s[0:8]

def truncate_to_n(s, n):
    return s[0:n]

def truncate_to_n_dots(s, n):
    return s if len(s) <= 3 else s[0:n-3] + '...'

CheckResult.check(truncate_to_8('hallo'), 'hallo')
CheckResult.check(truncate_to_8('hallotom'), 'hallotom')
CheckResult.check(truncate_to_8('hallosacsac'), 'hallosac')

CheckResult.check(truncate_to_n('hallo', 2), 'ha')
CheckResult.check(truncate_to_n('hallo', 4), 'hall')
CheckResult.check(truncate_to_n('hallo', 6), 'hallo')

CheckResult.check(truncate_to_n_dots('ha', 3), 'ha')
CheckResult.check(truncate_to_n_dots('hal', 3), 'hal')
CheckResult.check(truncate_to_n_dots('hallo', 3), '...')
