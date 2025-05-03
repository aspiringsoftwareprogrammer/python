# if statement = a block of code that will execute if its condition is true 
# any indented code underneath an if statement is a bloc of code for that if statement 
# always checks if statement is first if it is true it ignores everything below 
# order of the if statement matters!


age = int(input("How old are you?: "))

if age >= 18:
    print("You are an adult")
elif age < 0:
    print("You have not even been born yet")
else:
    print("You are a child")
