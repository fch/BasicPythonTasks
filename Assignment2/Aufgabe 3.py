
def truncate_to_n_dots(string, n):
    return truncate_to_n(string, n) + '...'

def truncate_to_n(string, n):
    return string[:(int(n))]


def truncate_to_8(string):
    return string[:8]


print('Super-Test  Nudel : ' + truncate_to_8('Nudel'))
print('Super-Test welcomeTestObject : ' + truncate_to_8('welcomeTestObject'))

print("truncate_to_n : " + truncate_to_n("dadasdadasddsa", 6))

print("truncate_to_n_dots : " + truncate_to_n_dots("dadasdadasddsa", 6))
