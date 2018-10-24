#ex1
def sum_odd_while_v2(n):
     '''(int)->int
        Returns the sum of all odd integers between 5 and n
        '''
     x=0
     i=3
     while i<len(range(n))-1:
         i+=2
         x=x+i
     return x

#ex2
num1=int(input("Give me an integer: "))
num2=int(input("Give me another integer: "))
print(num1+num2)


flag=True
while flag:
    response=input("Would you like to continue adding numbers? ")
    if response=="yes":
        num1=int(input("Give me an integer: "))
        num2=int(input("Give me another integer: "))
        print(num1+num2)
    else:
        flag=False

#ex3
def first_neg(userlist):
	i=-1
	while i<len(userlist)-1:
		i+=1
		if userlist[i]<0:
			return i

#ex4
def sum_5_consecutive(userlist):
	for i in range(len(userlist)-4):
		if userlist[i]+userlist[i+1]+userlist[i+2]+userlist[i+3]+userlist[i+4]==0:
			return True
	return False

def sum_5_consecutive_v2(userlist):
	i=-1
	while i+1<(len(userlist)-4):
		i+=1
		if userlist[i]+userlist[i+1]+userlist[i+2]+userlist[i+3]+userlist[i+4]==0:
			return True
	return False

#ex5
n=int(input("Enter a positive even integer for the size of the list? "))

#1a
a=[0]*n
print(a)

#1b
i=0
a=[]
while i<n:
    i+=1
    a=a+[0]
print(a)

#2a
import random
b=[]
while len(b)<n:
    b=b+[random.randint(1,100)]
print(b)

#2b
b=random.sample(range(1, 100), n)
print(b)

#3
c=b

#4a
i=-1
while i<n//2-1:
    i+=1
    c[i]=0
print(c)

#4b
c=[0]*(n//2)+c[n//2:n]
print(c)

#5
d=[b]
print(id(b))
print(id(d))

#6
e=b[1::2]
print(e)

#ex6
def fib(n):
	a=[1,1]
	for i in range(2,n):
		a.append(a[i-1]+a[i-2])
	return a

#ex7
def inner_product(a,b):
    innersum=0
    for i in range(len(a)):
        innersum=innersum+a[i]*b[i]
    return innersum


    

