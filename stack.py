class Stack:
    def __init__(self):
        self.items=[]
    def push(self,data):
        return self.items.append(data)
    def pop(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
    def print(self):
        print(self.items)
s=Stack()
n=int(input("Enter the number of elements: "))
for i in range(n):
    x=int(input("Enter the element: "))
    s.push(x)
s.print()