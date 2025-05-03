# logical operators (and, or, not) = used to check if two or more conditional statements are true 
# not operator just flips everything ... think oposite day 

temp = int(input("What is the tempreture like today?: "))

if not(temp >= 15 and temp <= 30):
    print("the tempreture is good today!")
    print("go outside")
elif not(temp < 15):
    print("the tempreture is quite cold")
    print("wear a coat if you are going outside")