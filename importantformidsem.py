p=[]
i=int(input("type your number"))
for a in range(i):
    s=input()
    t=s.split()
    d={}
    d["rollno"]=int(t[0])
    d["name"]=t[1]
    d["marks"]=int(t[2])
    p.append(d)
print(p)
