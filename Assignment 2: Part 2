# Name: Yousuf Ahmed
# Student number:  300022604
# Course: IT1 1120 
# Assignment Number 2 - Part 2

############
#Question 1
############
def min_enclosing_rectangle(radius,x,y):
        '''
        (number,number,number)->tuple

        Pre-condition(s): Radius, x, and y must be a number; type(radius)==int or float, type(x)==int or float, type(y)==int or float
        
        Returns the x and y coordinates of the bottom-left corner of the smallest axis-rectangle that contains
        a circle defined by "radius" and the "x" and "y" coordinates of its center.
        ''' 
        if radius>=0:
                return (x-radius, y-radius)

############
#Question 2
############
def series_sum():
        '''
        ()->number

        Pre-condition(s): None
        
        Returns the sum of 1000 + 1/(1**2) + 1/(2**2) + 1/(3**2) + 1/(4**2) +.....+1/(n**2) 
        '''
        x=0
        pos_int=int(input("Please enter a non-negative integer: "))
        if pos_int>=0:
                for i in range(1,pos_int+1):
                        x=x+1/i**2
                return(1000+x)

############
#Question 3
############
def pell(n):
        '''
        (int)->int

        Pre-condition(s): n must be a integer; type(n)==int

        Returns the nth Pell number based on the sequence: [n=0, pell(0)=0], [n=1, pell(1)=1], [n>1, 2*pell(n-1)+pell(n-2)]
        '''
        x=0
        if n==0 or n==1:
                return n
        if n>1:
                for i in range(n+1):
                        x=2*(pell(n-1))+pell(n-2)
                return x

############
#Question 4
############
def countMembers(s):
        '''
        (str)->int

        Pre-condition(s): s must be a string; type(s)==str

        Returns the number of extraordinary characters in s. A character is said to be extraordinary if it is: a lower
        case letter between e and j, or an upper case letter between F and X, or a numeral between 2 and 6, or an exclamation
        mark (!), or a comma (,), or a backslash (\)
        '''
        x=0
        for i in range(0,len(s)):
                if s[i] in "efghij" or s[i] in "FGHIJKLMNOPQRSTUXWX" or s[i] in "23456" or s[i] in "!,\\":
                        x+=1
        return x

############
#Question 5
############
def casual_number(s):
        '''
        (str)->int

        Pre-condition(s): s must be a string; type(s)==str

        Returns an integer representing a number in s
        '''
        x=0
        if s=="-":
                pass
        else:
                for i in range(len(s)):
                        if s<"0":
                                if s[i].isdigit()!=True:
                                        return None
                                if s[i].isdigit():
                                        x+=1
                                        if x==len(s):
                                                num_s=int(s.replace(",",""))
                                                return num_s
                        else:        
                                if s[i] in "-,0123456789":
                                        x+=1
                                        if x==len(s):
                                                num_s=int(s.replace(",",""))
                                                return num_s

############
#Question 6
############
def alienNumbers(s):
        '''
        (str)->int

        Pre-condition(s): s must be a string; type(s)==str

        Returns the integer value represented by each chracter in s by using the string method, s.count()
        '''
        return s.count("T")*1024+s.count("y")*598+s.count("!")*121+s.count("a")*42+s.count("N")*6+s.count("U")



############
#Question 7
############
def alienNumbersAgain(s):
        '''
        (str)->int

        Pre-condition(s): s must be a string; type(s)==str

        Returns the integer value represented by each chracter in s without using any string methods
        ''' 
        
        aliensum=0
        for i in range(len(s)):
                if s[i]=="T":
                        aliensum+=1024
                if s[i]=="y":
                        aliensum+=598
                if s[i]=="!":
                        aliensum+=121
                if s[i]=="a":
                        aliensum+=42
                if s[i]=="N":
                        aliensum+=6
                if s[i]=="U":
                        aliensum+=1
        return aliensum

############
#Question 8
############
def encrypt(s):
        '''
        (str)->str

        Pre-condition(s): s must be a string; type(s)==str

        Returns a reversed and character-alternated copy of the string, s 
        '''
        newS=""
        rev=s[::-1]
        for i in range(len(s)):
                newS=newS+rev[i]+rev[-1-i]
                if len(newS)==len(s):
                        return newS
                if rev[i]==rev[-1-i]:
                        newS=newS.replace(newS[-1],"")
                        newerS=newS+rev[i]
                        return newerS

############
#Question 9
############
def oPify(s):
        '''
        (str)->str

        Pre-condition(s): s must be a string; type(s)==str

        Returns a string with the letters o and p inserted between every pair of consecutive characters of s, as follows.
        If the ﬁrst character in the pair is uppercase, it inserts an uppercase O.
        If however, it is lowercase, it inserts the lowercase o. If the second character is uppercase, it inserts an uppercase P.
        If however, it is lowercase, it inserts the lowercase p.
        If at least one of the character is not a letter in the alphabet, it does not insert anything between that pair.
        Finally, if s has one or less characters, the function returns the same string as s.
        '''
        newS=""
        newerS=""
        if len(s)==1:
                return s
        for i in range(len(s)-1):
                        if s[i].isalpha() and s[i+1].isalpha():
                                if s[i].isupper() and s[i+1].isupper():
                                        newS=newS+s[i]+"OP"
                                        newerS=newS+s[-1]
                                if s[i].isupper() and not s[i+1].isupper():
                                        newS=newS+s[i]+"Op"
                                        newerS=newS+s[-1]
                                if not s[i].isupper() and s[i+1].isupper():
                                        newS=newS+s[i]+"oP"
                                        newerS=newS+s[-1]
                                if not s[i].isupper() and not s[i+1].isupper():
                                        newS=newS+s[i]+"op"
                                        newerS=newS+s[-1]
                        if s[i].isalpha() and s[i+1].isalpha()==False:
                                newS=newS+s[i:len(s)]
                                newerS=newS
                        if s.isdigit():
                                return s
			
        return newerS

############
#Question 10
############
def nonrepetitive(s):
        '''
        (str)->bool

        Pre-condition(s): s must be a string; type(s)==str

        Returns True if s is nonrepetitive and False otherwise. A word is said to be nonrepetitive if it word does not contain any subword twice in a row
        '''

        
        for i in range(1,len(s)//2+1):
                for ch in range(len(s)):
                        if ch+2*i <= len(s):
                                if s[ch:ch+i]==s[ch+i:ch+2*i]:
                                        return False
        return True
