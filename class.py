class Student:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
a=input("Enter the name: ")
b=int(input("Enter the age: "))
c=input("Enter the gender: ")
print(type(a))
print(type(b))
print(type(c))
o=Student(a,b,c)
print(o.name,o.age,o.gender)