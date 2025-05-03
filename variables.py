#bro code youtube series 
# variable = a container for a value. Behaves as the value that it contains 
# you can't do any maths with a string 
# can't do any string concatenation with int or float data types 
# solution is casting wrap the variable with the data type you want to convert it to at the start so string(age) - age was a int is not a string

# casting practice 

height = 21.9
greeting = "Hi i am " + str(height) + " cm tall"
print(type(height))
print(greeting)

# before adding casting got the following error TypeError: can only concatenate str (not "float") to str
