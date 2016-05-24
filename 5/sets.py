# Diff between list and set
# Venn diagram


print 'Declaring a empty set'
new_set = set()
print new_set, type(new_set)

print '\n------------------------------------------------------------\n'

set_a = set(["Jake", "John"])
set_b = set(["John", "Abcd"])

print 'Union:'
print 'set_a -> ', set_a
print 'set_b -> ', set_b
print set_a | set_b
print set_a.union(set_b)

print '\n------------------------------------------------------------\n'

set_a = set(["Jake", "John"])
set_b = set(["John", "Abcd"])

print 'Inseccao:'
print 'set_a -> ', set_a
print 'set_b -> ', set_b
print set_a & set_b
print set_a.intersection(set_b)

print '\n------------------------------------------------------------\n'

set_a = set(["Jake", "John"])
set_b = set(["John", "Abcd"])

print 'Difference:'
print 'set_a -> ', set_a
print 'set_b -> ', set_b
print set_a - set_b
print set_a.difference(set_b)

print '\n------------------------------------------------------------\n'

set_a = set(["Jake", "John"])
set_b = set(["John", "Abcd"])

print 'Symmetric_difference:'
print 'set_a -> ', set_a
print 'set_b -> ', set_b
print set_a ^ set_b
print set_a.symmetric_difference(set_b)

print '\n------------------------------------------------------------\n'

set_a = set(["Jake"])
set_b = set(["Jake","John", "Abcd"])

print 'Sub set:'
print 'set_a -> ', set_a
print 'set_b -> ', set_b
print set_a < set_b
print set_a.issubset(set_b)

print '\n------------------------------------------------------------\n'

set_a = set(["Jake","John", "Abcd"])
set_b = set(["Jake"])

print 'Super set:'
print 'set_a -> ', set_a
print 'set_b -> ', set_b
print set_a > set_b
print set_a.issuperset(set_b)

print '\n------------------------------------------------------------\n'

print 'Proper sub/super set: when set != other'
set_a = set(["Jake"])
set_b = set(["Jake"])
print 'A is subset of B?', set_a <= set_b
print 'A is proper subset of B?', set_a < set_b


