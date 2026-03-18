# def decorator(func):
#     def wrapper():
#      c=float(input("enter the number: "))
#      result=func()
#      return result+c
#     return wrapper

# @decorator
# def addition():
#     num1=float(input("enter number:"))
#     num2=float(input("enter number:"))
#     return num1+num2
    
# print(addition())


# print name in capital letters
# def decorator1(func):
#     def inner():
#         return func().upper()
#     return inner
    
# @decorator1
# def name():
#     name=input("enter your name: ")
#     surname=input("enter your surname: ")
#     return name+" "+surname
# print(name())




# def greet(gr):
#     def inner():
#      print("good morning")
#      gr()
#     return inner

# @greet
# def fun():
#     print("hi how are you")
# @greet
# def fun2():
#     print("hello what's up!")
# fun()
# fun2()

# question1
# def repeat(n):
#     def decorator(function):
#         def wrapepr():
#             for i in range(n):
#                 function()
#         return wrapepr
#     return decorator
# @repeat(3)
# def greet() :
#     print("helllo")
# greet()      

def decor(function):
    def wrapper(a,b):
        print("good morning")
        function(a,b)
    return wrapper
@decor  
def hello():
    print("hello world")
@decor
def add(a,b):
    print(a+b)

hello()
add(12,12)


