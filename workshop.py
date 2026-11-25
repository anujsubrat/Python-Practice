import time
import docx
x=print
budget=int(input("put your budget here \n"))
time.sleep(2)
kkr=100
csk=200
x('count till 10')
for i in range(10):
    time.sleep(1)
    print(i+1,end=' ')

time.sleep(2)
if(budget>=100):
    print("you can watch kkr")
elif(budget>=200):
    print('you can watch csk')
else:
    x('go home')

time.sleep(2)
x("hello world")
time.sleep(2)
exit()
