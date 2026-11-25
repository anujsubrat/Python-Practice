def abc():
    s="this is this and thisare"
    a=s.split()
    print(a)
    p=[]
    for i in a:
        if i=="this":
            i=i.replace("this","that")
            print(i)
            p.append(i)
        else:
            print(i)
            p.append(i)
    print(" ".join(p))
            
    
    

abc()
