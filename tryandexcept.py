try:
    a=int(input("type a new number"))
    b=int(input("type another number"))
    C=a/b
except(ZeroDivisionError):
    print("yes it is error of zero division")
else:
    print("no error")
finally:
    print("nothing to type")
