# loop control statements = change a loops execution from its normal sequence 
# break = used to terminate the loop entirely 
# continue = skips to the next iteration of the loop
# pass = does nothing, acts as a placeholder 

while True:
    name = input("What is your name?: ")
    if name != "":
        break

phone_number = "1234-345345-13123-4"

for i in phone_number:
    if i == "-":
        continue
    print(i, end="")  

# # here end="" -- means that the value will not be in the next like like 
'''
5
3
4
5
1
3
1
2
3

but instead it will print like 
1234345345131234
'''

for i in range(1, 11):
    if i == 9:
        pass
    else:
        print(i, end="")
    