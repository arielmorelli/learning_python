# -*- coding: utf-8 -*-

print 'Declaring a empty list'
new_list = list()
print new_list, type(new_list)
new_list = []
print new_list, type(new_list)

print '\n------------------------------------------------------------\n'

print 'Declaring a populated list:'
new_list = [1, 2, 3]  # Int list
print new_list, type(new_list), [type(a) for  a in new_list]

new_list = ['a', 1, ['inside', 'list'], {'a': 'a value', 'b': 'b value'}] # List with many types
print new_list, type(new_list), [type(a) for  a in new_list]

print '\n------------------------------------------------------------\n'

print 'Acessing a element in list:'
new_list = ['a', 'b', 'c', 'd', 'e']
print new_list
print 'new_list[0] -> ', new_list[0]
print 'new_list[1] -> ', new_list[1]
try:
    print 'new_list[98]:', new_list[98]
except Exception as e:
    print e

print '\n------------------------------------------------------------\n'

print 'Slicing a list:'
new_list = ['a', 'b', 'c', 'd', 'e']
print 'list ', new_list
print 'new_list[1:3] -> ', new_list[1:3]
print 'new_list[::2] -> ', new_list[::2]

print '\n------------------------------------------------------------\n'

# Lembrar que listas são circulares! Valores negativos são o mesmo que ir do último elemento pro primeiro.

print new_list
print 'new_list[-1] -> ', new_list[-1]
print 'new_list[-3] -> ', new_list[-3]
try:
    print 'new_list[-3]:', new_list[-99]
except Exception as e:
    print e

print '\n------------------------------------------------------------\n'

print 'Updating lists:'
new_list = ['a', 'b', 'c', 'd', 'e']
print new_list
new_list[1] = 'new_value'
print "new_list[1] = 'new_value' -> ", new_list

print '\n------------------------------------------------------------\n'

print 'Appending values - append, insert, concat:'
# Diff:
# Append, insert: no return
# Concat: has return, create a new list
print '\n-->Append:'
new_list = ['a', 'b', 'c', 'd', 'e']
print new_list
new_list.append('new_value')
print "new_list.append('new_value')' -> ", new_list

print '\n-->Insert:'
new_list = ['a', 'b', 'c', 'd', 'e']
print new_list
new_list.insert(0, 'new_value')
print "new_list.insert(0, 'new_value')' -> ", new_list
new_list = ['a', 'b', 'c', 'd', 'e']
new_list.insert(2, 'new_value')
print "new_list.insert(2, 'new_value')' -> ", new_list

print '\n-->Concatenation:'
new_list_1 = ['1', '2']
print 'new_list_1 -> ', new_list_1
new_list_2 = ['98', '99']
print 'new_list_2 -> ', new_list_2
print 'new_list_1 + new_list_2 -> ', new_list_1 + new_list_2

print '\n------------------------------------------------------------\n'

print 'Delete elements:'
print '\n-->remove(x)'
new_list = ['a', 'b', 'c', 'd', 'e', 'b']
print new_list
new_list.remove('b')
print "new_list.remove('b') -> ", new_list

print '\n-->pop()'
new_list = ['a', 'b', 'c', 'd', 'e']
print new_list
new_list.pop()
print "new_list.pop() -> ", new_list

print '\n-->pop(index)'
new_list = ['a', 'b', 'c', 'd', 'e']
print new_list
new_list.pop(3)
print "new_list.pop(3) -> ", new_list

print '\n-->using del'
new_list = ['a', 'b', 'c', 'd', 'e']
print new_list
del new_list[1]
print "del new_list[1] -> ", new_list

print '\n------------------------------------------------------------\n'

print 'Repetition:'
new_list = ['a']
print new_list
print "new_list*3 -> ", new_list*3

print '\n------------------------------------------------------------\n'

print 'Looking for a element:'
print '\n-->Using in:'
new_list = ['a', 'b', 'c', 'd', 'e']
print "'a' in new_list-> ", new_list

print '\n-->Using index:'
new_list = ['a', 'b', 'c', 'd', 'e']
print "new_list.index('c') -> ", new_list.index('c')

print '\n-->Using index when not exist:'
new_list = ['a', 'b', 'c', 'd', 'e']
try:
    print "new_list.index('z') -> ", new_list.index('z')
except Exception as e:
    print e

print '\n-->Using count:'
new_list = ['a', 'b', 'c', 'd', 'e']
print "new_list.count('a') -> ", new_list.count('a')

print '\n------------------------------------------------------------\n'

print 'Iterating (summing + 10):'

print '\n-->Using for + len:'
new_list = [1, 2, 3] 
for index in range(len(new_list)):
    print new_list[index] + 1

print '\n-->Using for:'
new_list = [1, 2, 3] 
for elem in new_list:
    print elem + 1

print '\n-->The pythonic way'
print [elem+1 for elem in new_list]

print '\n------------------------------------------------------------'
print '------------------------------------------------------------'
print '------------------------------------------------------------'
print '------------------------------------------------------------'
print '------------------------------------------------------------\n'

print 'But, how do I remove elements durint a iteraction?'

print '\n-->Using while + del:'
new_list = ['a', 'b', 'a', 'c', 'a', 'd'] 
while 'a' in new_list:
    new_list.remove('a')
print new_list

print '\n-->Using reversed:'
new_list = ['a', 'b', 'a', 'c', 'a', 'd']
for elem in reversed(new_list):
    if elem == 'a':
        new_list.remove(elem)
print new_list

