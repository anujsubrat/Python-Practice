'''wap to input a limit and display sum of factorial of each number start from 1 to such
limit
for eg
input
enter limit=5
output
s=1!+2!+3!+4!+5!'''
def fact(N):
    f=1
    for i in range(1,N+1):
        f=f*i
        return f
imit=int(input('enter '))
s=0
for j in range(1,limit+1):
    s=s+fact(j)
print("sum=",s)
