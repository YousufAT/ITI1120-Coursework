# Name: Yousuf Ahmed
# Student number:  300022604
# Course: IT1 1120 
# Assignment Number 2 - Part 1

############
#Core Function
############
def split_tester(N,d):
    '''
    (str,str)->bool

    Pre-condition(s): N and d must be strings; type(N)==str, type(d)==str

    Returns True if  N can be split into pieces with d digits such that the resulting sequence is strictly increasing
    '''
    m=""
    d=int(d)
    if d==len(N):
        print(N)
        return True
    if len(N)%d!=0:
        return False
    if len(N)//d==2:
        m=m+N[0:d]+", "+N[d:len(N)]
        print(m)
        return N[0:d]<N[d:len(N)]
    else:
        for i in range(0,len(N),d):
            m=m+N[i:i+d]+", "
        print(m[:-2])
        for i in range(0,len(N)-d,d):
            if N[i:i+d]==N[i+d:(i+d)+d]:
                return False
            else:
                x=N[i:i+d]<N[i+d:(i+d)+d]
                if x==False:
                    return False
        return True


############
#Main Program
############
print("*"*46)
print("*"+" "*44+"*")
print("* __Welcome to my increasing-splits tester__ *")
print("*"+" "*44+"*")
print("*"*46)

name=input("What is your name? ")

print("*"*(49+len(name)))
print("*"+" "*(47+len(name))+"*")
print("* __"+name+", welcome to my increasing-splits tester.__ *")
print("*"+" "*(47+len(name))+"*")
print("*"*(49+len(name)))

flag=True
while flag:
        question=input(name+", would you like to test if a number admits an increasing-split of give size? ")
        question=(question.strip()).lower()
        if question==("no" or "NO" or "No"):
                print("*"*(18+len(name)))
                print("*"+" "*(16+len(name))+"*")
                print("* __"+"Good bye "+name+"!__ *")
                print("*"+" "*(16+len(name))+"*")
                print("*"*(18+len(name)))
                flag=False
        elif question==("yes" or "YES" or "Yes"):
                print("Good choice!")
                userinput=input("Enter a positive integer: ")
                if userinput.isalpha():
                    print("The input can only contain digits. Try again.")
                if "." in userinput:
                    print("The input can only contain digits. Try again.")
                if userinput<="0":
                    print("The input has to be a positive integer. Try again.")
                if userinput.isdecimal() and userinput!="0":
                    split=input("Input the split. The split has to divide the length of "+userinput+" i.e. "+str(len(userinput))+" ")
                    if split<="0":
                        print("The input has to be a positive integer. Try again.")
                    if split.isalpha() or "." in split:
                        print("The input can only contain digits. Try again.")
                    if split.isdigit() and len(userinput)%int(split)!=0:
                        print(split+" does not divide "+str(len(userinput))+". Try again" )
                    if split.isdigit() and len(userinput)%int(split)==0:
                        if split_tester(userinput,split)==True:
                                print("The sequence is increasing")
                        else:
                                print("The sequence is not increasing")
        else:
            print("Please enter yes or no. Try again.")

                                
        
        
                
        
        
                              
        
        

        
