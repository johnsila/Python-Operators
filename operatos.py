#arithmetric operators
print("ARITHMETRIC OPERATORS")
print("")
a=18
b=20
print("a=18")
print("b=20")
print("")
#addition
print("sum=",a+b)

#subtraction
print("remeinder=,",a-b)

#division
print("division=",a/b)

#multiplication
print("product=",a*b)

#modulus
print("module=",a%b)

#exponentiation
#a number raised to anothera^b
print("expontention=",a**b)

#Floor division 
print("floor division",a//b)

print("")
#assignment operators
print("ASSIGNMENT OPERATORS")
print("")
x=10
print("x=10")

#(x+3)
x+=3
print("+=3 ;",x)

#-=
y=10
y-=3
print("-=3 ;",y)

#*=
z=10
z*=4
print("*=4 ;",z)

#/=
z=10
z/=4
print("/=4 ;",z)

#%=
z=10
z%=4
print("%=4 ;",z)

#**=
z=10
z**=4
print("**=4 ;",z)

#//=
z=10
z//=4
print("//=4 ;",z)

#&=
z=10
z&=4
print("&=4 ;",z)

#|=
z=10
z|=4
print("|=4 ;",z)

#^=
z=10
z^=4
print("^=4 ;",z)

#>>=
z=10
z>>=4
print(">>= ;",z)

#<<=
z=10
z>>=4
print("<<= ;",z)

print("  ")
#Comparison operators
print("comparison operators")
print(" ")

#== equals to
x=12
y=14
print("x=12, y=14")
print("x==y =",x==y)#returns false since x is not equals to y

#not equls(!=)
print("x!Y =",x!=y)#returns true since x is not equals to y

#grater than(>)
print("x>Y =",x>y)#returns flase since x is not grater than to y

#less than(<)
print("x<Y =",x<y)#returns true since x is less than  y

#Greater than or equal to	x >= y
print("x>=Y =",x>=y)#returns false since x is less than and not equals to   y

#Less than or equal to	x <= y
print("x<=Y =",x<=y)#returns true since x is less than but not equal to   y

#logical operators
print("")
print("Logical operators")
#and
print("and operator")#Returns True if both statements are true
x = 5
print("x=5")
print("and;x > 3 and x < 10 =",x > 3 and x < 10)# returns True because 5 is greater than 3 AND 5 is less than 10
#or
print("or;x > 3 or x < 4 =",x > 3 or x < 4)# returns True because one of the conditions are true (5 is greater than 3, but 5 is not less than 4)
#not
print("not;x > 3 and x < 10 =",not(x > 3 and x < 10))# returns False because not is used to reverse the result

print("")
#identity operators

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print("x=",x)
print("y=",y)
print("z=,",z)
print("")

#is
print("is operator")
print("is x z;",x is z)# returns True because z is the same object as x

print("is x y;",x is y)# returns False because x is not the same object as y, even if they have the same content

print("isx==y;",x == y)# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y

#is not
print("")
print("Is not operator")

print("x is not z;",x is not z)# returns False because z is the same object as x

print("x is not y;",x is not y)# returns True because x is not the same object as y, even if they have the same content

print("x!=y;",x != y)# to demonstrate the difference betweeen "is not" and "!=": this comparison returns False because x is equal to y

print("")
#membership operatos
print("MEMBERSHIP OPERATOS, IN, NOT IN")
print("")

print("IN")
x = ["apple", "banana"]
print("x=",x)
print("")
print("NOT IN")
print("is banana in x;","banana" in x)# returns True because a sequence with the value "banana" is in the list
print("is pineapple not in x;" ,"pineapple" not in x)# returns True because a sequence with the value "pineapple" is not in the list
