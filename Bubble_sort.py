n=int(input("Enter number of elements: "))
l=[]
for i in range(n):
    ele=int(input("Enter the element: "))
    l.append(ele)
for j in range(n):
    for i in range(0,n-1-j):
        if l[i]>l[i+1]:
            l[i],l[i+1]=l[i+1],l[i]
print(l)