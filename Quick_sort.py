def divide(l,low,high):
    p=l[high]
    pivot=high
    j=-1
    for i in range(0,high):
        if l[i]<=p:
            j=j+1
            l[i],l[j]=l[j],l[i]
    j=j+1
    l[j],l[pivot]=l[pivot],l[j]
    pivot=j   
    return pivot

def Quick_sort(l,low,high):
    if low<high:
        pivot=divide(l,low,high)
        Quick_sort(l,low,pivot-1)
        Quick_sort(l,pivot+1,high)
    return

if __name__=="__main__":
    l=list(map(int,input().split()))
    Quick_sort(l,0,len(l)-1)
    print("Sorted array=",l)