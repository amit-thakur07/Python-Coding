# class student:
#     def display(self):
#         print(f"name: {self.name}, age={self.age}")
# s1=student()
# s1.name="alice"
# s1.age=12
# s1.display()

# class emp_id:
#     def display(self):
#         name=input("enter name:")
#         id=int(input("enter id: "))
#         salary=int(input("enter salary: "))
#         print(f"name is {name}, id is {id}, salary is {salary}")
# s1=emp_id()
# s1.display()


#que:  Create a Student class with:
# name
# roll_no
# marks
# Method:
# display() → prints student details

#ans
#  class Student:
#     def Stu(self,name,roll_no,marks):
#      print(f"the name is{name},roll_no is {roll_no},marks are{marks}")
# name=input("enter the name of student: ")
# roll_no=int(input("enter the roll no: "))
# marks=float(input("enter the total marks: "))
# s1=Student()
# s1.Stu(name,roll_no,marks)

# Create a Rectangle class with:
# length
# width
# Methods:
# area() → returns area

# class rectange:
#     def rect(self):
#         self.length=float(input("enter the lenght : "))
#         self.width=float(input("enter the width: "))
#         self.area=self.length*self.width
#         return self.area
# s1=rectange()
# x =s1.rect()
# print(x)

# Create a Mobile class with:
# brand
# price
# Method:
# apply_discount(percent) → reduces price based on discount

# use of staticmethod instead of using self:
# class mobile():
#     @staticmethod
#     def mob(brand,mobile_name,price):
#         return(f"brand name is {brand},mobile name is :{mobile_name},price is : {price}")
# brand=input("enter brand name: ")
# mobile_name=input("enter mobile name: ")
# price=int(input("enter price details: "))
# s1=mobile()
# print(s1.mob(brand,mobile_name,price))


# class P:
#     company="microsoft"
#     def __init__(self,name,salary,pin):
#         self.name=name
#         self.salary=salary
#         self.pin=pin
# p=P("hary",12000,23400)
# print(p.company,p.name,p.pin,p.salary)
