#1
a=0
for i in range(1,10+1,1):
    a=a+6**i
print(a)

#2
#inputString = input('введите 5 символов - abcd и цифру')
#index = inputString.index("5")
#print('The index of number:', index)
#for i in inputString:
#    for i,index in enumerate(inputString)
#print(i)



k=0
inputStr = input("ведите 5 символов - abcd и цифру:")
for i in inputStr:
    for j in range(0,10):
        if i==str(j):
            print("число", i, "находится на", k, "месте")
    k+=1





#3
import random
x=random.random() #random, randint, randrange
print(x)
y=3*x+2
print(y)
L = list(range(1))
L.append(x)
print(L)

#print(a)
#b=random.randint(2,100)
#print(b)
#c=a*b
#if c>=2 and c<=5:
#    print(c)
#else:
#    print("saaad")


#OR
#from random import randrange
#print("Vivod", randrange(0,2,step))


#5
#a=0
#for i in range (2,100,1):
#    a=a+((-1)**i)*(i-2)

