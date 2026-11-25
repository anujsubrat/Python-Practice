'''f=open("student.txt", "w")
s="my name is this and this is not this and if this is thisare"
f.write(s)
print(s)
f.close()'''
 
d=open("student.txt","r")
data=d.read()
a1=data.split()
print(a1)
S=""
for i in a1:
    if (i == "this"):
        q=i.replace("this","that")
        S+=q+" "
    else:
        S+=i+" "
print(S)
d.close()
