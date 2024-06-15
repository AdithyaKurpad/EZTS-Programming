#Lists
#Maximum count of voter, returns -1 if more than one voter has same votes 
'''l=[1,1,2,2,2,3,3,3,3,4,4,4,4,4,5,5,5,5,5]
d={}
c,c1,c2,c3,c4,c5=0,0,0,0,0,0
for i in range(len(l)):
    if l[i]==1:
        c=c+1
        d[l[i]]=c
    if l[i]==2:
        c1=c1+1
        d[l[i]]=c1
    if l[i]==3:
        c2=c2+1
        d[l[i]]=c2
    if l[i]==4:
        c3=c3+1
        d[l[i]]=c3
    if l[i]==5:
        c4=c4+1
        d[l[i]]=c4
    if l[i]==6:
        c5=c5+1
        d[l[i]]=c5
print(d)
l1=[]
ele=max(d.values())
for i in d:
    if d[i]==ele:
        l1.append(i)
print(l1)

if len(l1)>1:
    print(-1)
else:
    print(l1.pop())'''
    
#Files
'''import os
with open("MSD.txt","w") as f:
    f.write("Thala for a reason\n")
    f.write("Captain Cool\n")
    #f.close()
    
with open("MSD.txt","a") as f:
    f.write("5 IPL Trophies,3 ICC Trophies\n")
    
with open("MSD.txt","r") as f:
    r=f.read()
    print(r)
    r=r.replace("Captain Cool","Captain Legend")

with open("MSD.txt","a") as f:
    f.write(r)

with open("MSD.txt","r") as f:
    print(f.tell())
    #print(f.read().decode('utf-8'))
    
with open("MSD.txt","r+b") as f:
    print(f.tell())
    f.seek(-35,2)
    print(f.tell())
    f.write(b"#")
    print(f.read().decode('utf-8'))'''
    

    























    


    
    

    
    
