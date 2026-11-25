import time #adding delay function
x=print #replacing print with x

#if else statement

'''
conditional operatore
>,<,>=,<=,==,!=

'''

a=int(input('enter your age\n'))
x('your age is',a)
if(a>18):
    x('yes you can drive')
else:
        x("no you can't drive")

apple_price=input("put apples price\n")
budget=input("put your budget\n")
if(apple_price<=budget):
    x("Alexa,add 1kg Apples to the cart")
else:
    x('Alexa,do not add Apples to the cart')

time.sleep(2)
exit()
