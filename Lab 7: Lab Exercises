#5.16
def indexes(string,letter):
	answer=[]
	for i in range(len(string)):
		if letter==string[i]:
			answer.append(i)
	return answer

#5.17
def doubles(z):
	for i in range(len(z)-1):
		if z[i+1]==z[i]*2:
			print(z[i+1])

#5.18
def four_letter(z):
	answer=[]
	for i in range(len(z)):
		if len(z[i])==4:
			answer.append(z[i])
	return answer
#5.19
def inBoth(a,b):
	for char in a:
		return char in b

#5.20
def intersect(a,b):
	answer=[]
	for i in range(len(a)):
		if a[i] in b:
			answer.append(a[i])
	return answer

#5.21
def pair(a,b,num):
	for i in range(len(a)):
		for char in b:
			if a[i]+char==num:
				print(a[i],char,sep=" ")
#5.22
def pairSum(a,num):
	for i in range(len(a)-1):
		for j in range(i+1,len(a)):
			if a[i]+a[j]==num:
				print(i,j)
#5.29
def lastfirst(a):
	firstname=[]
	lastname=[]
	answer=[firstname,lastname]
	for i in range(len(a)):
		firstname.append(a[i][a[i].find(",")+2:])
		lastname.append(a[i][:a[i].find(",")])
	return answer

#5.31
def subsetSum(a,num):
	for i in range(len(a)-2):
		for j in range(i+1, len(a)-1):
			for k in range(j+1, len(a)):
				if a[i] + a[j] + a[k] == num:
					return True
	return False

#5.33
def mystery(n):
	counter=0
	while n>1:
		counter+=1
		n=n//2
	return counter

#5.46
def inversions(z):
	counter=0
	for i in range(len(z)-1):
		if z[i]>z[i+1]:
			counter+=1
	return counter*2

#5.48
def sublist(a,b):
	newlist=[]
	for i in range(len(b)):
		if b[i] in a:
			newlist.append(b[i])
	return a==newlist
#5.37
def mssl(a):
    best = 0
    for i in range(len(a)):
        for j in range(i+1, len(a)+1):
            total = 0
            for k in range(i, j):
                total += a[k]
            if total > best:
                best = total
    return best
