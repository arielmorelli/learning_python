print 'http://thecodeship.com/patterns/guide-to-python-function-decorators/'

print '-------------------------------------------------------------------------------------------------'

print '''
What we should know before learn decorators:
    Assign functions of variables
    Define functions inseide functions
    Send functions as parameters
    Functions can return another functions
'''

print '''
Assign functions of variables'

def greet(name):
        return "Hello "+name

        greet_someone = greet
        print greet_someone("John")

'''

def greet(name):
    return "Hello "+name
    
greet_someone = greet
print '>>>', greet_someone("John")

print '-------------------------------------------------------------------------------------------------'

print '''
Define functions inseide functions

def greet(name):
    def get_message():
        return "Hello "

    result = get_message()+name
    return result

print greet("John")
'''

def greet(name):
    def get_message():
        return "Hello "

    result = get_message()+name
    return result

print '>>>', greet("John")

print '-------------------------------------------------------------------------------------------------'

print '''
Send functions as parameters

def greet(name):
   return "Hello " + name 

def call_func(func):
    other_name = "John"
    return func(other_name)  

print call_func(greet)
'''

def greet(name):
   return "Hello " + name 

def call_func(func):
    other_name = "John"
    return func(other_name)  

print '>>>', call_func(greet)

print '-------------------------------------------------------------------------------------------------'

print '''
Functions can return another functions

def compose_greet_func():
    def get_message():
        return "Hello there!"

    return get_message

greet = compose_greet_func()
print greet()
'''

def compose_greet_func():
    def get_message():
        return "Hello there!"

    return get_message

greet = compose_greet_func()
print '>>>', greet()

print '-------------------------------------------------------------------------------------------------'

print '''
Out first decorator! :)

def the_guy_who_decorate(func):
   def func_wrapper(name):
       return "<FROM_DECORATOR>{0}</FROM_DECORATOR>".format(func(name))
   return func_wrapper

@the_guy_who_decorate #  Look at my DECORATOR. My DECORATOR is amazing. Give it a lick. Mmmm, it tastes just like raisins!
def print_a_text(name):
   return "{}".format(name)

print print_a_text("Oh Long Johnson")

'''

def the_guy_who_decorate(func):
   def func_wrapper(name):
       return "<FROM_DECORATOR>{0}</FROM_DECORATOR>".format(func(name))
   return func_wrapper

@the_guy_who_decorate
def print_a_text(name):
   return name

print '>>>', print_a_text("Oh Long Johnson")

print '-------------------------------------------------------------------------------------------------'

print '''
Using many decorators - Order matters!!!!!!!!!!!

def decorator1(func):
   def func_wrapper(name):
       return "(__D1__){0}".format(func(name))
   return func_wrapper

def decorator2(func):  
   def func_wrapper(name):
       return "(__D2__){0}".format(func(name))
   return func_wrapper

@decorator1
@decorator2
def text1(name):
   return name

@decorator2
@decorator1
def text2(name):
   return name

print '1>>>', text1('Narwhals')
print '2>>>', text2('Amazing horse')
'''

def decorator1(func):
   def func_wrapper(name):
       return "(__D1__){0}".format(func(name))
   return func_wrapper

def decorator2(func):  
   def func_wrapper(name):
       return "(__D2__){0}".format(func(name))
   return func_wrapper

@decorator1
@decorator2
def text1(name):
   return name

@decorator2
@decorator1
def text2(name):
   return name

print '1>>>', text1('Narwhals')
print '2>>>', text2('Amazing horse')

print '-------------------------------------------------------------------------------------------------'

print '''
Passing arguments to decorators

def tags(tag_name):
    def tags_decorator(func):
        def func_wrapper(name):
            return "<{0}>{1}</{0}>".format(tag_name, func(name))
        return func_wrapper
    return tags_decorator

@tags("div")
def text1(name):
    return name

@tags("p")
def text2(name):
    return name

print text1("Luke, I am you father")
print text2("NOOOOOOOOOOOOOOOOOOOO")
'''

def tags(tag_name):
    def tags_decorator(func):
        def func_wrapper(name):
            return "<{0}>{1}</{0}>".format(tag_name, func(name))
        return func_wrapper
    return tags_decorator

@tags("div")
def text1(name):
    return name

@tags("p")
def text2(name):
    return name

print '>>>', text1("Luke, I am you father")
print '>>>', text2("NOOOOOOOOOOOOOOOOOOOO")

