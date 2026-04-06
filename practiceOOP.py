# class TwoDvector:
#     def __init__(self, i, j):
#         print(f"2d vector = {i}i + {j}j")

# class ThreeDvector(TwoDvector):
#     def __init__(self, i, j, k):        
#         super().__init__(i, j)           
#         print(f"3d vector = {i}i + {j}j + {k}k")

# s1 = ThreeDvector(12, 23, 56)        


# class Animals:
#     def __init__(self,class_animals):
#        print(f"this is the class {class_animals}")

# class Pets(Animals):
#     def __init__(self,class_pets,class_animals):
#        super().__init__(class_animals)
#        print(f"this is the class pets {class_pets}")


# class Dog(Pets):
#   def __init__(self):
#     super().__init__("pet class","animal class")
#   def bark(self):
#      print("dog barks")

# s1=Dog()
# s1.bark()



# q3 complex number sum and multiply 
# class Complex:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def __add__(self,other):
#         return complex(self.a+ other.a,self.b+other.b)
    
# s1=Complex(12)
# s2=complex(23)
# print(s1+s2)        
    

