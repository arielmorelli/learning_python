print '''Files: read, write and with clause

print open(name[, mode[, buffering]])
print Modes:
print r : Only for read. Do not create a new file.
print r+: Read and write. Do not create a new file.
print w : Only write. The file is created if it does not exist, otherwise will erase the one.
print w+: Write and read. The file is created if it does not exist, otherwise will erase the one.
print a : Only write. The file is created if it does not exist.
print a+: Read and write. The file is created if it does not exist.
'''

print '''
Writing file:
file_handler = open('/tmp/example.txt')
'''

try:
    file_handler = open('/tmp/example.txt')
except Exception as e:
    print 'Error: {}'.format(e)


print '''
Creating a file:
file_handler = open('/tmp/example.txt', 'w')
file_handler.write('Hello from file!\n')
file_handler.write('This is the second line.')
'''

file_handler = open('/tmp/example.txt', 'w')
file_handler.write('Hello from file!\n')
file_handler.write('This is the second line.')

print '''
Closing handler.
file_handler.close()
'''

file_handler.close()

print '''
Reading file
file_handler = open('/tmp/example.txt', 'r')
'''

file_handler = open('/tmp/example.txt', 'r')

print 'Init file:'
for line in file_handler.readlines():
    print '\t{}'.format(line)
print 'EOF'

print '\n----------------------------------------------------------------------'

print '''
Closing handler:
file_handler.close()
'''
file_handler.close()

print '''
Using with clause:
with something() as named_something:
    <CODE HERE>
'''

print '''
Same as:
named_something = something()
named_something.__enter__()
<CODE HERE>
named_something.__exit__()
'''

print '''
Example:
with open('/tmp/new_example.txt', 'a+') as file_handler:
    file_handler.write('First line!\\n')
    file_handler.write('Second line!')
'''

with open('/tmp/new_example.txt', 'a+') as file_handler:
    file_handler.write('First line of the new file!\n')
    file_handler.write('Second line of the new file!')
    file_handler.seek(0)
    print 'Reading the file:'
    for line in file_handler.readlines():
        print '\t{}'.format(line)
    print 'EOF'

print 'print file_handler'
print file_handler
