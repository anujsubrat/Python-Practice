def factorial(n):
    if(n==0 or n==1):
        print("1")
        return 1
    
b=n* factorial(n-1)
    print(b)
return b

factorial(5)
