class A:
    def __init__(self,usn):
        self.usn=usn
    def details(self):
        self.name=input("Enter the name: ")
        #self.usn=input("Enter the usn: ")
        self.m1=int(input("Enter the m1: "))
        self.m2=int(input("Enter the m2: "))
        self.m3=int(input("Enter the m3: "))
        self.m4=int(input("Enter the m4: "))
        self.m5=int(input("Enter the m5: "))
    def per(self):
        self.details()
        print("Name:",self.name,"USN:",self.usn,"Marks:",self.m1,self.m2,self.m3,self.m4,self.m5)
        per=((self.m1+self.m2+self.m3+self.m4+self.m5)/500)*100
        print("Percentage is",per)
        if per>=90:
            print("Grade A+")
        elif 90>per>=80:
            print("Grade A")
        elif 80>per>=70:
            print("Grade B+")
        elif per<70:
            print("Grade B")
n=int(input("Enter the number of students: "))
for i in range(n):
    s=input(f"Enter the USN of student {i+1}: ")
    c=A(s)
    c.per()
