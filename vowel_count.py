def cont_vowel(s):
    dict={'A':0,'E':0,'I':0,'0':0,'u':0}
    for i in s:
        if i=='a' or i=='A':
            dict['A']+=1
        elif i=='e' or i=='E':
            dict['E']+=1
        elif i=='i' or i=='I':
            dict['I']+=1
        elif i=='o' or i=='O':
            dict['O']+=1
        elif i=='u' or i=='U':
            dict['U']+=1
    x=max(dict.values())
    result=[]
    for i,j in dict.items():
        if j==x:
            result.append(i)
    return result
n=[
    ['alex','hi mahi'],
    ['sam', 'a lovely is the sum'],
    ['jamie','reading a book is my favorite'],
    ['taylor','i love video games']

]
m={}
for i in n:
    m[i[0]]=cont_vowel(i[1])
print(m)