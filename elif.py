import time
x=print
num=int(input('enter the value of num\n'))
if(num<0):
        x("number is negative")

elif(num==0):
    x('number is zer\'o')
elif(num==330):
    x('number is special')
else:
    x("number is positive")

time.sleep(2)
exit()
