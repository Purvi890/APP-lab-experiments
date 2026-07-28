#decorators
def decorator(func):
    def wrapper():
        print('before func')
        func()
        print("after func")
    return wrapper
@decorator
def hello():
    print('hello')
hello()
# *args **kwargs collects named arguments
def add(*args):
    summ=0
    for i in args:
        summ+=i
    print(summ)
add(1,2,3,4,5,6)
# decorators with arguments
def decorator2(func):
    def wrapper(*args,**kwargs):
        print("bf")
        func(*args,**kwargs)
        print("af")
    return wrapper
@decorator2
def add(a,b):
    print(a+b)
@decorator2
def display(name='Purvi',age="19"):
    print(name,age)
add(1,2)
display()
#class decorators __call__
class class_dec:
    def __init__(self,name):
        self.name=name
    def __call__(self):
        print("bf")
        self.name()
        print("af")
@class_dec
def hello2():
    print("hello")
hello2()
       
#class methods
class demo:
    total=0

    @classmethod
    def add(cls,var):
        cls.total+=var
        return cls.total
d=demo()
print(d.add(4))
#magic methods, __init__, _str_,_add_,_repr_,_call_
