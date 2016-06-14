#Lambda functions: anonymous functions (i.e. functions that are not bound to a name) at runtime

print 'http://www.secnetix.de/olli/Python/lambda_functions.hawk'

print '\nNormal function: def f (x): return x**2'
print 'Lambda function: l = lambda x: x**2'


def normal_function(x):
    return x**2

l = lambda x: x**2

print 'Return normal function:', normal_function(4)
print 'Return lambda:', l(4)

print '\n------------------------------------------------------------'
print 'Examples:'
print '\nUsing REDUCE - sum of all elements'
print 'Reduce: reduce a iterable to a single item.'
print 'Usage: reduce(function, iterable, initializer=None). The function must be a 2 arguments: (accum_value, x)'
print 'Base: [1, 3, 5, 7, 9]'
print 'reduce(lambda x, y: x + y, base)'

base = [1, 3, 5, 7, 9]

print reduce(lambda x, y: x + y, base)


print '\nUsing MAP - if the number is even'
print 'Map: change the elements of the list using a function.'
print 'Usage: map(function, iterable). The function must be a 2 arguments: (function, itable)'
print 'Base: [1, 2, 3, 4, 5, 6]'
print 'map(lambda x: x % 2 == 0, base)'


base = [1, 2, 3, 4, 5, 6]

print map(lambda x: x % 2 == 0, base)



