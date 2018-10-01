#Question 1
def pay(wage,hours):
	if hours<=40:
		return wage*hours
	if 40<hours<=60:
		return (wage*40)+(hours-40)*1.5*wage
	else:
		return (wage*40)+(1.5*wage*20)+(hours-60)*2*wage

#Question 2
def rps(p1,p2):
	if (p1=="R" and p2=="S") or (p1=="S" and p2=="P") or (p1=="P" and p2=="R"):
		return -1
	if p1==p2:
		return 0
	else:
		return 1
#Question 3a
def is_divisible(n,m):
        
    return n%m==0

first=int(input("Enter 1st integer: "))
second=int(input("Enter 2nd integer: "))

if(is_divisible(first,second)):
    print(first,"is divisible by",second)
else:
    print(first,"is not divisible by",second)



#Question 3b
def is_divisible(n,m):
    return n%m==0

def is_divisible23n8(n):
    if (is_divisible(n,2) or is_divisible(n,3)) and not is_divisible(n,8):
        return ("yes")
    else:
        return ("no")
    
x=int(input("Enter an integer: "))

if (is_divisible23n8(x)=="yes"):
    print(x,"is divisible by 2 or 3 but not 8")
else:
    print ("It is not true that", x, "is divisible by 2 or 3 but not 8")




