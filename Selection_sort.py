n=int(input("Enter the number of elements: "))
l=[]
for i in range(n):
    ele=int(input("Enter the element: "))
    l.append(ele)
for j in range(n):
    pos=j
    min=l[j]
    for i in range(j,n):
        if l[i]<min:
            min=l[i]
            pos=i
    l[j],l[pos]=l[pos],l[j]
print(l)