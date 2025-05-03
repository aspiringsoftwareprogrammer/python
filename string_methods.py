# to get length of string use len
# find to get the index of a char 
# capitalise to get the first letter to be full caps 
# upper makes your chars all upper case 
# lower makes your chars all lower case 
# .isdigit - returns true or false if there is a digit in the string 
# .isalpha - check if all chars are alphabetical if there is a space will say false 
# count - how many chars they are overall or how many chars of a specific value like p 
# replace - change char value
# can repeat string value * num of times 


# completed the following katas 
# A Needle in the Haystack

def find_needle(haystack):
    
    index = haystack.index('needle')
    return "found the needle at position " + str(index)

#All Star Code Challenge #18

def str_count(strng, letter):
    return strng.count(letter)

# Grasshopper - Debug sayHello

def say_hello(name):
    return "Hello" + ", " + name

