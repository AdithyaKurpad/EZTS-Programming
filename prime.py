m=int(input("Enter the message: "))
flag=1
if m<1:
    flag=1
elif m==1:
    flag=0
else:
    for i in range(2,(m//2)+1): #Iterating till half of m to make it efficient
        if m%i==0:
            flag=1
if flag==0:
    print("Valid message")
else:
    print("Invalid message")