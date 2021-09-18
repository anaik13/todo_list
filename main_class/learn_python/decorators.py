# https://www.programiz.com/python-programming/decorator

# 1) Decorators without passing parameters

def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner

@make_pretty
def ordinary():
    print("I am ordinary")
# is equivalent to
def ordinary():
    print("I am ordinary")
ordinary = make_pretty(ordinary)


# 2) Decorators with passing parameters

# a)
def smart_divide(func):
    def inner(a, b):
        print("I am going to divide", a, "and", b)
        if b == 0:
            print("Whoops! cannot divide")
            return

        return func(a, b)
    return inner

@smart_divide
def divide(a, b):
    print(a/b)

# b) create general decorators that work with any number of parameters
def works_for_all(func):
    def inner(*args, **kwargs):
        print("I can decorate any function")
        return func(*args, **kwargs)
    return inner


# 3) Chaining decorators
def star(func):
    def inner(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30)
    return inner

def percent(func):
    def inner(*args, **kwargs):
        print("%" * 30)
        func(*args, **kwargs)
        print("%" * 30)
    return inner

@star
@percent
def printer(msg):
    print(msg)
# is equivalent to
def printer(msg):
    print(msg)
printer = star(percent(printer))



