class A:
    def __init__(self,a,b,c):
        self.A=a
        self.__B=b
    def fun(self):
        print(self.A)
        print(self.__B)
o=A(1,2,3)
o.fun()