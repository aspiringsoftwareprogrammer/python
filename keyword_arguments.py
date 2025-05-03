# arguments preceeded by an indicator when we pass them to a function, the order of the argument doesnt matter
# unlike professional arguments Python knows the names of the arguments that our function recieves 

def greeting(first,middle,last):
    print("Hello "+ " " + first +  " " + middle +  " " + last)

print(greeting(first="henry", middle="newtom", last="bartholamew"))