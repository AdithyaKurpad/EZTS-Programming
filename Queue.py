class Queue:
    def __init__(self):
        self.l=[]
    def push(self,data):
        return self.l.append(data)
    def pop(self):
        return self.l.pop(0)
    def size(self):
        return len(self.l)
    def top(self):
        return self.l[0]
    def print(self):
        print(self.l)
    def rev(self):
        return self.l[::-1]
q=Queue()
q.push(1)
q.push(2)
q.push(3)
q.print()
print(q.size())
print(q.top())
q.pop()
q.print()
print(q.size())
print(q.top())
print(q.rev())