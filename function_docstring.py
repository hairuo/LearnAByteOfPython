def print_max(x, y):
    '''prints the maximum of two

    The two value muse be integers.'''

    x = int(x)
    y = int(y)

    if x > y:
        print(x, 'is maximum')
    else:
        print(y, 'is maximum')

print_max(3, 5)
print(print_max.__doc__)
