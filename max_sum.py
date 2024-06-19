l=[2,4,3,5,6,3,4,6,7,1,2,5]
i=0
k=int(input("Enter k value: "))
maxsum=0
maxarray=0
while i<len(l):
    if sum(l[i:i+k])>maxsum:
        maxsum=sum(l[i:i+k])
        maxarray=l[i:i+k]
    i=i+1
print(maxarray)