#urlify-%20

st="my name is megha"
# string is immutable therefore 
li=list(st)
print(li)
for i in range(len(li)):
    if li[i]==' ':
        li[i]='%20'
print(li)
st=' '.join(map(str,li))#using map fn to convert to string
print(st)