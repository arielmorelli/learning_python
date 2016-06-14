# -*- coding: utf-8 -*-

print 'Declaring a empty dict'
new_dict = dict()
print new_dict, type(new_dict)
new_dict = {}
print new_dict, type(new_dict)

print '\n------------------------------------------------------------\n'

print 'Declaring a populated dict:'
new_dict = {'a': 'a value', 'b': 125}
print new_dict
new_dict = dict(one=1, two=2, three=3)
print new_dict
new_dict = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
print new_dict
new_dict = dict([('two', 2), ('one', 1), ('three', 3)])
print new_dict
new_dict = dict({'three': 3, 'one': 1, 'two': 2})
print new_dict

print '\n------------------------------------------------------------\n'

print 'Acessing a element in dict:'
new_dict = {'a': 'a value', 'b': 125}
print new_dict
print "new_dict[a] -> ", new_dict['a']
print "new_dict.get('b') -> ", new_dict.get('b')
print "new_dict.get('x', 'defaul return value') -> ", new_dict.get('x', 'defaul return value')
print "new_dict['row']:", new_dict.get('row')
try:
    print "new_dict['row']:", new_dict['row']
except Exception as e:
    print 'Error:', e

print '\n------------------------------------------------------------\n'

print 'Updating dicts:'
new_dict = {'a': 'a value', 'b': 125}
new_dict['b'] = 'new_value'
print "new_dict['b'] = 'new_value' -> ", new_dict

print '\n------------------------------------------------------------\n'

print 'Appending values:'
new_dict = {'a': 'a value', 'b': 125}
new_dict['c'] = 'value of c'
print "new_dict['c'] = 'value of c' -> ", new_dict

print '\n------------------------------------------------------------\n'

print 'Delete elements:'
new_dict = {'a': 'a value', 'b': 125}
print new_dict
del new_dict['a']
print "del new_dict['a'] -> ", new_dict

print '\n------------------------------------------------------------\n'

print 'Looking for a element:'
print '\n-->Key in dict:'
new_dict = {'a': 'a value', 'b': 125}
print "'a' in new_dict-> ", 'a' in new_dict

print '\n------------------------------------------------------------\n'

print 'Iterating:'

new_dict = {'a': 'a value', 'b': 125}
for key, value in new_dict.iteritems():
        print key, value

print '\n------------------------------------------------------------'
print '------------------------------------------------------------'
print '------------------------------------------------------------'
print '------------------------------------------------------------'
print '------------------------------------------------------------\n'

print 'But, how do I remove elements during a iteraction?'

print '\n-->Using aux list of keys:'
new_dict = {'a': 222, 'b': 100, 'c': 222, 'd': 500, 'e': 222, 'f':222, 't': 400}
print new_dict
keys_to_remove = [key for key, value in new_dict.iteritems() if value == 222]
[new_dict.pop(key) for key in keys_to_remove]
print new_dict

print '\n-->Using copy of the dict:'
new_dict = {'a': 222, 'b': 100, 'c': 222, 'd': 500, 'e': 222, 'f':222, 't': 400}
print new_dict
for key, value in new_dict.copy().iteritems():
    if value == 222:
        del new_dict[key]
print new_dict

