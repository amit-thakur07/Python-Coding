#eg.1.
#  class car:
#     def start(self):
#         return(f"car starts")
# class car1(car):
#     def stop(self):
#         return(f"car stops")
# s1=car1()
# print(s1.start())
# print(s1.stop())

# FUNCTIONS PRACTICE
# def fun(n):
#     return n*n
# print(fun(2))

# 2.
# def fun(a):
#     return a**2
# a= int(input("enter a number: "))
# print(fun(a))

# 3
# i=input("enter a namw: ")
# def fun(i):
#     print(f"Hello {i}")
# fun(i)

# 4.
# def largest(a,b):

#     if a>b:
#         print("a is greater and the value is: ")
#         return a
#     elif a==b:
#         print("values are equal")
#     else:
#         print("b is greater and the value is : ")
#         return b
# a=int(input("enter first number: "))
# b=int(input("enter second number: "))
# print(largest(a,b))

# 5
# def even_odd(a):
#     return "even" if a%2==0 else "odd"
# try:
#     a=int(input("enter number: "))
#     print(f"number is {even_odd(a)}")
# except ValueError:
#     print("invalid input! please enter an interger")

# 6

# def fun():
#  st="my name is"
#  count=0
#  for i in st:
    
#      count=count+1
#  print(count)
# fun()

# 7 REVERSING A STRING WITHOUT USING SLICING
# st="amit"
# rev=""
# for ch in st:
#     rev=ch+rev
# print(rev)


