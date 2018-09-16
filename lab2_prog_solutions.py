#ex1
def repeater(s1,s2,n):
    return ("_"+(s1+s2)*n+"_")

#ex2
def roots(a,b,c):
    x1=(-b+math.sqrt(b**2-4*a*c))/(2*a)
    x2=(-b-math.sqrt(b**2-4*a*c))/(2*a)
    print ("The quadratic equation with coefficients a =", a, "b =", b, "c =", c, "has the following solutions (i.e. roots):", x1, "and", x2)

#ex3
def real_roots(a,b,c):
    x=b**2-4*a*c
    return x>=0

#ex4
def reverse(x):
    return(x%10)*10+(x//10)
