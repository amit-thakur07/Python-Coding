# class Employee:
#     @staticmethod
#     def fun():
#         print("hello")
# s1=Employee()
# s1.fun()
# a functon inside the class and you do not need object or clas data

# 2
# class User:
#     @staticmethod
#     def is_valid_email(email):
#         return "@" in email and "." in email
# email=input("enter the mail: ")
# s1=User()
# print(s1.is_valid_email(email))

def fun(functi1):
    def wrapper():
        print("before")
        functi1()
        print("after")
    return wrapper
def new():
    print("hello")
s1=fun(new)
s1()




