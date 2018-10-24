#ex1

def is_eligible(age,citizenship,prison):
    return (age>=18) and citizenship==("Canadian" or "Canada" or " Canada" or "canadian") and prison==("No" or "no")

name=input("What is your name? ")
userage=int(input("How old are you? "))
usercitizenship=input("What is your status of citizenship? ")
userprison=input("Are you currently in prison for any convincted criminal offences? ")

if is_eligible(userage,usercitizenship,userprison):
    print("Thank you", name, "you are", userage, "and Canadian and not in prison thus you are eligible to vote.")
else:
    print("Unfortunately", name, "you are uneligible to vote")

#ex2

def mess(phrase):
    '''(str)->str'''
    x=0
    phrase=phrase.replace(" ","-")
    for i in range(0,len(phrase)-1):
        x+=1
        if phrase[x]=="r" or "s" or "t" or "v" or "w" or "x" or "y" or "z":
            phrase=phrase.replace("r","R")
            phrase=phrase.replace("s","S")
            phrase=phrase.replace("t","T")
            phrase=phrase.replace("v","V")
            phrase=phrase.replace("w","W")
            phrase=phrase.replace("x","X")
            phrase=phrase.replace("y","Y")
            phrase=phrase.replace("z","Z")
    return phrase

#ex3

def is_divisible(n,m):
     '''(int, int)->bool
     returns True if n is divisible by n, and False otherwise.'''
     return n%m==0

def is_divisible23n8(n):
     '''(int)->bool
     returns string "yes" if n is divisible by 2 or 3 but not 8, and "no" otherwise.'''
     if ( (is_divisible(n,2) or is_divisible(n,3)) and not(is_divisible(n,8))):
          return True
     else:
          return False

def print_all_23n8(num):
     '''
     num>=0
     '''
     x=0
     for i in range(num):
          x+=1
          if is_divisible23n8(x):
               print(x)
          
          
usernum=int(input("Give me a number: "))
print_all_23n8(usernum)

#ex4

userint=int(input("Give me a number: "))

#halfpyramid
x=0
for i in range(userint):
    x+=1
    print("$"*x)
print()

#fullpyramid
x=0
for i in range(userint):
    x+=1
    print(" "*(userint-x)+"#"*(x*2-1)+" "*(userint-x))

#ex5
userint=int(input("Give me a positive integer: "))

x=0
for i in range(userint):
    x+=1
    if userint%x==0:
        print(x,end=" ")

print()

def prime(num):
    x=0
    divisorcounter=0
    if num>2:
        for i in range(num):
            x+=1
            if num%x==0:
                divisorcounter+=1
        return divisorcounter==2

if prime(userint):
    print(userint, "is a prime number")
else:
    print(userint, "is not a prime number")
                
def smallerprimes(num):
    x=0
    primecounter=0
    print(2)
    for i in range(num-1):
        x+=1
        if prime(x):
            primecounter+=1
            print(x)
