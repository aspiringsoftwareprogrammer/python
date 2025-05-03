# for loop = a statement that will execute its block of code a limited amount of times
# while loop = unlimited 
# for loop = limited 
# (x,x,x)first num is inclusive, the second is exclusive and the third is step 

import time 

for i in range(10):
    print(i+1)

for i in range(90, 101, 2):
    print(i)

# can iterate over a string, or any sort of collection 
for i in "Bro Code":
    print(i)

for seconds in range(5,0,-1):
    print(seconds)
    time.sleep(1)
print("Happy New Year!")

