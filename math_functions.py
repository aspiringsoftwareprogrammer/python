import math 

pi = 3.14 
x = 4
y = 0
z = 9
print(round(pi))
print(math.ceil(pi)) # round up
print(math.floor(pi)) # round down
print(abs(pi)) # absolute value - aka how far away a number is from 0
print(pow(pi,2)) # power to x
print(math.sqrt(pi)) # finds the square root 
print(max(x,y,z)) # finds max value 
print(min(x,y,z)) # finds min value 

#Simple multiplication

def simple_multiplication(number) :
    res = number * 8 if number % 2 == 0 else number * 9
    return res

#Super Duper Easy

def problem(a):
    res = "Error" if type(a) == str else a * 50 + 6
    return res

# 5 without numbers !!

def unusual_five():
    a = "apple"
    return(len(a))