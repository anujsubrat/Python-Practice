s=open("anuj.txt","r")

data=s.read()
p=data.split()
print(len(p[2]))
s.close()
