l=[2,4,3,5,6,3,4,6,7,1,2,5]
k=int(input("Enter k value: "))
maxsum=sum(l[:k])
maxarray=l[:k]
currsum=maxsum
for i in range(1,len(l)-k+1):
    currsum=currsum-l[i-1]+l[i+k-1]
    if currsum>maxsum:
        maxsum=currsum
        maxarray=l[i:i+k]
print(maxsum)
print(maxarray)