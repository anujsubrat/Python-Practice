import time
a=int(input("put your time\n"))
x=print
if(6<a<12):
    x('good morning')
elif(a==12):
    x('good noon')
elif(12<a<17):
    x('good afternoon')
elif(17>a<2044E):
    x("goog evening")
else:
    x('good night')
time.sleep(3)
exit()
