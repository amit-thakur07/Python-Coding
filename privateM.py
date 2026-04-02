# # access a private attribute inside a class body by using another function
# class A:
#     def __init__(self):
#         self.__name="amit"
# obj=A()
# print(obj._A__name)

# method 2'
# class A:
#     def __init__(self):
#         self.__name="amit"
#     def show(self):
#         return self.__name
# obj=A()
# print(obj.show())


# class Student:
#  def methdo(self,length,width):
#         Area=length*width
#         return(Area)
# length=float(input("enter a number: "))
# width=float(input("enter a number: "))
# s1=Student()
# print(s1.methdo(length,width))


