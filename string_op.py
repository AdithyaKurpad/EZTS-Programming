#Take the input as string with 2 operands and 1 operator and evaluate that string
s=input()
op=['+','-','*','/']
for i in s:
    if i in op:
        x=i
        break
n=s.split(x)
print(n)
n1=float(n[0])
n2=float(n[1])
match x:
    case '+':
        print("Addition:",n1+n2)
    case '-':
        print("Subtraction:",n1-n2)
    case '*':
        print("Multiplication:",n1*n2)
    case '/':
        if n2!=0:
            print("Division:",n1/n2)
        else:
            print("Division by zero error")
    case _:
        print("Default")