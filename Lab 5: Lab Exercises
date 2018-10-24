#ex1
def ah(l,x,y):
	counter=0
	for i in range(len(l)):
		if x<l[i]<y:
			counter+=1
	for i in range(len(l)+1):
		if x<l[-i]:
			minnumber=l[-i]
		return(counter,minnumber)
#ex2part1
def is_perfect(n):
     current_sum = 0
     for divisor in range(1, n):
          if n % divisor == 0:
               current_sum = current_sum + divisor

     if n == current_sum:
          return True
     else:
          return False

print("Printing perfect numbers smaller than 10,000:")
for number in range(6,10001):
     if is_perfect(number):
          print(number)       

#ex2part2             
print("Printing perfect numbers smaller than 35,000,000:")
for number in range(6,35000000):
     if is_perfect(number):
          print(number)   
#ex3a
def arithmetic(l):
	diff = l[1] - l[0]
     for i in range(1, len(l)-1):
        if l[i+1] - l[i] != diff:
            return False
     return True

#ex3b
def is_sorted(l):
	for i in range(len(l)-1):
		checker=(l[i+1]>=l[i])
		if checker==False:
			return False
	return checker
