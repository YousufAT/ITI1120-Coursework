#Family name: Yousuf Ahmed
# Student number:  300022604
# Course: IT1 1120 
# Assignment Number 1

import turtle
import math

########################
# Question 1
########################

def pythagorean_pair(a,b):
     '''

     (int,int)->bool

     Returns True if a and b are a pythagorean pair (if there exists such an integer c that type(math.sqrt(a**2+b**2))==int) and returns false if they are not.

     '''
     return math.sqrt(a**2+b**2)==int(math.sqrt(a**2+b**2))
     

#######################
# Question 2
#######################

def mh2kh(s):
     '''

     (number)->number

     Returns "s" miles to kilometres
     
     '''
     return s*1.60934
     
#######################
# Question 3
#######################

def in_out(xs,ys,side):
     '''

     (number,number,number)->None

     side>=0
     
     Print True if the user's query points (inputs) are in the square defined by xs,ys,side (user's arguments)
     and if otherwise, prints False.
     
     '''
     xq=float(input("Enter a number for the x coordinate of a query point: "))
     yq=float(input("Enter a number for the y coordinate of a query point: "))
     print((xs-side)<xq<(xs+side) and (ys-side)<yq<(ys+side))

#######################
# Question 4
#######################
     

def safe(n):
     '''

     (int)->bool
     
     0<=n<=99
     
     Returns True if n does not contain 9 as its first or second digit
     or is not divisble by 9 and returns false otherwise.
     
     '''
     return n%9!=0 and n//10!=9 and n%10!=9

#######################
# Question 5
#######################

def quote_maker(quote,name,year):
     '''

     (str,str,int)->str

     Returns the arguments in a string saying: In (year), a person called (name) said: (“quote").
     
     '''
     return ('In'+" "+str(year)+", a person called"+" "+name+" "+'said: \"'+quote+'\"')

#######################
# Question 6
#######################

def quote_displayer():
     '''

     ()->None

     Prints a string by calling upon quote_maker and
     using the user's input as arguments.
     
     '''
     quote=input("Give me a quote: ")
     name=input("Who said that? ")
     year=input("What year did she/he say that? ")
     display=quote_maker(quote,name,year)
     print(display)


#######################
# Question 7
#######################

def rps_winner():
     '''

     ()->None

     Converts the user's input a to a rock-paper-scissors simulation and prints the result of the game.
     
     '''
     p1=input('''What choice did player 1 make?
Type one of the following options: rock, paper, scissors: ''')
     p2=input('''What choice did player 2 make?
Type one of the following options: rock, paper, scissors: ''')
     p1wins=(p1=="rock" and p2=="scissors") or (p1=="scissors" and p2=="paper") or (p1=="paper" and p2=="rock")
     p2wins=(p2=="rock" and p1=="scissors") or (p2=="scissors" and p1=="paper") or (p2=="paper" and p1=="rock")
     tiegame=(p1!=p2)
     print("Player 1 wins. That is", p1wins)
     print("It is a tie. That is not", tiegame)

#######################
# Question 8
#######################

def fun(x):
     '''

     (number)->number
     
     x>=0

     Returns the value for y in the equation: 10**(4*y)==x+3.
     
     '''
     return (math.log(x+3,10))/4

#######################
# Question 9
#######################

def ascii_name_plaque(name):
     '''

     (str)->None

     Prints a plaque containing "name".
     
     '''
     print ("*"*(len(name)+8))
     print ("*"+" "*(len(name)+6)+"*")
     print ("*"+" __"+name+"__ "+"*")
     print ("*"+" "*(len(name)+6)+"*")
     print ("*"*(len(name)+8))

#######################
# Question 10
#######################

def draw_car():
     '''
     This is a functio that draws a car using the turtle tool. 
     It contains no paramaters.
     
     '''
     import turtle
     t=turtle.Turtle()
     s=turtle.Screen()
     #carframe
     t.pencolor("black")
     t.pensize(3)
     t.goto(150,0)
     t.penup()
     t.goto(188,-30)
     t.pendown()
     #rightwheel
     t.fillcolor("black")
     t.begin_fill()
     t.circle(40)
     t.penup()
     t.goto(189,-15)
     t.pendown()
     t.end_fill()
     t.fillcolor("grey")
     t.begin_fill()
     t.circle(25)
     t.left(90)
     t.forward(25)
     t.right(30)
     t.forward(25)
     t.forward(-25)
     t.right(70)
     t.forward(25)
     t.forward(-25)
     t.left(150)
     t.forward(25)
     t.forward(-25)
     t.left(60)
     t.forward(25)
     t.end_fill()
     #carframe
    
     
     t.right(200)
     t.penup()
     t.forward(60)
     t.pendown()
     
     t.forward(35)
     t.left(90)
     t.forward(35)
     t.left(90)
     t.forward(35)
     t.forward(-17.5)
     
     
     
     t.right(90)
     t.forward(25)
     t.fillcolor("orange")
     t.begin_fill()
     t.left(90)
     t.forward(20)
     t.right(90)
     t.forward(10)
     t.right(90)
     t.forward(20)
     t.left(90)
     t.forward(-20)
     t.end_fill()
     t.forward(40)
     t.left(85)
     t.forward(90)
     t.left(95)
     t.forward(70)
     
     
     t.forward(-70)
     t.right(180)
     t.fillcolor("blue")
     t.begin_fill()
     t.left(35)
     t.forward(70)
     t.left(55)
     t.forward(113)
     t.left(90)
     t.goto(0,100)
     t.left(90)
     t.forward(153)
     t.forward(-153)
     t.end_fill()
     t.goto(0,0)
     t.goto(0,157)
     t.fillcolor("blue")
     t.begin_fill()
     t.goto(-60,157)
     t.right(110)
     t.forward(61)
     t.goto(0,100)
     t.end_fill()
     t.goto(-82,100)
     t.right(60)
     t.forward(45)
     t.left(80)
     
     t.forward(20)
     t.fillcolor("red")
     t.begin_fill()
     t.left(90)
     t.forward(20)
     t.right(90)
     t.forward(10)
     t.right(90)
     t.forward(20)
     t.left(90)
     t.forward(-20)
     t.end_fill()
     t.forward(40)
     
     
     t.left(90)
     t.forward(20)
     t.forward(-40)
     t.right(90)
     t.goto(-146,0)
     t.left(90)
     t.forward(37)
     

     #leftwheel
     t.penup()
     t.goto(-73,-30)
     t.pendown()
     t.fillcolor("black")
     t.begin_fill()
     t.circle(40)
     t.penup()
     t.goto(-72,-15)
     t.pendown()
     t.end_fill()
     t.fillcolor("grey")
     t.begin_fill()
     t.circle(25)
     t.left(90)
     t.forward(25)
     t.right(30)
     t.forward(25)
     t.forward(-25)
     t.right(70)
     t.forward(25)
     t.forward(-25)
     t.left(150)
     t.forward(25)
     t.forward(-25)
     t.left(60)
     t.forward(25)
     t.left(159)
     t.end_fill()
     

     #restofframe
     t.penup()
     t.forward(60)
     t.pendown()
     t.goto(0,0)
    

     #road
     t.right(90)
     t.penup()
     t.forward(32)
     t.pencolor("black")
     t.fillcolor("black")
     t.begin_fill()
     t.right(89)
     t.pendown()
     t.forward(200)
     t.forward(-500)
     t.left(90)
     t.forward(15)
     t.right(90)
     t.forward(500)
     t.right(90)
     t.forward(15)
     t.end_fill()

     
#######################
# Question 11
#######################

def alogical(n):
     '''

     (number)->int

     n>=1
     
     Returns the amount of times that n must be divided by 2 to become less than or equal to 1.
     
     '''
     return math.ceil(math.log(n, 10)/math.log(2,10))

#######################
# Question 12
#######################

def time_format(h,m):
     '''

     (int,int)->str

     Returns the time in a descriptive string displaying the hour, h, and the minute, m, rounded to the nearest 5 minutes.

     0<=h<=23
     0<=m<=59
     
     '''
     roundedminute=int(5*round(float(m)/5))
     if 0<=h<23:
          if m<=27:
               if roundedminute==0:
                    return(str(h)+" o'clock")
               else:
                    return(str(roundedminute)+" minutes past "+str(h)+" o'clock")
          if 27<m<=32:
                    return("half past"+" "+str(h)+" o'clock")
          if 33<m<=57:
                    return(str(60-roundedminute)+" minutes to "+str(h+1)+" o'clock")
          if m>57:
                    return(str(h+1)+" o'clock")
     if h>=23:
          if m<=27:
               if roundedminute==0:
                    return(str(h)+" o'clock")
               else:
                    return(str(roundedminute)+" minutes past "+str(h)+" o'clock")
          if 27<m<=32:
                    return("half past"+" "+str(h)+" o'clock")
          if 33<m<=57:
                    return(str(60-roundedminute)+" minutes to 0 o'clock")
          if m>57:
                    return("0 o'clock")

     
#######################
# Question 13
#######################

def cad_cashier(price,paid):
     '''

     (number,number)->float

     price>=0
     paid>=0

     Returns the amount of change based on the differnece between amount paid and the price.
     
     '''
     return round(paid-((round((price/5),2))*5),2)

#######################
# Question 14
#######################

def min_CAD_coins(price,payment):
     '''

     (number,number)->tuple

     Calls upon cad_cashier and returns the change in the minimum number of coins.
     
     '''
     changeincents=round((cad_cashier(price,payment))*100)
     t=changeincents//200
     l=(changeincents-(200*t))//100
     q=(changeincents-(200*t)-(100*l))//25
     d=(changeincents-(200*t)-(100*l)-(25*q))//10
     n=(changeincents-(200*t)-(100*l)-(25*q)-(10*d))//5
     return (t,l,q,d,n)
