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

print 'Erasing values'
print '-->remove:'
new_list = ['a', 'b', 'c', 'd', 'e']
print new_list
new_list.remove('c')
print "new_list.remove('c') -> ", new_list

print '-->pop:'
new_list = ['a', 'b', 'c', 'd', 'e']
print new_list
new_list.pop(1)
print "new_list.pop(1) -> ", new_list

# Removing values inside for


print help(list)
print '\n------------------------------------------------------------\n'

repetition

print '\n------------------------------------------------------------\n'

membership

print '\n------------------------------------------------------------\n'

iteration

print '\n------------------------------------------------------------\n'

