# https://www.geeksforgeeks.org/python-scope-of-variables/


# global - It would be impossible to assign to a global variable without global, although free variables may refer to globals without being declared global.
# nonlocal - The statement allows encapsulated code to rebind variables outside of the local scope besides the global (module) scope.


# my_var = 3
# # The variable is global because any Python function or class defined in this module or notebook, is able to access this variable
#
#  def my_first_func():
# ...     # my_func can 'see' the global variable
# ...     print('I see "my_var" = ', my_var, ' from "my_first_func"')
# >>> my_first_func()
# I see "my_var" =  3  from "my_first_func"
# Variables defined inside a function or class, are not global. Only the function or class can see the variable:
#
# >>> def my_second_func():
# ...     a = 10
# ...     print('I see "a" = ', a, 'from "my_second_func"')
# >>> my_second_func()
# I see "a" =  10 from "my_second_func"


# Types of Python Variable Scope:
# - local scope
# - enclosing scope
# - global scope
# - built-in scope
#
# However, it is bad practice to try to manipulate global values from inside local scopes. Try to pass it as a parameter to the function.



# https://www.geeksforgeeks.org/python-scope-of-variables/

# Global variables are the ones that are defined and declared outside any function and are not specified to any function.\
# They can be used by any part of the program.
#
# Example:

# # This function uses global variable s
# def f():
#     print(s)
#     # Global scope
# s = "I love Geeksforgeeks"
# f()


# # This function has a variable with name same as s.
# def f():
#     s = "Me too."
#     print(s)
#
# # Global scope
# s = "I love Geeksforgeeks"
# f()
# print(s)
# # As there is no local s, the value from the global s will be used.


# def f():
#     print(s)
#
#     # This program will NOT show error
#     # if we comment below line.
#     s = "Me too."
#     print(s)
#
# # Global scope
# s = "I love Geeksforgeeks"
# f()
# print(s)


# To make the above program work, we need to use global keyword. We only need to use global keyword in a function
# if we want to do assignments / change them. global is not needed for printing and accessing.
# Any variable which is changed or created inside of a function is local, if it hasn’t been declared as a global variable.

# # This function modifies global variable 's'
# def f():
#     global s
#     print(s)
#     s = "Look for Geeksforgeeks Python Section"
#     print(s)
#
# s = "Python is great !"
# f()
# print(s)


# In Python, nonlocal keyword is used in the case of nested functions.

# This keyword works similar to the global, but rather than global, this keyword declares a variable to point to the
# variable of outside enclosing function, in case of nested functions.

# # Example:
# print("Value of a using nonlocal is : ", end="")
# def outer():
#     a = 5
#     def inner():
#         nonlocal a
#         a = 10
#     inner()
#     print(a)
# outer()
#
# # demonstrating without non local
# print("Value of a without using nonlocal is : ", end="")
# def outer():
#     a = 5
#     def inner():
#         a = 10
#     inner()
#     print(a)
# outer()









# https://realpython.com/python-scope-legb-rule/



# global variable - A variable declared outside the function is called global function.
# local variable - A variable declared inside the function is called local function.


print(globals())
print(locals())


# In which order does Python search the different levels of namespaces? It uses the LEGB-rule,
# which stands for Local -> Enclosed -> Global -> Built-in.
# - Local
#     Local (or function) scope is the code block or body of any Python function or lambda expression.
#     This Python scope contains the names that you define inside the function. These names will only be visible
#     from the code of the function. It’s created at function call, not at function definition, so you’ll have as
#     many different local scopes as function calls. This is true even if you call the same function multiple times,
#     or recursively. Each call will result in a new local scope being created.
# - Enclosing
#     Enclosing (or nonlocal) scope is a special scope that only exists for nested functions.
#     If the local scope is an inner or nested function, then the enclosing scope is the scope of the outer or
#     enclosing function. This scope contains the names that you define in the enclosing function. The names in the
#     enclosing scope are visible from the code of the inner and enclosing functions.
# - Global
#     Global (or module) scope is the top-most scope in a Python program, script, or module.
#     This Python scope contains all of the names that you define at the top level of a program or a module.
#     Names in this Python scope are visible from everywhere in your code.
# - Built-in
#     Built-in scope is a special Python scope that’s created or loaded whenever you run a script or open an interactive
#     session. This scope contains names such as keywords, functions, exceptions, and other attributes that are built
#     into Python. Names in this Python scope are also available from everywhere in your code. It’s automatically
#     loaded by Python when you run a program or script.



def outer_func():
     # This block is the Local scope of outer_func()
     var = 100  # A nonlocal var
     # It's also the enclosing scope of inner_func()
     def inner_func():
         # This block is the Local scope of inner_func()
         print(f"Printing var from inner_func(): {var}")
     inner_func()
     print(f"Printing var from outer_func(): {var}")
outer_func()
# Printing var from inner_func(): 100
# Printing var from outer_func(): 100
inner_func()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'inner_func' is not defined

# When you call outer_func(), you’re also creating a local scope. The local scope of outer_func() is, at the same time,
# the enclosing scope of inner_func(). From inside inner_func(), this scope is neither the global scope nor the local scope.
# It’s a special scope that lies in between those two scopes and is known as the enclosing scope.
# Note that inner_func() is a temporary function that comes to life only during the execution of its
# enclosing function, outer_func(). Note that inner_func() is only visible to the code in outer_func().



# Modifying global names is generally considered bad programming practice because it can lead to code that is:
# - Difficult to debug: Almost any statement in the program can change the value of a global name.
# - Hard to understand: You need to be aware of all the statements that access and modify global names.
# - Impossible to reuse: The code is dependent on global names that are specific to a concrete program.
# - Good programming practice recommends using local names rather than global names.



# In contrast to global, you can’t use nonlocal to create lazy nonlocal names. Names must already exist
# in the enclosing Python scope if you want to use them as nonlocal names. This means that you can’t
# create nonlocal names by declaring them in a nonlocal statement in a nested function. Take a look
# at the following code example:
def func():
     def nested():
         nonlocal lazy_var  # Try to create a nonlocal lazy name
#   File "<stdin>", line 3
# SyntaxError: no binding for nonlocal 'lazy_var' found



# Discovering Unusual Python Scopes

# You’ll find some Python structures where name resolution seems not to fit into the LEGB rule for Python scopes.
# These structures include:
# - Comprehensions
# - Exception blocks
# - Classes and instances

# Comprehensions

[item for item in range(5)]
# [0, 1, 2, 3, 4]
item
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#     item
# NameError: name 'item' is not defined

# Once you run the list comprehension, the variable item is forgotten and you can’t access its value anymore.
# Note that this only applies to comprehensions. When it comes to regular for loops,
# the loop variable holds the last value processed by the loop:
for item in range(5):
     print(item)
item
# 4


# Exception Variables Scope

# The exception variable is a variable that holds a reference to the exception raised by a try statement.
# In Python 3.x, such variables are local to the except block and are forgotten when the block ends.
lst = [1, 2, 3]
try:
    lst[4]
except IndexError as err:
    # The variable err is local to this block
    # Here you can do anything with err
    print(err)
# list index out of range
err # Is out of scope
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#     err
# NameError: name 'err' is not defined

# To work around this behavior, you can define an auxiliary variable out of the try statement and
# then assign the exception to that variable inside the except block.
lst = [1, 2, 3]
ex = None
try:
    lst[4]
except IndexError as err:
    ex = err
    print(err)
# list index out of range
err  # Is out of scope
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'err' is not defined
ex  # Holds a reference to the exception
# list index out of range


# Od 'Class and Instance Attributes Scope' -> poxniej !!!