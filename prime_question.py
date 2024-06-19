'''def prime(k):
    m=k
    flag=0
    if m<1:
        flag=1
    elif m==1:
        flag=0
    else:
        for i in range(2,(m//2)+1):
            if m%i==0:
                flag=1
    if flag==0:
        return 1
    else:
        return 0
 
#Level 1   
n=int(input("Enter an integer: "))
r=[]
k=n+1
flag=0
while flag<1:
    flag=prime(k)
    if flag==1:
        r.append(k)
    else:
        k=k+1

#Level 2
sum=0
for i in range(n+1,k):
    sum=sum+i    
r.append(sum)
    
#level 3
p1 = k
k=p1+1
flag=0
while flag<1:
    flag=prime(k)
    if flag==1:
        p2=k
    else:
        k=k+1
p3 =p1*p2
bool_v=True if prime(p3)==1 else False
r.append(bool_v)
t = tuple(r)
print(t)'''