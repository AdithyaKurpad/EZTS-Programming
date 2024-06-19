n=int(input("Enter the number of terms: "))
first=0
sec=1
if n==1:
    print(first)
else:
    print(first,end=" ")
    print(sec,end=" ")
    for i in range(2,n):
        first,sec=sec,first+sec
        print(sec,end=" ")