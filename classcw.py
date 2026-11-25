'''WAP to input a sting and count and display it after replacing word "this" with
"that. I/P: this is my class thisare and this is.
O/P: that is my class thisare and that is.'''

a=input("enter a sentence")
l=a.split()
t=""
for i in l:
    if(i=="this"):
        t=t+"that "
    else:
            t=t+i+" "

print(t)
