class Stack:
    def __init__(self):
        self.l=[]
    def push(self,data):
        return self.l.append(data)
    def pop(self):
        return self.l.pop()
    def size(self):
        return len(self.l)
    def top(self):
        return self.l[0]
e=input()
s=Stack()
ob="[{("
cb=")}]"
flag=0
for i in e:
    if i in ob:
        s.push(i)
    if i in cb:
        x=s.pop()
        if x=='(' and i==')':
            pass
        elif x=='[' and i==']':
            pass
        elif x=='{' and i=='}':
            pass
        else: 
            flag=1
            break
if flag==0 and s.size()==0:
    print("Valid")
else:
    print("Invalid")