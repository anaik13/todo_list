# Syntax for using Assert in Pyhton:
# assert <condition>
# assert <condition>,<error message>
# In Python we can use assert statement in two ways as mentioned above.

# assert statement has a condition and if the condition is not satisfied the program will stop and give AssertionError.
# assert statement can also have a condition and a optional error message.
# If the condition is not satisfied assert stops the program and gives AssertionError along with the error message.

# assert statement is used to check types, values of argument and the output of the function.



# Example

x = "hello"

#if condition returns True, then nothing happens:
print('assert 1')
assert x == "hello"

#if condition returns False, AssertionError is raised:
print('assert 2')
assert x == "goodbye", "x should be 'hello'"
